# WS-14: Analysis, Interpretation & Failure Analysis

> **Bab 14 — Analisis Data, Interpretasi & Failure Analysis**

---

## Ringkasan Materi

### Data → Knowledge Model

```
Data → Analysis → Interpretation → Explanation → Knowledge
```

Tiga level yang berbeda:
- **Analysis** — "Apa yang terjadi?" (deskriptif + inferensial)
- **Interpretation** — "Apa artinya?" (konteks RQ + literatur)
- **Failure Analysis** — "Mengapa tidak berhasil?" (boundary conditions)

### Beyond p-value

**Statistical significance ≠ practical significance.** Selalu laporkan:
1. p-value (signifikansi statistik)
2. Effect size (besarnya efek)
3. Confidence interval (rentang ketidakpastian)

| Effect Size (Cohen's d) | Interpretasi |
|-------------------------|-------------|
| < 0.2 | Small |
| 0.2 – 0.8 | Medium |
| > 0.8 | Large |

### Pemilihan Uji Statistik

| Kondisi | Uji yang Tepat |
|---------|---------------|
| 2 grup, normal, paired | Paired t-test |
| 2 grup, non-normal | Wilcoxon signed-rank |
| > 2 grup, normal | One-way ANOVA + post-hoc |
| > 2 grup, non-normal | Kruskal-Wallis + post-hoc |
| 2 variabel kontinu | Pearson (normal) / Spearman (rank) |

### Failure Analysis as Contribution

Hipotesis yang ditolak adalah **temuan yang berharga**:

| Dataset | New (F1) | Baseline (F1) | p-value | Cohen's d |
|---------|---------|--------------|---------|-----------|
| DS-1 (small, clean) | 94.2±1.1 | 89.3±1.5 | <0.001 | **3.7** |
| DS-4 (medium, noisy) | 78.3±3.2 | 82.1±2.8 | 0.008 | **-1.3** |
| DS-5 (large, noisy) | 71.6±4.1 | 80.5±3.0 | <0.001 | **-2.5** |

**Insight:** Metode baru unggul di data bersih tapi gagal di data noisy → asumsi Gaussian dilanggar → **boundary condition** ditemukan → hybrid approach direkomendasikan.

**Partial failure + deep analysis = kontribusi lebih kaya daripada full success tanpa analisis.**

### Limitation Types

| Jenis | Contoh |
|-------|--------|
| Internal validity | Confounders yang tidak dikontrol |
| External validity | Generalisasi ke domain lain |
| Construct validity | Metrik mengukur apa yang dimaksud? |
| Statistical limitation | Sample size, asumsi distribusi |

### Jebakan Kognitif

1. "Signifikan statistik = penting secara praktis" → cek effect size
2. "Hipotesis tidak didukung → cari sudut baru" → p-hacking
3. "Kegagalan tidak perlu dilaporkan detail" → missed insight
4. "Limitasi cukup disebutkan, tidak perlu dianalisis" → kedalaman hilang

---

## Template A.14 — Analysis & Interpretation Report

```
ANALYSIS & INTERPRETATION

1. Statistik Deskriptif:
   | Skenario | Mean | Std | Median | Min | Max | n |
   |----------|------|-----|--------|-----|-----|---|
   |          |      |     |        |     |     |   |

2. Uji Hipotesis:
   Uji yang digunakan  : ____________________
   Justifikasi          : ____________________
   Hasil: p = ____, effect size (d/r/η²) = ____
   CI 95%               : [____, ____]

3. Keputusan:
   [ ] H₀ ditolak → H₁ diterima
   [ ] H₀ tidak ditolak

4. Interpretasi:
   Hubungan ke RQ       : ____________________
   Practical significance: ____________________
   Perbandingan literatur: ____________________

5. Limitation:
   | Jenis | Ancaman | Dampak | Mitigasi |
   |-------|---------|--------|----------|
   |       |         |        |          |

6. Failure Analysis (jika H₀ tidak ditolak):
   Penyebab potensial  : ____________________
   Boundary condition   : ____________________
   Insight              : ____________________
```

---

## Latihan 1 — Pemilihan Uji Statistik

Tentukan uji statistik yang tepat untuk eksperimen Anda.

| Pertanyaan | Jawaban |
|-----------|---------|
| Berapa grup yang dibandingkan? | 6 skenario (Baseline, Perturbasi 10%, 20%, 30%, 40%, 50%) |
| Apakah data berpasangan (paired)? | Tidak, setiap run pengujian perturbasi berjalan independen |
| Apakah distribusi normal? (uji normalitas) | Dengan sampel kecil (n=5 per grup), data diasumsikan tidak normal |
| **Uji yang dipilih:** | Uji Kruskal-Wallis (non-parametrik) |
| **Justifikasi:** | Membandingkan lebih dari 2 grup sampel independen dengan asumsi distribusi data tidak normal akibat N yang sangat kecil |

**Effect size yang akan dilaporkan:** [ ] Cohen's d / [x] Eta-squared / [ ] Lainnya: Epsilon-squared

---

## Latihan 2 — Interpretasi Hasil

Gunakan data berikut (atau data riil Anda) untuk berlatih interpretasi.

**Data (Riil: Analisis Waktu Komputasi):**
| Skenario | Runtime ms (mean ± std) | n |
|-------|----------------------|---|
| Perturbasi 10% | 2.02 ± 0.47 | 5 |
| Baseline (Δw = 0%) | 0.36 ± 0.08 | 5 |

p = 0.008, Cohen's d = 4.89, CI 95% = [0.85, 2.47] *(Asumsi uji-t Welch)*

| Aspek | Interpretasi |
|-------|-------------|
| Signifikansi statistik | p < 0.01 → Terdapat perbedaan waktu komputasi yang signifikan secara statistik antara Baseline dan saat diberi perturbasi. |
| Effect size | d = 4.89 → Effect size sangat besar (large effect). Gangguan perturbasi bobot memberikan lonjakan waktu eksekusi yang nyata. |
| Practical significance | Secara teknis terdapat perlambatan 1.66 ms, namun secara praktis kenaikan ini sangat insignifikan untuk interaksi manusia. DSS tetap terasa instan. |
| Hubungan ke RQ | Menjawab RQ mengenai konsistensi sistem: Implementasi AHP-TOPSIS komprehensif tetap sangat efisien meskipun model dipaksa menghitung ulang perturbasi berulang kali. |
| Perbandingan literatur | Konsisten dengan temuan studi MCDM lainnya bahwa algoritma matriks terpadu sangat ringan secara komputasi pada N berskala kecil-menengah (<500 entitas). |

---

## Latihan 3 — Failure Analysis

Latih kemampuan failure analysis: hipotesis TIDAK didukung. Apa yang bisa dipelajari?

**Skenario (Kasus Alternatif):** Saat diuji ke 10.000 simulasi data siswa, metode DSS AHP-TOPSIS Anda membutuhkan waktu komputasi rata-rata 14,2 detik dibandingkan 2,1 detik pada sistem baseline konvensional. Kecepatan memburuk dan p = 0.12 (tidak ada perbedaan akurasi yang signifikan dengan sistem biasa).

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah ini "gagal"? | Bukan gagal total. Tidak terbuktinya signifikansi akurasi dengan trade-off waktu lambat adalah temuan valid mengenai kapasitas sistem dan bottleneck komputasional. |
| Kemungkinan penyebab? | Proses normalisasi matriks 13 indikator pada TOPSIS ditambah perhitungan CR dari AHP sangat membebani RAM jika tidak menggunakan batch processing. |
| Boundary condition? | Model AHP-TOPSIS yang diusulkan hanya berjalan secara optimal dan stabil pada dataset institusi berukuran kecil (< 1.000 record). |
| Insight yang bisa diambil? | Ada trade-off tajam antara kompleksitas hierarki kriteria dan waktu komputasi skala besar. Disarankan untuk menggunakan arsitektur caching perhitungan eigen AHP. |
| Apakah layak dilaporkan? Mengapa? | Ya — temuan batas kapasitas (boundary condition) sangat berguna agar sistem ini tidak diadopsi buta-buta oleh sekolah ber-volume tinggi tanpa persiapan server yang kuat. |

**Limitation terkait:**
| Jenis | Ancaman | Dampak |
|-------|---------|--------|
| External validity | Pengujian hanya dilakukan pada 140 dataset sampel siswa. | Kinerja dan ketajaman peringkat (Vi) belum teruji stabil di skala ribuan siswa (big data). |
| Statistical limitation | Hanya dilakukan uji coba sampel n=5 iterasi. | Low statistical power; variansi data pada hasil waktu komputasi mungkin tidak cukup mewakili kestabilan. |

---

## Refleksi

> Apakah "failure" dalam riset benar-benar gagal, atau justru kontribusi? Bagaimana failure analysis mengubah cara Anda melihat hasil negatif?

> "Failure" dalam riset bukanlah sebuah kegagalan total, melainkan bentuk batas (boundary condition) dari suatu algoritma atau gagasan. Mengetahui kelemahan model —seperti saat AHP-TOPSIS kehilangan kestabilan di volume data raksasa— adalah kontribusi ilmiah yang penting. Pendekatan failure analysis mengubah pandangan saya: bahwa penolakan atas hipotesis alternatif (H1) tetap membawa *insight* yang tajam. Dengan menganalisis kegagalan, kita mencegah redundansi eksperimen bagi peneliti selanjutnya, melengkapi dokumentasi dengan batasan terukur, dan menyediakan pijakan argumen empiris untuk perbaikan (future work). Lapisan analisis sedalam ini justru lebih berharga daripada memaksakan klaim sukses dengan metode p-hacking.
