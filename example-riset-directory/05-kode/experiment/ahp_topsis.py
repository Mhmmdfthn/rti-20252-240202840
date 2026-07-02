"""
ahp_topsis.py
=============
Implementasi inti algoritma hibrida AHP-TOPSIS.

Struktur:
  AHPCalculator   — menghitung bobot prioritas dari matriks perbandingan berpasangan
  TOPSISRanker    — memberi peringkat alternatif menggunakan bobot AHP
  run_ahp_topsis  — fungsi entry-point yang menyatukan keduanya
"""

import numpy as np


# ══════════════════════════════════════════════════════════
# AHP — Analytic Hierarchy Process
# ══════════════════════════════════════════════════════════

# Random Index (RI) untuk n = 1..10
_RI_TABLE = {1: 0.00, 2: 0.00, 3: 0.58, 4: 0.90,
             5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41,
             9: 1.45, 10: 1.51}


class AHPCalculator:
    """
    Hitung bobot prioritas dari matriks perbandingan berpasangan (AHP).

    Parameters
    ----------
    matrix : np.ndarray, shape (n, n)
        Matriks perbandingan berpasangan (nilai positif, resiprokal).
    """

    def __init__(self, matrix: np.ndarray):
        self.matrix = matrix.astype(float)
        self.n = matrix.shape[0]
        self._weights: np.ndarray | None = None
        self._cr: float | None = None

    # ── Public API ──────────────────────────────────────
    def compute_weights(self) -> np.ndarray:
        """Hitung dan kembalikan vektor bobot prioritas (sum = 1.0)."""
        if self._weights is None:
            self._weights = self._eigenvector_method()
        return self._weights

    def consistency_ratio(self) -> float:
        """Hitung Consistency Ratio (CR). Nilai < 0.1 diterima."""
        if self._cr is None:
            w = self.compute_weights()
            lam_max = float(np.mean(
                (self.matrix @ w) / w
            ))
            n = self.n
            ci = (lam_max - n) / (n - 1)
            ri = _RI_TABLE.get(n, 1.51)
            self._cr = ci / ri if ri > 0 else 0.0
        return self._cr

    def is_consistent(self, threshold: float = 0.1) -> bool:
        return self.consistency_ratio() <= threshold

    # ── Private ─────────────────────────────────────────
    def _eigenvector_method(self) -> np.ndarray:
        """Metode eigenvector utama (approx. geometric mean per baris)."""
        geo_means = np.prod(self.matrix, axis=1) ** (1 / self.n)
        weights = geo_means / geo_means.sum()
        return weights


# ══════════════════════════════════════════════════════════
# TOPSIS — Technique for Order Preference by Similarity to Ideal Solution
# ══════════════════════════════════════════════════════════

