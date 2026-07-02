"""
sensitivity_test.py
===================
Modul pengujian sensitivitas bobot (Weight Perturbation Analysis).

Fungsi utama:
  perturb_weights()     — Modifikasi bobot sebesar delta_pct persen
  compute_spearman()    — Hitung korelasi Spearman antara dua vektor peringkat
  detect_reversal()     — Deteksi apakah ada perubahan peringkat (rank reversal)
  run_sensitivity_test()— Jalankan satu skenario uji sensitivitas lengkap
"""

import numpy as np
from scipy import stats


# ══════════════════════════════════════════════════════════
# Perturbasi Bobot
# ══════════════════════════════════════════════════════════

def perturb_weights(
    base_weights: np.ndarray,
    delta_pct: float,
    mode: str = "uniform",
    rng: np.random.Generator | None = None,
) -> np.ndarray:
    """
    Tambahkan gangguan (perturbation) pada vektor bobot.

    Parameters
    ----------
    base_weights : np.ndarray (k,) — bobot asli (sum ≈ 1.0)
    delta_pct    : float — besar gangguan dalam persen (0–100)
    mode         : 'uniform'  — semua bobot bergeser seragam
                   'random'   — gangguan random tiap bobot
    rng          : numpy Generator untuk mode random (opsional)

    Returns
    -------
    np.ndarray (k,) — bobot setelah gangguan (sum = 1.0)
    """
    w = base_weights.copy().astype(float)
    delta = delta_pct / 100.0

    if mode == "uniform":
        # Geser semua bobot ke arah seragam (lebih adil/rata)
        uniform = np.ones_like(w) / len(w)
        perturbed = (1 - delta) * w + delta * uniform
    elif mode == "random":
        if rng is None:
            rng = np.random.default_rng(42)
        noise = rng.uniform(-delta, delta, size=len(w))
        perturbed = w + noise * w       # gangguan proporsional
        perturbed = np.clip(perturbed, 1e-6, None)
    else:
        raise ValueError(f"Mode tidak dikenal: {mode!r}. Gunakan 'uniform' atau 'random'.")

    # Normalisasi ulang
    perturbed /= perturbed.sum()
    return perturbed


# ══════════════════════════════════════════════════════════
# Metrik Statistik
# ══════════════════════════════════════════════════════════

def compute_spearman(
    ranks_base: np.ndarray,
    ranks_perturbed: np.ndarray,
) -> float:
    """
    Hitung Spearman Rank Correlation Coefficient (ρ) antara dua vektor peringkat.

    Parameters
    ----------
    ranks_base      : np.ndarray (m,) — peringkat baseline
    ranks_perturbed : np.ndarray (m,) — peringkat setelah perturbasi

    Returns
    -------
    float — nilai ρ dalam [-1.0, 1.0]
    """
    rho, _ = stats.spearmanr(ranks_base, ranks_perturbed)
    return float(rho)


def detect_reversal(
    ranks_base: np.ndarray,
    ranks_perturbed: np.ndarray,
    top_k: int = 10,
) -> bool:
    """
    Deteksi rank reversal pada top-K alternatif.

    Rank reversal dianggap terjadi jika ada alternatif yang:
    - Sebelumnya masuk top-K, lalu keluar (atau sebaliknya)

    Parameters
    ----------
    ranks_base      : np.ndarray (m,) — peringkat baseline
    ranks_perturbed : np.ndarray (m,) — peringkat setelah perturbasi
    top_k           : int — jumlah posisi teratas yang diawasi

    Returns
    -------
    bool — True jika ada rank reversal pada top-K
    """
    top_base      = set(np.where(ranks_base      <= top_k)[0])
    top_perturbed = set(np.where(ranks_perturbed <= top_k)[0])
    return top_base != top_perturbed


def compute_kendall_tau(
    ranks_base: np.ndarray,
    ranks_perturbed: np.ndarray,
) -> float:
    """Hitung Kendall's Tau-b sebagai metrik korelasi tambahan."""
    tau, _ = stats.kendalltau(ranks_base, ranks_perturbed)
    return float(tau)


# ══════════════════════════════════════════════════════════
# Skenario Uji Sensitivitas
# ══════════════════════════════════════════════════════════

def run_sensitivity_test(
    delta_w_pct: float,
    base_weights: np.ndarray,
    base_ranks: np.ndarray,
    decision_matrix: np.ndarray,
    pairwise_matrix: np.ndarray,
    run_ahp_topsis_fn,
    top_k: int = 10,
) -> dict:
    """
    Jalankan satu skenario uji sensitivitas pada satu nilai delta_w.

    Steps:
      1. Buat bobot terganggu
      2. Jalankan ulang AHP-TOPSIS dengan bobot terganggu
      3. Hitung Spearman ρ dan deteksi rank reversal

    Parameters
    ----------
    delta_w_pct      : float — besar gangguan bobot (%)
    base_weights     : np.ndarray — bobot AHP asli (13,)
    base_ranks       : np.ndarray — peringkat TOPSIS baseline
    decision_matrix  : np.ndarray — matriks keputusan (m × 13)
    pairwise_matrix  : np.ndarray — matriks AHP (4 × 4)
    run_ahp_topsis_fn: callable — fungsi run_ahp_topsis dari ahp_topsis.py
    top_k            : int — threshold rank reversal detection

    Returns
    -------
    dict dengan kunci:
      - delta_w_pct     : float
      - perturbed_weights: np.ndarray
      - perturbed_ranks  : np.ndarray
      - spearman_rho     : float
      - kendall_tau      : float
      - reversal_detected: bool
    """
    # 1. Perturbasi bobot
    perturbed_w = perturb_weights(base_weights, delta_w_pct, mode="uniform")

    # 2. Jalankan ulang dengan sub_weights yang sudah diperturbasi
    result = run_ahp_topsis_fn(
        decision_matrix=decision_matrix,
        pairwise_matrix=pairwise_matrix,
        sub_weights=perturbed_w,
    )
    perturbed_ranks = result["ranks"]

    # 3. Hitung metrik
    rho = compute_spearman(base_ranks, perturbed_ranks)
    tau = compute_kendall_tau(base_ranks, perturbed_ranks)
    reversal = detect_reversal(base_ranks, perturbed_ranks, top_k=top_k)

    return {
        "delta_w_pct":      delta_w_pct,
        "perturbed_weights": perturbed_w,
        "perturbed_ranks":   perturbed_ranks,
        "spearman_rho":      rho,
        "kendall_tau":       tau,
        "reversal_detected": reversal,
    }
