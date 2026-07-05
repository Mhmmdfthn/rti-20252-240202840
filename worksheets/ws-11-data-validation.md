# WS-11: Data Validation & Integrity

> **Bab 11 — Validasi Data & Integritas**

---

## Ringkasan Materi

### Data Trust Model

```
Raw Data → Data Cleaning → Consistency Check → Validation Process → Trusted Data
```

Data mentah belum bisa dipercaya. Harus melewati pipeline validasi sebelum siap untuk analisis statistik.

### Empat Pilar Data Quality

| Pilar | Deskripsi | Contoh Pelanggaran |
|-------|----------|-------------------|
| **Accuracy** | Nilai dalam range masuk akal | Akurasi = 1.5 (di luar [0,1]) |
| **Consistency** | Format seragam di semua run | Run 1: CSV, Run 2: JSON |
| **Completeness** | Tidak ada data hilang dari plan | 97 dari 100 run tercatat |
| **Validity** | Data sesuai desain eksperimen | Parameter baseline tercampur treatment |

### Proses Validasi Progresif

1. **Format validation** — Tipe file, header, kolom
2. **Range validation** — Nilai dalam batas logis
3. **Consistency validation** — Format seragam antar-run
4. **Logic validation** — Data cocok dengan desain eksperimen

Jika gagal di langkah awal → tidak perlu lanjut.

### Anomaly Detection — 3 Jenis

| Jenis | Deskripsi | Deteksi |
|-------|----------|---------|
| **Statistical outlier** | Nilai di luar distribusi normal | IQR: < Q1-1.5×IQR atau > Q3+1.5×IQR |
| **Contextual anomaly** | Normal absolut, abnormal dalam konteks | Run 1-10: ~91%, Run 11-20: ~88% |
| **Pattern anomaly** | Pola sistematis (bukan random) | Performa menurun berurutan |

**Prinsip:** Detect → Investigate → Document → Decide — **JANGAN langsung hapus.**

### Engineering vs Research Validation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Data sesuai spesifikasi bisnis | Data layak untuk analisis statistik |
| Missing data | Impute / set default | Investigasi penyebab → dokumentasi |
| Outlier | Bug → fix | Mungkin temuan → investigasi |
| Dokumentasi | Minimal (log error) | Komprehensif (anomali + keputusan) |

### Jebakan Kognitif

1. "Logging otomatis ≠ data benar" → bisa ada bug di logger
2. "Outlier = hapus" → bisa jadi temuan penting
3. "Dataset kecil tidak perlu validasi" → justru lebih rentan
4. "Mean normal = data benar" → [94, 95, 93, **44**, 94] → mean 84% terlihat wajar

---

## Template A.11 — Data Validation Checklist

```
DATA VALIDATION CHECKLIST

Completeness:
  [x] Semua skenario tercakup
  [x] Jumlah run sesuai rencana
  [x] Tidak ada file output hilang
  Missing: 0 dari 60 data points

Format Consistency:
  [x] Semua file format sama (CSV/JSON/...)
  [x] Header konsisten
  [x] Tipe data konsisten (numerik tetap numerik)

Range & Logic:
  [x] Nilai dalam range masuk akal
  [x] Tidak ada waktu negatif
  [x] Metrik 0–100%, tidak di luar range
  Anomali ditemukan: 17 outlier pada runtime Real Dataset (tidak berdampak pada metrik utama).

Cross-Validation:
  [x] Run identik → hasil mendekati
  [x] Trend konsisten dengan ekspektasi teori

Keputusan:
  [x] Data siap analisis
  [ ] Perlu cleaning
  [ ] Perlu re-run (skenario: -)
```

---

## Latihan 1 — Completeness Check

Verifikasi apakah semua data yang direncanakan sudah terkumpul.

| Skenario | Run Direncanakan | Run Tercatat | Missing | Alasan |
|----------|-----------------|-------------|---------|--------|
| Real Dataset (n=140) | 30 | 30 | 0 | — |
| Synthetic Dataset (n=10000) | 30 | 30 | 0 | — |

**Total expected:** 60 | **Total actual:** 60 | **Missing:** 0

**Keputusan untuk data missing:**
> Tidak ada data yang hilang di hasil akhir pelaporan. Eksperimen tereksekusi secara utuh sebanyak 60 iterasi.

---

## Latihan 2 — Anomaly Investigation

Periksa data Anda untuk anomali. Gunakan metode IQR atau z-score.

**Dataset sampel (berdasarkan `anomaly_log.txt` terbaru):**

| Run | Runtime (ms) |
|-----|-------------|
| Real-0025 (Baseline) | 0.26 |
| Real-0026 | 2.05 |
| Real-0028 | 1.63 |
| Real-0022 | 3.09 |

**Deteksi outlier:**
- Baseline normal ≈ 0.26 ms - 0.52 ms
- Algoritma Logger memakai threshold dinamis: > 5× Baseline 
- Outlier terdeteksi: 17 run pada Real Dataset (contoh: Run 0022 mencapai 3.09 ms).

**Investigasi (untuk setiap outlier):**

| Outlier | Nilai | Kemungkinan Penyebab | Keputusan |
|---------|-------|---------------------|-----------|
| Real Dataset (17 anomali) | 1.37 - 3.09 ms | CPU interrupt atau overhead proses *background* OS sesaat saat mengeksekusi perhitungan matriks kecil (n=140). | Anomali runtime (terdeteksi flag anomaly = true) murni masalah overhead *benchmarking* OS, nilai luaran *ranking* dan Spearman Rho valid serta tidak terdistorsi. Data tetap dipertahankan. |

---

## Latihan 3 — Validation Report

Buat laporan validasi ringkas untuk dataset eksperimen Anda.

**1. Completeness:** 100% data terkumpul (60 dari 60 runs).
**2. Format:** [x] Konsisten / [ ] Ada inkonsistensi.
**3. Range check (anomali):** Beberapa *outlier* runtime muncul pada "Real Dataset" (mis. 3.09 ms vs 0.52 ms baseline). Terekam rapi di `anomaly_log.txt`. Metrik korelasi Spearman valid.
**4. Logic check:** [x] Parameter sesuai plan / [ ] Ada ketidaksesuaian.

**Kesimpulan:** [x] Data siap analisis / [ ] Perlu tindakan.


---

## Refleksi

> Apa perbedaan antara "data yang benar" dan "data yang dipercaya"? Mengapa proses validasi formal diperlukan meskipun data dikumpulkan secara otomatis?

> Data yang benar adalah angka mentah hasil keluaran sistem (log output), namun belum tentu mewakili kondisi wajar karena bisa mengandung error sistemik atau outlier sesaat. Data yang dipercaya adalah data yang telah melalui serangkaian filter validasi sehingga murni merepresentasikan fenomena yang sedang diteliti (bebas bias eksperimen). Validasi formal mutlak diperlukan walau dicatat otomatis karena lingkungan eksekusi (seperti state memori dan background CPU) rentan terhadap anomali yang luput dari skrip logging dasar.
