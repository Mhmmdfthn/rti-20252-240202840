import os
import random
from pathlib import Path

import numpy as np
import pandas as pd

# ──────────────────────────────────────────────
# Konstanta kriteria
# ──────────────────────────────────────────────
CRITERIA = [
    "C11",
    "C12",
    "C13",
    "C14",  # Karakter / Kepribadian
    "C21",
    "C22",
    "C23",  # Komunikasi
    "C31",
    "C32",
    "C33",  # Kerjasama
    "C41",
    "C42",
    "C43",  # Tanggung Jawab
]

# Skala penilaian: 1–5 (Likert)
SCALE_MIN = 1
SCALE_MAX = 5


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)


def generate_synthetic_data(n: int = 10000, seed: int = 42) -> pd.DataFrame:

    set_seed(seed)

    # Profil heterogenitas realistis
    profiles = [
        {"loc": 4.2, "scale": 0.35, "count": int(n * 0.40)},  # Berprestasi
        {"loc": 3.5, "scale": 0.55, "count": int(n * 0.40)},  # Rata-rata
        {
            "loc": 2.7,
            "scale": 0.60,
            "count": n - int(n * 0.40) - int(n * 0.40),
        },  # Perlu bimbingan
    ]

    rows = []
    student_idx = 1
    for profile in profiles:
        count = profile["count"]
        base_scores = np.random.normal(
            loc=profile["loc"], scale=profile["scale"], size=count
        ).clip(SCALE_MIN, SCALE_MAX)

        for i in range(count):
            row = {"student_id": f"SYN-{student_idx:05d}"}
            for criterion in CRITERIA:
                noise = np.random.normal(0, 0.30)
                row[criterion] = round(
                    float(np.clip(base_scores[i] + noise, SCALE_MIN, SCALE_MAX)), 1
                )
            rows.append(row)
            student_idx += 1

    df = pd.DataFrame(rows)
    print(
        f"[data_loader] Dataset sintetis berhasil dibuat: {len(df)} baris (seed={seed})"
    )
    return df


def load_real_data(csv_path: str | Path | None = None) -> pd.DataFrame:
    """Muat dataset riil dari file CSV.

    Kolom CSV asli (C11–C43) langsung digunakan.
    Kolom 'Alternatif' dijadikan index.

    Parameters
    ----------
    csv_path :
        Path ke file CSV.  Jika None, akan dicari secara otomatis di
        ``../../../../04-data/datasetsimulasi_riil_140.csv`` relatif
        terhadap direktori file ini.

    Returns
    -------
    pd.DataFrame
        DataFrame dengan kolom C11–C43 dan index nama siswa.

    Raises
    ------
    FileNotFoundError
        Jika file CSV tidak ditemukan.
    ValueError
        Jika kolom yang dibutuhkan tidak ada di CSV.
    """
    if csv_path is None:
        # Lokasi default: <repo>/example-riset-directory/04-data/datasetsimulasi_riil_140.csv
        csv_path = (
            Path(__file__).resolve().parents[3]
            / "04-data"
            / "datasetsimulasi_riil_140.csv"
        )
    csv_path = Path(csv_path)

    if not csv_path.exists():
        raise FileNotFoundError(
            f"[data_loader] File dataset riil tidak ditemukan: {csv_path}"
        )

    df = pd.read_csv(csv_path)

    # Validasi kolom
    missing = [c for c in CRITERIA if c not in df.columns]
    if missing:
        raise ValueError(
            f"[data_loader] Kolom berikut tidak ada di CSV: {missing}\n"
            f"Kolom yang tersedia: {list(df.columns)}"
        )

    # Jadikan kolom Alternatif sebagai index (jika ada)
    if "Alternatif" in df.columns:
        df = df.set_index("Alternatif")

    # Pastikan semua nilai numerik
    df[CRITERIA] = df[CRITERIA].apply(pd.to_numeric, errors="coerce")

    n_before = len(df)
    df = df.dropna(subset=CRITERIA)
    n_dropped = n_before - len(df)
    if n_dropped:
        print(f"[data_loader] {n_dropped} baris di-drop karena nilai kosong/NaN.")

    print(
        f"[data_loader] Dataset riil berhasil dimuat: {len(df)} baris "
        f"dari '{csv_path.name}'"
    )
    return df


def get_pairwise_matrix() -> np.ndarray:

    matrix = np.array(
        [
            [1, 3, 5, 7],  # K  vs KO, KP, TJ
            [1 / 3, 1, 3, 5],  # KO vs K, KP, TJ
            [1 / 5, 1 / 3, 1, 3],  # KP vs K, KO, TJ
            [1 / 7, 1 / 5, 1 / 3, 1],  # TJ vs K, KO, KP
        ],
        dtype=float,
    )
    return matrix
