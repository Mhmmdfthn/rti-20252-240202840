# WS-10: Experiment Execution & Data Collection

> **Bab 10 — Eksekusi Eksperimen & Pengumpulan Data**

---

## Ringkasan Materi

### Experiment Execution Pipeline

```
Design → Execution Plan → Controlled Execution → Data Collection → Data Logging → Dataset for Analysis
```

### Multiple Run = Non-Negotiable

Single run **tidak pernah cukup** untuk klaim ilmiah. Minimum 5-10 run per skenario dengan seed berbeda. Multiple run menghasilkan:
- Mean, std, confidence interval
- Distribusi hasil → uji statistik
- Variabilitas → error bar di grafik

### Execution Plan

Setiap eksperimen harus memiliki plan sebelum eksekusi:
- Daftar skenario
- Jumlah run per skenario
- Random seed per run (pre-determined!)
- Urutan eksekusi (randomisasi/counterbalancing)
- Pre-execution checklist

### Data Logging Komprehensif

Setiap run menghasilkan log terstruktur:
1. **Identitas** — Run ID, timestamp, skenario
2. **Konfigurasi** — Semua parameter, seed, code version
3. **Hasil** — Semua metrik, output detail
4. **Metadata** — Waktu eksekusi, resource usage, warning/error

Format: CSV/JSON/database — **bukan stdout yang di-copy-paste**.

### Engineering vs Research Execution

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Run | Sekali (deploy) | Multiple (min 5-10, seed berbeda) |
| Logging | Error log, access log | Semua parameter, metrik, metadata |
| Anomali | Bug → fix → redeploy | Investigasi → dokumentasi → analisis |
| Urutan | Tidak penting | Bisa bias — perlu randomisasi |

### Anomali = Dokumentasi, Bukan Hapus

Run gagal/anomali tidak boleh dihapus tanpa dokumentasi. Bisa jadi:
- **Bug** → fix & re-run (dokumentasikan!)
- **Batas kemampuan metode** → DNF = temuan
- **Data yang bias** jika hanya simpan run "berhasil"

### Jebakan Kognitif

1. "Satu angka cukup" → tanpa distribusi, tidak bisa diuji
2. "Seed tidak penting" → bahkan algoritma deterministik bisa dipengaruhi library stokastik
3. "Run gagal langsung hapus" → kehilangan temuan potensial
4. "Semua run harus hari ini" → thermal throttling, fatigue

---

## Template A.10 — Execution Plan & Data Log

```
EXECUTION PLAN

| Run # | Skenario | Seed | Parameter | Status | Waktu | Output File |
|-------|----------|------|-----------|--------|-------|-------------|
| 1     |          |      |           |        |       |             |
| 2     |          |      |           |        |       |             |
| 3     |          |      |           |        |       |             |
| ...   |          |      |           |        |       |             |

Jumlah runs per skenario : ____
Total runs               : ____

DATA LOG (per run):
  Run ID    : ____________________
  Timestamp : ____________________
  Skenario  : ____________________
  Input     : ____________________
  Output    : ____________________
  Anomali   : ____________________
  Catatan   : ____________________
```

---

## Latihan 1 — Execution Plan

Susun execution plan untuk eksperimen Anda. Tentukan skenario, jumlah run, dan seed sebelum eksekusi.

| Run # | Skenario | Seed | Parameter Kunci | Status |
|-------|----------|------|----------------|--------|
| 1 | Real Dataset | 42 | n=140, delta=0-50% | Planned |
| 2 | Real Dataset | 123 | n=140, delta=0-50% | Planned |
| 3 | Real Dataset | 456 | n=140, delta=0-50% | Planned |
| 4 | Real Dataset | 789 | n=140, delta=0-50% | Planned |
| 5 | Real Dataset | 1001 | n=140, delta=0-50% | Planned |
| 6 | Synthetic Dataset | 42 | n=10000, delta=0-50% | Planned |
| 7 | Synthetic Dataset | 123 | n=10000, delta=0-50% | Planned |
| 8 | Synthetic Dataset | 456 | n=10000, delta=0-50% | Planned |
| 9 | Synthetic Dataset | 789 | n=10000, delta=0-50% | Planned |
| 10 | Synthetic Dataset | 1001 | n=10000, delta=0-50% | Planned |

**Total skenario:** 2 (Real & Synthetic)
**Run per skenario:** 5
**Total run keseluruhan:** 10

---

## Latihan 2 — Data Log Terstruktur

Desain format data log untuk eksperimen Anda. Tentukan field apa saja yang akan dicatat.

**Identitas:**
| Field | Contoh |
|-------|--------|
| Run ID | run-synthetic-001 |
| Timestamp | 2026-06-27T10:30:00 |
| Skenario | Synthetic Dataset |

**Konfigurasi:**
| Field | Contoh |
|-------|--------|
| Seed | 42 |
| Code version | commit abc1234 |
| Dataset Size | 10000 |
| Delta Range | 0-50%, step 10% |

**Hasil:**
| Metrik | Tipe Data | Range Valid |
|--------|----------|-------------|
| Spearman Rho | float | -1.0 – 1.0 |
| Runtime (ms) | float | > 0.0 |
| Reversal Detected | boolean | True/False |

**Format output:** [x] CSV / [x] JSONL / [ ] Database / [ ] Lainnya: ____

---

## Latihan 3 — Anomaly Protocol

Rencanakan bagaimana menangani anomali. Untuk setiap jenis, tentukan langkah yang diambil.

| Jenis Anomali | Contoh | Tindakan |
|---------------|--------|----------|
| Run gagal (crash) | Out of Memory (OOM) pada n=100000 | Dokumentasi batasan memori, kurangi ukuran dataset menjadi 50000, lalu re-run |
| Hasil ekstrem | Nilai Spearman Rho anjlok ke 0.1 | Investigasi distribusi data matriks awal, periksa apakah terjadi pembagian dengan nol saat normalisasi |
| Waktu eksekusi anomali | Runtime tiba-tiba melonjak 5x lipat pada run tertentu | Cek CPU throttling atau proses latar OS, singkirkan outlier (trim), re-run uji waktu |
| Inkonsistensi dengan run lain | Algoritma sangat sensitif/berubah jauh saat ganti seed | Catat temuan, tingkatkan jumlah sampel simulasi (n runs) untuk mendapatkan nilai ekspektasi yang representatif |

**Prinsip:** Detect → Investigate → Document → Decide

---

## Refleksi

> Pernahkah Anda melaporkan hasil riset/tugas dari single run? Apa risikonya? Bagaimana multiple run mengubah kepercayaan terhadap hasil?

**Pengalaman sebelumnya:**
> Biasanya hanya menjalankan eksperimen satu kali saja dan langsung menggunakan waktu komputasi (execution time) dari run tersebut sebagai kesimpulan akhir, tanpa menyadari fluktuasi akibat proses background OS.
**Yang akan dilakukan berbeda:**
> Menjalankan multiple run (minimal 5-10 kali dengan pengaturan random seed yang berbeda) lalu mengambil nilai rata-rata serta mengukur deviasi standar dari waktu komputasi, agar kesimpulan ilmiah lebih kokoh dan stabil terhadap anomali lingkungan.

