# Arsitektur dan Skema Instrumen — Benchmarking AHP-TOPSIS (Noise Injection)

Dokumen ini memaparkan arsitektur komponen skrip benchmarking, alur kalkulasi algoritma hibrida (AHP dan TOPSIS) beserta skenario **noise injection** untuk pengujian sensitivitas, skema struktur file CSV input/output, serta pemetaan desain teori ke dalam implementasi modul penelitian.

---

## 1. Diagram Arsitektur Komponen

Sistem terdiri dari dua *layer* utama: sistem operasional DSS dan instrumen eksperimen (skrip benchmarking). Dalam penelitian ini, fokus berada pada **Benchmarking Engine** sebagai instrumen pengujian ketangguhan algoritma.

```mermaid
graph TD
    subgraph "Sumber Data (CSV)"
        DS_RIIL[/Dataset Riil\n140 Siswa × 13 Indikator/]
        DS_SINTETIS[/Dataset Sintetis\nPerluasan s.d. 10.000 Entri/]
    end

    subgraph "Benchmarking Engine (CLI)"
        DL[data_loader.py]
        ENGINE[ahp_topsis.py\nCalculation Engine]
        ST[sensitivity_test.py\nNoise Injection & Metrik]
        LG[logger.py\nPerekam Hasil]
    end

    subgraph "Output Artefak (CSV)"
        LOG[/Log Eksperimen\ndelta_w, spearman_rho, runtime_ms/]
        REPORT[Laporan Analisis\nAmbang Toleransi Stabilitas]
    end

    DS_RIIL --> DL
    DS_SINTETIS --> DL
    DL --> ST
    ST <-->|Iterasi Uji Sensitivitas| ENGINE
    ST --> LG
    LG --> LOG
    LOG --> REPORT
```

---

## 2. Alur Kalkulasi Algoritma (Flowchart Lengkap)

Alur dari pembacaan data hingga pemetaan ambang batas toleransi stabilitas.

```mermaid
flowchart TD
    A([Mulai]) --> B[Load Dataset Riil / Sintetis]
    B --> C[Input Matriks Perbandingan Berpasangan oleh Pakar]
    C --> D[Hitung Bobot Eigen & Consistency Ratio AHP]

    D --> E{CR ≤ 0.1?}
    E -- Tidak --> F[Revisi Matriks Pakar]
    F --> C
    E -- Ya --> G[Simpan Bobot Kriteria Baseline]

    G --> H[Jalankan TOPSIS Baseline\ntanpa Deviasi Bobot]
    H --> I[Simpan Urutan Peringkat Acuan]

    I --> J[Loop: Level Deviasi ΔW\n±10% → ±20% → ... → ±50%]
    J --> K[Weight Manipulator:\nSuntikkan Deviasi pada Kriteria Bobot Tertinggi]
    K --> L[Normalisasi Ulang Bobot Kriteria]
    L --> M[Jalankan TOPSIS dengan Bobot Terdeviasi]
    M --> N[Hitung Korelasi Rank Spearman ρ\nvs. Peringkat Acuan]
    N --> O[Catat Runtime ms]

    O --> P{Masih ada level ΔW\nberikutnya?}
    P -- Ya --> J
    P -- Tidak --> Q[Analisis Hasil:\nPetakan Ambang Toleransi Stabilitas]

    Q --> R([Selesai / Ekspor Laporan])
```

---

## 3. Skema Struktur Matriks Data (Input & Output)

Proyek ini mendasarkan perhitungannya pada matriks keputusan (tanpa database relasional). Berikut adalah struktur konseptual data yang diolah:

### A. Matriks Data Input Utama (Dataset Riil)

| Kolom | Tipe | Keterangan |
|-------|------|------------|
| `Alternatif` | string | Nama atau ID alternatif (contoh: Siswa-1) |
| `C11` – `C14` | float | Skor observasi Karakter / Kepribadian |
| `C21` – `C23` | float | Skor observasi Komunikasi |
| `C31` – `C33` | float | Skor observasi Kerjasama |
| `C41` – `C43` | float | Skor observasi Tanggung Jawab |

> Total: 13 kolom skor kriteria + 1 kolom identitas.

### B. Matriks Data Perluasan (Dataset Sintetis)

Format kolom sama seperti dataset riil, namun berisi hingga **10.000 baris** alternatif yang dibangkitkan secara terprogram untuk menguji performa beban (eksekusi matriks skala besar).


### C. Struktur Log Hasil Eksperimen

| Kolom | Tipe | Keterangan |
|-------|------|------------|
| `run_id` | int | Nomor iterasi eksperimen |
| `dataset_type` | string | `riil` atau `sintetis` |
| `n_alternatif` | int | Jumlah baris data yang diuji |
| `delta_w` | float | Tingkat deviasi bobot yang disuntikkan (0.0, 0.1, ..., 0.5) |
| `spearman_rho` | float | Koefisien korelasi Rank Spearman vs. baseline |
| `runtime_ms` | float | Waktu eksekusi algoritma end-to-end (ms) |

---
