# WS-12: Result Presentation & Visualization

> **Bab 12 — Penyajian Hasil & Visualisasi**

---

## Ringkasan Materi

### Data → Insight Model

```
Validated Data → Structured Presentation → Visualization → Pattern Recognition → Insight
```

Penyajian **mendahului** analisis. Tabel dan grafik membantu peneliti "melihat" data sebelum menghitung. Langsung ke uji statistik tanpa visualisasi berisiko kesimpulan yang secara teknis benar tapi kontekstual salah (Anscombe's Quartet, 1973).

### Tabel = Presisi, Grafik = Pola

Keduanya **saling melengkapi**:
- Tabel: angka presisi, self-contained (dipahami tanpa teks), sortable
- Grafik: pola visual, tren, perbandingan cepat

### Jenis Grafik Berdasarkan Tujuan

| Tujuan | Jenis Grafik |
|--------|-------------|
| Perbandingan antar-skenario | Bar chart (grouped/stacked) |
| Distribusi per-skenario | Box plot / violin plot |
| Tren temporal | Line chart |
| Korelasi dua variabel | Scatter plot |
| Proporsi (total = 100%) | Pie chart (hati-hati!) |

### Contoh Tabel Hasil yang Baik

| Model | Accuracy (%) | F1-Score (%) | Training Time (min) |
|-------|-------------|-------------|---------------------|
| BERT | 88.4 ± 1.2 | 87.1 ± 1.4 | 45.2 ± 3.1 |
| LSTM | 86.1 ± 1.8 | 84.5 ± 2.0 | 12.8 ± 1.2 |
| SVM | 82.3 ± 0.9 | 80.7 ± 1.1 | 0.3 ± 0.1 |

*N=10 per model. Mean ± std. Diurutkan berdasarkan Accuracy.*

### Visualization Bias — Yang Harus Dihindari

| Bias | Deskripsi | Dampak |
|------|----------|--------|
| Truncated axis | Y tidak dari 0 | Memperbesar perbedaan kecil |
| Inconsistent scale | Dua grafik skala beda | Perbandingan menyesatkan |
| Cherry-picked data | Hanya tampilkan yang "menang" | Selektif, tidak jujur |
| 3D effects | Efek 3D tanpa dimensi data ke-3 | Distorsi tanpa informasi |
| Missing error bar | Tidak ada variabilitas | Menyembunyikan ketidakpastian |

### Engineering vs Research Presentation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan grafik | Dashboard monitoring | Mendukung argumen ilmiah |
| Informasi wajib | KPI, threshold | Mean, std, CI, N, p-value |
| Bias handling | Less critical | Wajib dihindari (peer-review) |

---

## Template A.12 — Result Presentation Plan

```
RESULT PRESENTATION PLAN

Research Question : Bagaimana performa dan sensitivitas algoritma hibrida AHP-TOPSIS dalam mereduksi bias penilaian pada sistem pengambil keputusan jika diuji menggunakan instrumen data multidimensional?
Metrik Utama      : Spearman Rho (Konsistensi Peringkat) & Runtime (Efisiensi)

Tabel Hasil:
| Skenario (Real Dataset) | Spearman Rho (mean) | Runtime ms (mean ± std) | n |
|-------------------------|---------------------|-------------------------|---|
| Baseline (Δw = 0%)      | 1.0000              | 0.36 ± 0.08             | 5 |
| Perturbasi Bobot 10%    | 0.9991              | 2.02 ± 0.47             | 5 |
| Perturbasi Bobot 20%    | 0.9950              | 1.64 ± 0.42             | 5 |
| Perturbasi Bobot 30%    | 0.9889              | 1.91 ± 0.67             | 5 |
| Perturbasi Bobot 40%    | 0.9774              | 2.32 ± 0.47             | 5 |
| Perturbasi Bobot 50%    | 0.9603              | 1.63 ± 0.47             | 5 |

Visualisasi yang Direncanakan:
| # | Jenis Grafik | Pesan Utama | Metrik |
|---|-------------|-------------|--------|
| 1 | Line Chart | Penurunan kestabilan peringkat seiring naiknya persentase perturbasi bobot | Delta W vs Spearman Rho |
| 2 | Line Chart with Error Bars | Fluktuasi runtime dan overhead OS pada pengujian skala kecil (140) | Delta W vs Runtime (ms) |

Bias Check:
  [x] Y-axis mulai dari 0 (atau dijustifikasi)
  [x] Error bar/CI ditampilkan
  [x] Semua data disertakan (tidak cherry-picked)
  [x] Tidak menggunakan 3D tanpa alasan
```

---

## Latihan 1 — Tabel Hasil

Buat tabel hasil eksperimen Anda (boleh dengan data simulasi jika belum punya data riil).

| Skenario (Real Dataset) | Spearman Rho (mean) | Runtime ms (mean ± std) | n |
|-------------------------|---------------------|-------------------------|---|
| Baseline (Δw = 0%)      | 1.0000              | 0.36 ± 0.08             | 5 |
| Perturbasi Bobot 10%    | 0.9991              | 2.02 ± 0.47             | 5 |
| Perturbasi Bobot 20%    | 0.9950              | 1.64 ± 0.42             | 5 |
| Perturbasi Bobot 30%    | 0.9889              | 1.91 ± 0.67             | 5 |
| Perturbasi Bobot 40%    | 0.9774              | 2.32 ± 0.47             | 5 |
| Perturbasi Bobot 50%    | 0.9603              | 1.63 ± 0.47             | 5 |

**Checklist tabel:**
- [x] Self-contained (judul jelas, satuan ada, N tercantum)
- [x] Mean ± std (bukan single number)
- [x] Diurutkan berdasarkan metrik utama
- [x] Format konsisten di semua baris

---

## Latihan 2 — Rencana Visualisasi

Rencanakan 2-3 grafik untuk menyajikan data dari Latihan 1. Setiap grafik = satu pesan.

| # | Jenis Grafik | Pesan | Data yang Digunakan |
|---|-------------|-------|---------------------|
| 1 | Line Chart | Penurunan nilai Spearman Rho seiring peningkatan persentase perturbasi bobot (konsistensi global) | Tingkat perturbasi / Delta W (sumbu-X) vs Spearman Rho (sumbu-Y) |
| 2 | Line Chart | Penurunan nilai Kendall's Tau seiring peningkatan persentase perturbasi bobot (stabilitas rank inversions) | Tingkat perturbasi / Delta W (sumbu-X) vs Kendall's Tau (sumbu-Y) |
| 3 | Line Chart / Scatter Plot | Analisis kinerja komputasi dan observasi anomali runtime pada dataset riil vs sintetis | Tingkat perturbasi / Delta W (sumbu-X) vs Runtime dalam ms (sumbu-Y) |

---

## Latihan 3 — Bias Detection

Evaluasi visualisasi berikut untuk bias (skenario dari contoh):

**Skenario:** Metode A = 91.2%, Metode B = 90.8%. Bar chart dengan Y-axis mulai dari 90%.

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah error bar ditampilkan? | Tidak, variabilitas hasil antar iterasi tidak terlihat sehingga signifikansi perbedaan 0.4% tidak bisa dinilai. |
| Apakah semua kondisi ditampilkan? | Tidak jelas, bisa jadi ada hasil run yang dihilangkan (cherry-picking). |
| Apa solusinya? | Ubah rentang Y-axis (misal dari 0 atau rentang yang lebih proporsional) dan tambahkan error bars. |

**Evaluasi grafik Anda sendiri dari Latihan 2:**
- [x] Semua bias check lulus
- [ ] Ada yang perlu diperbaiki:

---

## Refleksi

> Mengapa tabel dan grafik keduanya diperlukan — tidak cukup salah satu saja? Pernahkah Anda membuat grafik yang (tanpa sengaja) menyesatkan?

> Tabel dan grafik memiliki peran yang saling melengkapi (komplementer). **Tabel** mutlak diperlukan untuk menyajikan nilai numerik presisi tinggi (beserta standar deviasi) agar hasil eksperimen bisa direproduksi dan diverifikasi oleh peneliti lain secara spesifik. Di sisi lain, **Grafik** sangat krusial untuk menangkap "pola global", tren, atau persebaran data (seperti laju degradasi metrik saat parameter naik) yang sangat sulit dikenali jika hanya memandangi deretan angka di tabel. Menggunakan keduanya memastikan pembaca mendapatkan *insight* kualitatif sekaligus bukti kuantitatif.
> Mengenai pembuatan grafik yang menyesatkan, di masa lalu hal ini sering terjadi tanpa disengaja saat kita memotong rentang sumbu-Y (memulainya bukan dari 0) hanya agar garis tren terlihat fluktuatif/dramatis. Selain itu, lupa menyertakan *error bars* juga pernah terjadi, yang mana hal itu justru menyembunyikan variabilitas data dan bisa memanipulasi pembaca untuk mempercayai suatu klaim keberhasilan yang sebenarnya belum terbukti konklusif.
