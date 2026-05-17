# WS-02: Problem Statement

> **Bab 2 — Problem Formulation & System Context**

---

## Ringkasan Materi

### Problem Formation Model

Masalah riset melewati 5 tahap transformasi. Melompat langsung dari Reality ke Variable adalah kesalahan paling umum.

```
Reality → Observed Issue (Symptom) → Diagnosed Problem (Root Cause)
→ Researchable Problem (Scoped) → Measurable Variable (Operationalized)
```

### Topic ≠ Problem ≠ Research Problem

| Level | Contoh | Status |
|-------|--------|--------|
| **Topik** | Keamanan IoT | Terlalu luas, tidak bisa diuji |
| **Problem** | MQTT tidak terenkripsi | Spesifik tapi belum riset |
| **Research Problem** | Belum ada studi membandingkan overhead TLS 1.3 vs DTLS pada MQTT di IoT RAM < 64KB | Bisa dirancang eksperimennya |

### Symptom vs Root Cause

Apa yang diamati (gejala) ≠ mengapa terjadi (akar masalah). Gunakan **5 Whys** atau **Fishbone Diagram** untuk menggali.

Contoh: "User meninggalkan checkout" (symptom) → "Waktu loading > 8 detik karena API call sequential" (root cause).

### System Thinking

Setiap masalah riset TI harus terikat pada komponen sistem: **Input → Process → Output → Outcome → Constraints → Stakeholders**.

### Problem Quality Check

Masalah riset yang layak harus memenuhi 5 kriteria:
- **Clarity** — Satu orang membaca akan paham
- **Measurability** — Ada metrik kuantitatif
- **Relevance** — Penting untuk domain
- **Testability** — Bisa gagal (falsifiable)
- **Impact** — Ada kontribusi jika terjawab

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Menyelesaikan masalah (*solve*) | Memahami dan membuktikan (*understand & prove*) |
| Masalah | Bug, error, fitur belum ada | Gap dalam pengetahuan |
| Scope | Selesaikan semua yang perlu | Batasi agar bisa dibuktikan |
| Output | Working system | Evidence, paper, replicable findings |

### Istilah Penting

- **Problem Statement** — Formulasi tertulis: konteks sistem + gap + dampak + justifikasi
- **System Context** — Deskripsi lengkap: input, proses, output, outcome, constraints, stakeholders
- **Problem Drift** — Masalah "bermutasi" dari pendahuluan ke metodologi karena statement awal tidak presisi
- **Solution-First Thinking** — Memulai dari solusi tanpa masalah yang jelas — berbahaya dalam riset
- **Operational Definition** — Definisi variabel yang cukup jelas agar peneliti lain bisa mengukur hal yang sama

---

## Template A.2 — Problem Statement Builder

