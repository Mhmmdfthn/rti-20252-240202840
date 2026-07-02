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
  [ ] Semua skenario tercakup
  [ ] Jumlah run sesuai rencana
  [ ] Tidak ada file output hilang
  Missing: ____ dari ____ data points

Format Consistency:
  [ ] Semua file format sama (CSV/JSON/...)
  [ ] Header konsisten
  [ ] Tipe data konsisten (numerik tetap numerik)

Range & Logic:
  [ ] Nilai dalam range masuk akal
  [ ] Tidak ada waktu negatif
  [ ] Metrik 0–100%, tidak di luar range
  Anomali ditemukan: ____________________

Cross-Validation:
  [ ] Run identik → hasil mendekati
  [ ] Trend konsisten dengan ekspektasi teori

Keputusan:
  [ ] Data siap analisis
  [ ] Perlu cleaning
  [ ] Perlu re-run (skenario: ____)
```

---

## Latihan 1 — Completeness Check

Verifikasi apakah semua data yang direncanakan sudah terkumpul.

| Skenario | Run Direncanakan | Run Tercatat | Missing | Alasan |
|----------|-----------------|-------------|---------|--------|
| Real Dataset (n=140) | 5 | 5 | 0 | — |
| Synthetic Dataset (n=10000) | 5 | 4 | 1 | Memory terpakai penuh (OOM) pada run ke-5 |

**Total expected:** 10 | **Total actual:** 9 | **Missing:** 1

**Keputusan untuk data missing:**
> Data missing (run 5) dibuang sementara. Ditambahkan mitigasi `gc.collect()` antar-run, lalu di-rerun ulang satu iterasi untuk melengkapi kelima run tersebut.

---

## Latihan 2 — Anomaly Investigation

Periksa data Anda untuk anomali. Gunakan metode IQR atau z-score.

**Dataset sampel (atau data Anda sendiri):**

| Run | Runtime (ms) |
|-----|-------------|
| 1 | 17.2 |
| 2 | 17.5 |
| 3 | 17.6 |
| 4 | 55.1 |
| 5 | 17.1 |

**Deteksi outlier:**
- Q1 = 17.15 | Q3 = 17.55 | IQR = 0.4
- Batas bawah (Q1 - 1.5×IQR) = 16.55
- Batas atas (Q3 + 1.5×IQR) = 18.15
- Outlier terdeteksi: Run 4 (55.1)

**Investigasi (untuk setiap outlier):**

| Outlier | Nilai | Kemungkinan Penyebab | Keputusan |
|---------|-------|---------------------|-----------|
| Run 4 | 55.1 | Proses background OS menyela siklus CPU sesaat (CPU interrupt) | Trim outlier, hitung mean dari 4 run normal, atau re-run iterasi ke-4 |

---

## Latihan 3 — Validation Report

Buat laporan validasi ringkas untuk dataset eksperimen Anda.

**1. Completeness:** 100% data terkumpul (setelah re-run data yang missing)
**2. Format:** [x] Konsisten / [ ] Ada inkonsistensi: 
**3. Range check (anomali):** Ditemukan satu outlier ekstrim pada waktu komputasi (Runtime), tapi nilai metrik Spearman Rho valid dalam batas -1 hingga 1.
**4. Logic check:** [x] Parameter sesuai plan / [ ] Ada ketidaksesuaian: 

**Kesimpulan:** [x] Data siap analisis / [ ] Perlu tindakan:

---

## Refleksi

> Apa perbedaan antara "data yang benar" dan "data yang dipercaya"? Mengapa proses validasi formal diperlukan meskipun data dikumpulkan secara otomatis?

> Data yang benar adalah angka mentah hasil keluaran sistem (log output), namun belum tentu mewakili kondisi wajar karena bisa mengandung error sistemik atau outlier sesaat. Data yang dipercaya adalah data yang telah melalui serangkaian filter validasi sehingga murni merepresentasikan fenomena yang sedang diteliti (bebas bias eksperimen). Validasi formal mutlak diperlukan walau dicatat otomatis karena lingkungan eksekusi (seperti state memori dan background CPU) rentan terhadap anomali yang luput dari skrip logging dasar.
