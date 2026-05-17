# WS-04: Research Question & Hypothesis

> **Bab 4 — Research Question, Contribution & Hypothesis**

---

## Ringkasan Materi

### RQ Bukan Pertanyaan Biasa

Research Question yang baik secara implisit mengandung cetak biru eksperimen: subjek, baseline, metrik, domain, dataset.

| Kualitas | Contoh |
|----------|--------|
| **Buruk** | "Bagaimana pengaruh deep learning terhadap deteksi malware?" |
| **Baik** | "Apakah CNN menghasilkan F1-Score lebih tinggi dari RF pada CIC-MalMem-2022?" |

Perbedaan: RQ yang baik menyebutkan **metode spesifik**, **metrik terukur**, **baseline**, dan **dataset**.

### Tiga Jenis RQ

| Jenis | Pola | Kebutuhan |
|-------|------|-----------|
| **Comparison** | A vs B → mana lebih baik? | ≥ 2 metode, metrik sama |
| **Improvement** | A' vs A → modifikasi lebih baik? | Pre/post, bukti perbaikan |
| **Exploratory** | Faktor X₁...Xₙ → pengaruh terhadap Y? | Multi-variabel, korelasi/regresi |

### Contribution Statement

Tiga jenis kontribusi: **Improvement** (metode terbukti lebih baik), **Comparison** (perbandingan sistematis yang belum ada), **Novel Approach** (pendekatan baru). Kontribusi harus terhubung langsung dengan gap — kontribusi tanpa gap = klaim tanpa justifikasi.

### Hypothesis H₀ / H₁

- **H₀** (Null) = Tidak ada perbedaan signifikan — asumsi default, harus dibuktikan salah
- **H₁** (Alternative) = Ada perbedaan signifikan — diterima hanya jika H₀ ditolak
- Harus **falsifiable**, mengandung **metrik terukur**, dirumuskan **SEBELUM eksperimen**

### Rantai Operasionalisasi

```
RQ → Variable → Metric → Data → Analysis
```

Jika rantai ini tidak lengkap, RQ belum mature. Bi-directional: RQ yang tidak bisa jadi hipotesis testable harus direvisi mundur.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan pertanyaan | Apa yang harus dibangun? | Apa yang harus dibuktikan? |
| Bentuk jawaban | Sistem yang berfungsi | Bukti empiris terukur |
| Sukses diukur oleh | User satisfaction, uptime | Signifikansi statistik, effect size |
| Jika gagal | Debug dan perbaiki | Laporkan, analisis mengapa |

### Istilah Penting

- **Research Question (RQ)** — Pertanyaan spesifik: variabel terukur + metrik + konteks
- **Contribution Statement** — Apa yang diketahui setelah riset selesai yang sebelumnya belum ada
- **H₀ / H₁** — Null vs Alternative Hypothesis
- **Falsifiability** — Kondisi hipotesis ditolak harus bisa didefinisikan sebelum eksperimen
- **Operationalization** — Proses mewujudkan konsep abstrak menjadi variabel terukur

---

## Template A.4 — RQ-Contribution-Hypothesis