class TOPSISRanker:
    """
    Beri peringkat alternatif menggunakan metode TOPSIS.

    Parameters
    ----------
    decision_matrix : np.ndarray, shape (m, k)
        m = jumlah alternatif, k = jumlah kriteria
    weights         : np.ndarray, shape (k,)
        Bobot tiap kriteria (sum = 1.0), biasanya dari AHP
    benefit_mask    : np.ndarray bool, shape (k,) — opsional
        True  = kriteria benefit (semakin tinggi semakin baik)
        False = kriteria cost    (semakin rendah semakin baik)
        Default: semua benefit
    """

    def __init__(
        self,
        decision_matrix: np.ndarray,
        weights: np.ndarray,
        benefit_mask: np.ndarray | None = None,
    ):
        self.dm = decision_matrix.astype(float)
        self.weights = weights.astype(float)
        m, k = self.dm.shape
        self.m = m
        self.k = k

        if benefit_mask is None:
            self.benefit_mask = np.ones(k, dtype=bool)
        else:
            self.benefit_mask = np.asarray(benefit_mask, dtype=bool)

        self._scores: np.ndarray | None = None
        self._ranks: np.ndarray | None = None

    # ── Public API ──────────────────────────────────────
    def compute_scores(self) -> np.ndarray:
        """Hitung skor kedekatan relatif (closeness coefficient) tiap alternatif."""
        if self._scores is None:
            self._scores = self._topsis_pipeline()
        return self._scores

    def get_ranking(self) -> np.ndarray:
        """Kembalikan array peringkat (1 = terbaik) untuk setiap alternatif."""
        if self._ranks is None:
            scores = self.compute_scores()
            # rankdata dari scipy versi sederhana (descending)
            order = np.argsort(-scores)           # indeks dari skor tertinggi
            ranks = np.empty_like(order)
            ranks[order] = np.arange(1, self.m + 1)
            self._ranks = ranks
        return self._ranks

    # ── Private ─────────────────────────────────────────
    def _topsis_pipeline(self) -> np.ndarray:
        dm = self.dm
        w  = self.weights

        # 1. Normalisasi vektor (Euclidean)
        norms = np.linalg.norm(dm, axis=0)
        norms[norms == 0] = 1e-12               # hindari division by zero
        normalized = dm / norms

        # 2. Matriks keputusan berbobot
        weighted = normalized * w

        # 3. Ideal positif (A+) dan negatif (A-)
        a_pos = np.where(self.benefit_mask, weighted.max(axis=0), weighted.min(axis=0))
        a_neg = np.where(self.benefit_mask, weighted.min(axis=0), weighted.max(axis=0))

        # 4. Jarak Euclidean ke ideal
        d_pos = np.sqrt(((weighted - a_pos) ** 2).sum(axis=1))
        d_neg = np.sqrt(((weighted - a_neg) ** 2).sum(axis=1))

        # 5. Closeness coefficient
        denom = d_pos + d_neg
        denom[denom == 0] = 1e-12
        scores = d_neg / denom

        return scores


# ══════════════════════════════════════════════════════════
# Entry-point tunggal
# ══════════════════════════════════════════════════════════

def run_ahp_topsis(
    decision_matrix: np.ndarray,
    pairwise_matrix: np.ndarray,
    sub_weights: np.ndarray | None = None,
) -> dict:
    """
    Jalankan pipeline AHP → TOPSIS secara lengkap.

    Alur:
      1. AHP: hitung bobot antar-kategori (dari pairwise_matrix)
      2. Gabungkan bobot kategori dengan sub-bobot kriteria (uniform jika None)
      3. TOPSIS: beri peringkat alternatif

    Parameters
    ----------
    decision_matrix : np.ndarray (m × 13) — skor siswa untuk 13 kriteria
    pairwise_matrix : np.ndarray (4 × 4)  — matriks perbandingan AHP
    sub_weights     : np.ndarray (13,) opsional — bobot dalam kategori
                      (default: uniform dalam tiap kategori)

    Returns
    -------
    dict dengan kunci:
      - weights      : np.ndarray (13,) bobot final per kriteria
      - scores       : np.ndarray (m,) closeness coefficient
      - ranks        : np.ndarray (m,) peringkat (1=terbaik)
      - cr           : float Consistency Ratio AHP
      - is_consistent: bool CR ≤ 0.1
    """
    # ── Langkah 1: AHP bobot kategori ──────────────────
    ahp = AHPCalculator(pairwise_matrix)
    category_weights = ahp.compute_weights()    # shape (4,)

    # ── Langkah 2: Distribusi ke 13 kriteria ───────────
    # Kategori: K(4), KO(3), KP(3), TJ(3)
    category_sizes = [4, 3, 3, 3]

    if sub_weights is None:
        # Uniform dalam setiap kategori
        final_weights = np.concatenate([
            np.full(sz, cw / sz)
            for cw, sz in zip(category_weights, category_sizes)
        ])
    else:
        # Gunakan sub_weights yang sudah dimodifikasi (untuk uji sensitivitas)
        final_weights = np.asarray(sub_weights, dtype=float)

    # Normalisasi ulang agar jumlah = 1
    total = final_weights.sum()
    if total > 0:
        final_weights /= total

    # ── Langkah 3: TOPSIS ──────────────────────────────
    topsis = TOPSISRanker(decision_matrix, final_weights)
    scores = topsis.compute_scores()
    ranks  = topsis.get_ranking()

    return {
        "weights":       final_weights,
        "scores":        scores,
        "ranks":         ranks,
        "cr":            ahp.consistency_ratio(),
        "is_consistent": ahp.is_consistent(),
    }
