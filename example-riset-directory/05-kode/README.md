# 05-kode

Direktori ini berisi source code implementasi untuk **Eksperimen Sensitivitas Bobot AHP-TOPSIS** (Decision Support System Evaluasi Soft Skill).

## Struktur Direktori

```text
05-kode/
└── experiment/               # Direktori utama kode eksperimen
    ├── src/                  # Modul source code utama
    │   ├── ahp_topsis.py     # Implementasi algoritma AHP dan TOPSIS
    │   ├── data_loader.py    # Modul untuk memuat atau men-generate data (Synthetic)
    │   ├── logger.py         # Sistem logging untuk mencatat hasil eksperimen
    │   └── sensitivity_test.py # Modul uji sensitivitas bobot
    ├── config/               # Konfigurasi
    │   └── experiment_config.json
    ├── main.py               # Entry-point utama untuk menjalankan eksperimen
    └── requirements.txt      # Daftar dependensi Python
```


## Acuan

Referensi dan landasan untuk implementasi kode eksperimen ini dapat dilihat pada dokumen berikut:
- **Perancangan Sistem & Eksperimen**: [../../worksheets/ws-06-system-experiment.md](../../worksheets/ws-06-system-experiment.md)
- **Desain Eksperimen Sensitivitas**: [../../worksheets/ws-07-experiment-design.md](../../worksheets/ws-07-experiment-design.md)
- **Implementasi (Kode)**: [../../worksheets/ws-09-implementation.md](../../worksheets/ws-09-implementation.md)
- **Validasi Data (AHP-TOPSIS)**: [../../worksheets/ws-11-data-validation.md](../../worksheets/ws-11-data-validation.md)