```
RQ-CONTRIBUTION-HYPOTHESIS

Gap Statement  : Proses penilaian kompetensi soft skill siswa di sekolah saat ini masih didominasi oleh observasi kualitatif dan deskriptif guru yang rentan terhadap bias subjektivitas dan inkonsistensi antar-penilai karena ketiadaan mekanisme pembobotan kriteria multidimensi yang terstruktur. Di sisi lain, mayoritas penelitian Multi-Criteria Decision Making (MCDM) di dunia pendidikan masih diterapkan secara parsial (hanya pada tahap pembobotan atau pemeringkatan saja), sehingga model hibrida terintegrasi yang dirancang khusus dengan kriteria hierarkis untuk domain soft skill siswa masih sangat terbatas.

Research Question:
  Tipe         : [ ] Comparison  [X] Improvement  [ ] Exploratory
  Formulasi    : Apakah penerapan model Decision Support System (DSS) yang mengintegrasikan metode AHP dan TOPSIS secara komprehensif berdasarkan 13 indikator operasional mampu menghasilkan nilai koefisien kedekatan (closeness coefficient) yang konsisten (CR =< 0.1), transparan, dan bebas dari bias subjektivitas penilai dibandingkan dengan sistem evaluasi konvensional di MA Mu'allimin Sruweng?
  Variabel IV  : Model DSS berbasis integrasi komprehensif metode AHP-TOPSIS dengan struktur kriteria hierarkis.
  Variabel DV  : Nilai Rasio Konsistensi (CR) kriteria dan akurasi diferensiasi peringkat preferensi akhir siswa (Vi).
  Metrik       : Consistency Ratio (CR =< 0.1) dan skor Closeness Coefficient ($0 \le V_i \le 1$).
  Dataset      : Data penilaian kualitatif (skala Likert 1–5) dari sampel 140 siswa kelas X dan XI MA Mu'allimin Sruweng.
  Baseline     : Sistem penilaian konvensional sekolah yang bertumpu pada observasi deskriptif guru tanpa pembobotan kriteria.

Quality Check RQ:
  [X] Variabel spesifik
  [X] Metrik jelas
  [X] Baseline ada
  [X] Konteks disebutkan
  [X] Memerlukan eksperimen (bukan hanya survei literatur)

Contribution Statement:
  Apa yang baru diketahui : Integrasi komprehensif metode AHP dan TOPSIS terbukti efektif mentransformasi parameter penilaian perilaku manusia yang intangible menjadi output kuantitatif terstruktur , di mana kriteria sosial-interpersonal seperti Kolaborasi ($w = 0.421$) dan Komunikasi ($w = 0.263$) divalidasi oleh para pakar sebagai indikator utama dalam mengukur keberhasilan soft skill siswa abad ke-21.
  Jenis kontribusi        : [X] Improvement  [ ] Comparison  [X] Novel approach
  Gap yang diisi          : Menyediakan kerangka evaluasi hibrida baru yang dirancang khusus untuk domain soft skill dengan pengujian validitas instrumen statistik (PLS-SEM) sebelum pemrosesan algoritma keputusan.

Hypothesis Pair:
  H₀ : Penerapan integrasi metode AHP-TOPSIS tidak memberikan perbedaan signifikan dalam menghasilkan pemeringkatan kompetensi soft skill siswa yang konsisten CR > 0.1 dan informatif dibandingkan sistem evaluasi konvensional.
  H₁ : Penerapan integrasi metode AHP-TOPSIS secara signifikan mampu menghasilkan pemeringkatan kompetensi soft skill siswa yang objektif, konsisten (CR =< 0.1), dan transparan dibandingkan sistem evaluasi konvensional.
  Threshold              : Nilai Rasio Konsistensi CR =< 0.1 dan sebaran nilai preferensi akhir Vi ke dalam 4 kategori interval kompetensi yang tegas.
  Justifikasi threshold  : Mengacu pada teori batas toleransi penyimpangan matriks perbandingan berpasangan Saaty (CR =< 0.1) serta batas baku fungsi pembagian solusi ideal positif dan negatif pada algoritma TOPSIS.
```

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:** Terbatasnya penerapan model MCDM komprehensif terintegrasi yang dirancang khusus dengan struktur kriteria hierarkis untuk menilai kompetensi soft skill siswa di sekolah formal.

**RQ versi pertama (tulis bebas):**
> Bagaimana cara membangun sistem komputer menggunakan kombinasi metode AHP dan TOPSIS yang bisa membantu guru-guru menilai nilai soft skill murid secara adil dan tidak pilih kasih?

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| Metode spesifik | YA | Menggunakan integrasi algoritma AHP dan TOPSIS. |
| Metrik terukur | YA | Diukur lewat tingkat konsistensi logika ($CR$) dan ketajaman peringkat ($V_i$). |
| Baseline | YA | Dibandingkan dengan evaluasi konvensional/deskriptif guru. |
| Dataset/konteks | YA | Diuji pada studi kasus 140 siswa kelas X & XI MA Mu'allimin Sruweng. |

**Tipe RQ:** [X] Comparison / [X] Improvement / [ ] Exploratory