```
PROBLEM STATEMENT BUILDER

Domain & Konteks
  Domain   : Sistem Transportasi Cerdas (Intelligent Transportation System)
  Konteks  : Pengaturan durasi lampu lalu lintas di persimpangan kota dengan volume kendaraan dinamis

System Context
  Input       : Volume kendaraan tiap arah, waktu siklus lampu, parameter algoritma genetika 
  Process     : Optimasi durasi lampu hijau menggunakan algoritma genetika berdasarkan fungsi fitness
  Output      : Durasi optimal lampu hijau untuk tiap arah
  Outcome     : Pengurangan antrean kendaraan dan waktu tunggu di persimpangan
  Constraints : Batas waktu siklus maksimum, variasi volume kendaraan, keterbatasan komputasi
  Stakeholders: Pengendara, Dinas Perhubungan, pemerintah kota

Fenomena → Problem
  Fenomena yang diamati             : Terjadi kemacetan di persimpangan saat jam sibuk
  Gejala (symptom) yang terukur     : Panjang antrean kendaraan tinggi dan waktu tunggu lama
  Masalah yang didiagnosis          : Pengaturan durasi lampu lalu lintas tidak adaptif terhadap kondisi aktual
  Masalah riset (researchable)      : Bagaimana mengoptimalkan durasi lampu lalu lintas untuk meminimalkan antrean kendaraan?
  Variabel yang terukur             : Volume kendaraan, durasi lampu hijau, total antrean, nilai fitness

Problem Quality Check
  [✔] Clarity — Apakah satu orang membaca akan paham?
  [✔] Measurability — Apakah ada metrik kuantitatif?
  [✔] Relevance — Apakah penting untuk domain?
  [✔] Testability — Apakah bisa gagal?
  [✔] Impact — Apakah ada kontribusi jika terjawab?

Problem Statement (1 paragraf):
  Kemacetan pada persimpangan jalan di area perkotaan sering terjadi akibat pengaturan durasi lampu lalu lintas yang tidak adaptif terhadap volume kendaraan yang dinamis. Hal ini menyebabkan peningkatan panjang antrean dan waktu tunggu kendaraan, terutama pada jam sibuk. Oleh karena itu, diperlukan suatu metode optimasi yang mampu menentukan durasi lampu hijau secara optimal. Penelitian ini bertujuan untuk mengoptimalkan durasi lampu lalu lintas menggunakan algoritma genetika dengan meminimalkan total antrean kendaraan sebagai fungsi fitness, sehingga dapat meningkatkan efisiensi arus lalu lintas di persimpangan.
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Sistem Pendukung Keputusan (DSS) Pendidikan

| Tahap | Hasil |
|-------|-------|
| Reality | Lembaga pendidikan dituntut untuk mengukur dan mengembangkan kompetensi soft skill siswa guna menghadapi dinamika abad ke-21. |
| Observed Issue (Symptom) | Penilaian soft skill di lapangan sering kali bias, tidak konsisten antar-guru, dan tidak memberikan perbedaan tingkat kompetensi yang jelas bagi 140 siswa. |
| Diagnosed Problem (Root Cause) | Evaluasi konvensional hanya bertumpu pada pengamatan kualitatif sesaat dan skala likert sederhana tanpa adanya pembobotan terstruktur untuk kriteria multidimensi. |
| Researchable Problem |Terbatasnya model DSS berbasis MCDM yang mengintegrasikan metode pembobotan hierarkis (AHP) dan pemeringkatan berbasis jarak solusi ideal (TOPSIS) secara komprehensif khusus untuk penilaian soft skill siswa. |
| Measurable Variable | Nilai batas uji konsistensi kriteria (CR ≤ 0.1) dan ketajaman hasil peringkat alternatif berdasarkan parameter kedekatan solusi ideal (C) |

**Apakah terjebak solution-first thinking?** [ ] Ya / [✔] Tidak
> Jika ya, kembali ke tahap mana? ________________________

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Nilai kuesioner penilaian mandiri siswa, lembar observasi guru (skala 1–5), serta matriks penilaian perbandingan kepentingan kriteria oleh 3 pakar (skala Saaty 1–9). |
| Process | Pembentukan hierarki 4 kriteria utama dan 13 indikator, perhitungan bobot prioritas dengan AHP, uji rasio konsistensi (CR), normalisasi matriks keputusan, serta pemeringkatan kedekatan solusi ideal positif dan negatif dengan TOPSIS. |
| Output | Nilai koefisien kedekatan akhir ($C_{ci}$), daftar peringkat urutan siswa, serta hasil pemetaan kategori kompetensi siswa. |
| Outcome | Tersedianya instrumen evaluasi yang objektif dan transparan sebagai dasar analitis bagi guru dalam merancang program pembinaan karakter yang dipersonalisasi. |
| Constraints | Ruang lingkup data terbatas pada satu instusi (MA Mu'allimin Sruweng), sensitivitas tinggi terhadap variasi bobot pakar, dan guru memerlukan pelatihan pemrosesan data berbasis kuantitatif.|
| Stakeholders | Tim manajemen sekolah (Kepala Madrasah, Waka Kurikulum, Guru BK), guru kelas sebagai evaluator lapangan, serta 140 siswa kelas X dan XI. |

**Komponen mana yang paling relevan dengan masalah riset?** Process. Karena inovasi utama dan kebaruan dari riset ini terletak pada integrasi komprehensif algoritma AHP dan TOPSIS dalam memproses struktur kriteria hierarkis penilaian soft skill

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 5 | Rumusan masalah sangat jelas membedakan kelemahan sistem konvensional (subjektif/bias) dengan keunggulan sistem yang diusulkan (sistematis/transparan). |
| Measurability | 5 | Keberhasilan model diukur secara eksak menggunakan parameter matematis baku seperti nilai reliabilitas instrumen PLS-SEM, nilai $CR = 0$ (konsistensi sempurna), dan koefisien preferensi preferensi $C_{ci}$ |
| Relevance | 5 | Menjawab tantangan riil dunia pendidikan modern yang membutuhkan standardisasi instrumen penilaian aspek non-akademik siswa. |
| Testability | 5 | Kebenaran hipotesis model diuji langsung menggunakan data sampel riil 3 siswa dari total 140 responden untuk membuktikan akurasi kalkulasi algoritma. |
| Impact | 4 | Memberikan kontribusi nyata bagi pendidik, namun dampaknya masih terbatas pada skala institusi lokal dan membutuhkan replikasi lebih lanjut untuk skala makro. |

**Skor total:** 24 / 25

**Problem statement versi final (1 paragraf):**
> Proses evaluasi kompetensi soft skill siswa di MA Mu'allimin Sruweng selama ini masih bergantung pada pengamatan subjektif guru tanpa mekanisme pembobotan kriteria multidimensi yang jelas, sehingga hasil penilaian rentan terhadap bias dan inkonsistensi. Keterbatasan model Decision Support System (DSS) yang mampu mengintegrasikan pembobotan kriteria hierarkis dengan mekanisme peringkat alternatif secara transparan memperparah sulitnya mengklasifikasikan tingkat kemampuan siswa secara adil dan terukur. Kondisi ini menyebabkan pendidik tidak memiliki basis data analitis yang andal untuk merancang program pembinaan karakter yang dipersonalisasi. Untuk mengatasi gap tersebut, penelitian ini merancang dan mengimplementasikan model DSS berbasis integrasi metode AHP-TOPSIS guna mentransformasi penilaian kualitatif perilaku siswa menjadi output kuantitatif yang objektif, konsisten, dan reproducible bagi pengambil keputusan di sekolah.
---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Saat melakukan coding, masalahnya itu teknis yaitu bug/error, fokusnya hanya bagaimana cara supaya program dapat jalan. Tapi dalam masalah riset, kita tidak hanya buat program berjalan, tapi harus membuktikan secara ilmiah kenapa masalah itu ada dan seberapa besar pengaruh solusinya (seperti peningkatan efisiensi) berdasarkan data. Riset itu mencari jawaban kenapa dan seberapa efektif, bukan hanya bisa jalan atau tidak.