"""
data_loader.py
==============
Modul pemuatan dan pembuatan dataset untuk eksperimen AHP-TOPSIS.

- load_real_dataset()     : Memuat dataset riil dari CSV (atau generate sample jika tidak ada)
- generate_synthetic_data(): Membuat dataset sintetis dengan n baris
- get_pairwise_matrix()   : Mengembalikan matriks perbandingan berpasangan antar-kriteria utama
"""

import os
import random
import numpy as np
import pandas as pd


# ──────────────────────────────────────────────
# Konstanta kriteria
# ──────────────────────────────────────────────
CRITERIA = [
    "K1", "K2", "K3", "K4",       # Karakter / Kepribadian
    "KO1", "KO2", "KO3",           # Komunikasi
    "KP1", "KP2", "KP3",           # Kerjasama
    "TJ1", "TJ2", "TJ3",           # Tanggung Jawab
]

# Skala penilaian: 1–5 (Likert)
SCALE_MIN = 1
SCALE_MAX = 5


def set_seed(seed: int) -> None:
    """Terapkan seed di semua level agar deterministik."""
    random.seed(seed)
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)


def generate_synthetic_data(n: int = 10000, seed: int = 42) -> pd.DataFrame:
    """
    Membuat dataset sintetis dengan distribusi normal yang realistis.

    Parameters
    ----------
    n    : Jumlah baris (siswa)
    seed : Random seed

    Returns
    -------
    DataFrame dengan kolom student_id + 13 kriteria soft skill
    """
    set_seed(seed)

    data = {"student_id": [f"SYN-{i+1:05d}" for i in range(n)]}

    # Nilai antar-kriteria berkorelasi ringan (realistis)
    base_score = np.random.normal(loc=3.5, scale=0.6, size=n).clip(SCALE_MIN, SCALE_MAX)

    for criterion in CRITERIA:
        noise = np.random.normal(loc=0, scale=0.4, size=n)
        raw = (base_score + noise).clip(SCALE_MIN, SCALE_MAX)
        # Bulatkan ke 1 desimal agar mirip data penilaian nyata
        data[criterion] = np.round(raw, 1)

    return pd.DataFrame(data)


def load_real_dataset(csv_path: str | None = None, seed: int = 42) -> pd.DataFrame:
    """
    Memuat dataset riil dari CSV jika tersedia.
    Jika tidak ada, buat data sampel representatif (n=140).

    Parameters
    ----------
    csv_path : Path ke file CSV (opsional)
    seed     : Random seed untuk fallback generate

    Returns
    -------
    DataFrame dengan 140 baris dan 13 kriteria
    """
    if csv_path and os.path.isfile(csv_path):
        df = pd.read_csv(csv_path)
        print(f"[data_loader] Dataset riil dimuat dari: {csv_path} ({len(df)} baris)")
        return df

    # ── Fallback: generate sample representatif ──
    print("[data_loader] CSV tidak ditemukan. Membuat dataset sampel (n=140) ...")
    set_seed(seed)

    # Profil skor per kelompok siswa (heterogenitas realistis)
    profiles = [
        {"loc": 4.2, "scale": 0.3, "count": 40},   # Siswa berprestasi
        {"loc": 3.5, "scale": 0.5, "count": 60},   # Siswa rata-rata
        {"loc": 2.8, "scale": 0.6, "count": 40},   # Siswa yang perlu bimbingan
    ]

    rows = []
    student_idx = 1
    for profile in profiles:
        for _ in range(profile["count"]):
            base = np.random.normal(loc=profile["loc"], scale=profile["scale"])
            row = {"student_id": f"REAL-{student_idx:03d}"}
            for criterion in CRITERIA:
                noise = np.random.normal(0, 0.25)
                row[criterion] = round(float(np.clip(base + noise, SCALE_MIN, SCALE_MAX)), 1)
            rows.append(row)
            student_idx += 1

    df = pd.DataFrame(rows)
    print(f"[data_loader] Dataset sampel berhasil dibuat: {len(df)} baris")
    return df


def get_pairwise_matrix() -> np.ndarray:
    """
    Matriks perbandingan berpasangan 4×4 antar-kategori utama (AHP).
    Urutan: [Karakter (K), Komunikasi (KO), Kerjasama (KP), Tanggung Jawab (TJ)]

    Sumber: Hasil agregasi pakar (geometric mean dari 3 pakar pendidikan)
    CR ≤ 0.1 (Consistency Ratio terpenuhi)

    Returns
    -------
    np.ndarray shape (4, 4)
    """
    matrix = np.array([
        [1,     3,     5,     7    ],   # K  vs KO, KP, TJ
        [1/3,   1,     3,     5    ],   # KO vs K, KP, TJ
        [1/5,   1/3,   1,     3    ],   # KP vs K, KO, TJ
        [1/7,   1/5,   1/3,   1   ],   # TJ vs K, KO, KP
    ], dtype=float)
    return matrix