**RQ versi revisi (setelah evaluasi):**
> Apakah implementasi model DSS hibrida berbasis integrasi komprehensif AHP-TOPSIS dengan struktur 13 indikator operasional mampu menghasilkan nilai closeness coefficient yang stabil, konsisten secara logis ($CR \le 0.1$), dan bebas bias evaluator dibandingkan sistem penilaian konvensional sekolah?
---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen | Isi |
|----------|-----|
| H₀ | Model DSS berbasis integrasi AHP-TOPSIS tidak menghasilkan nilai rasio konsistensi matriks kriteria yang valid (CR>0.1) serta gagal memberikan diferensiasi peringkat kompetensi siswa yang jelas dibandingkan evaluasi konvensional. |
| H₁ | Model DSS berbasis integrasi AHP-TOPSIS menghasilkan nilai rasio konsistensi matriks kriteria yang konsisten (CR≤0.1) serta memberikan pemisahan peringkat preferensi (Vi) yang tajam untuk memetakan 4 klasifikasi tingkat kompetensi siswa. |
| Metrik | Consistency Ratio (CR) dan Closeness Coefficient (Vi). |
| Threshold | CR≤0.1 dan koefisien akhir alternatif bernilai rentang 0≤Vi≤1. |
| Justifikasi threshold | Aturan baku nilai indeks acak (RI) penentu konsistensi penilaian pakar kriteria dan standarisasi proporsional jarak kedekatan solusi ideal positif/negatif TOPSIS. |

**Apakah hipotesis ini falsifiable?** [X] Ya / [ ] Tidak
> Bagaimana cara membuktikannya salah? Jika setelah pengujian ternyata matriks penilaian pakar menghasilkan CR > 0.1 atau sistem gagal memberikan pemisahan peringkat akhir (Vi) yang lebih tajam dibandingkan penilaian konvensional guru, maka H₁ ditolak.
---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| RQ | Apakah implementasi model DSS hibrida berbasis integrasi komprehensif AHP-TOPSIS dengan struktur 13 indikator operasional mampu menghasilkan nilai closeness coefficient yang konsisten ($CR \le 0.1$) dan bebas bias evaluator dibandingkan sistem penilaian konvensional sekolah? |
| Variable (IV) | Penggunaan model DSS berbasis kombinasi algoritma hibrida AHP dan TOPSIS. |
| Variable (DV) | Tingkat konsistensi matematis pembobotan kriteria dan ketajaman diferensiasi klasifikasi peringkat alternatif siswa. |
| Metric | Nilai indeks konsistensi ($CI$), rasio konsistensi ($CR$), dan nilai preferensi akhir kedekatan solusi ideal ($V_i$). |
| Data source | Kuesioner Penilaian Mandiri Siswa (skala 1-5), lembar Observasi Perilaku Siswa oleh Guru, dan matriks penilaian kepentingan kriteria dari 3 ahli (skala 1-9). |
| Analysis method | Perhitungan rata-rata baris matriks ternormalisasi (Eigenvector) , uji perkalian silang nilai eigen maksimum $\lambda_{max}$ , perkalian vektor bobot AHP ke matriks normalisasi terbobot TOPSIS , dan kalkulasi jarak Euclidean. |

**Apakah rantai lengkap?** [x] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? ______________

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul Jurnal Pendukung yang Dianalisis:** Sistem Pendukung Keputusan untuk Pemilihan Lokasi Usaha di Kota Kupang dengan SMART Method
**RQ yang Diekstrak:** Bagaimana penerapan metode Simple Multi Attribute Rating Technique (SMART) dalam sistem pendukung keputusan berbasis website dapat memberikan urutan rekomendasi alternatif lokasi usaha yang optimal bagi pelaku UMKM di Kota Kupang berdasarkan 5 kriteria spasial-ekonomi?
**Komponen yang Hilang:** RQ pada paper tersebut tidak menyertakan baseline pembanding operasional yang riil (tidak menghadapkan algoritma SMART secara langsung dengan metode MCDM sejenis seperti SAW atau AHP untuk mengukur akurasi perankingan alternatifnya). Selain itu, metrik validitas eksperimennya longgar karena pengujian sistem hanya bertumpu pada fungsionalitas antarmuka (Black box testing) , tanpa melakukan pengujian performa komputasi tingkat lanjut (load testing) atau uji kegunaan nyata (usability testing) oleh para pelaku UMKM selaku pengguna akhir. Rantai operasionalisasinya terputus di tingkat pembuktian keandalan model ketika berhadapan dengan data dinamis real-time.
