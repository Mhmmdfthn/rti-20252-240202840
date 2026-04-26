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

**Topik awal:** Optimasi Sistem ERP untuk Perusahaan

| Tahap | Hasil |
|-------|-------|
| Reality | Perusahaan masih pakai cara manual (catat di buku/Excel terpisah) |
| Observed Issue (Symptom) | Stok barang sering tidak cocok antara gudang dan laporan. |
| Diagnosed Problem (Root Cause) | Tidak ada sistem pusat (platform terintegrasi) yang menghubungkan divisi gudang dan admin. |
| Researchable Problem | Analisis perbandingan efisiensi kerja manual vs otomatisasi ERP pada bagian gudang. |
| Measurable Variable | Waktu proses input data dan persentase akurasi stok. |

**Apakah terjebak solution-first thinking?** [ ] Ya / [✔] Tidak
> Jika ya, kembali ke tahap mana? ________________________

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Data transaksi harian dan jumlah stok masuk/keluar. |
| Process | Pengolahan data otomatis oleh modul ERP. |
| Output | Informasi stok barang yang terupdate secara real-time. |
| Outcome | Berkurangnya kesalahan hitung dan proses kerja jadi lebih cepat. |
| Constraints | Karyawan butuh waktu buat belajar sistem baru (pelatihan) |
| Stakeholders | Staff gudang dan Manajer Operasional |

**Komponen mana yang paling relevan dengan masalah riset?** _______________

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 5 | Sangat jelas karena membandingkan dua kondisi (manual vs otomatis). |
| Measurability | 5 | Menggunakan angka persen yang mudah diukur secara kuantitatif. |
| Relevance | 5 | Sangat relevan dengan kebutuhan transformasi digital saat ini. |
| Testability | 4 | Bisa diuji, meski butuh akses ke data internal perusahaan. |
| Impact | 5 | Hasilnya bisa jadi panduan buat perusahaan lain yang mau pakai ERP. |

**Skor total:** 24 / 25

**Problem statement versi final (1 paragraf):**
> Sekarang banyak perusahaan masih menghadapi kendala efisiensi operasional karena ketergantungan pada pengolahan data secara manual yang berisiko tinggi terhadap kesalahan manusia (human error) serta kurangnya integrasi antar-departemen. Masalah ini mengakibatkan lambatnya alur kerja dan rendahnya akurasi data yang diperlukan untuk merespons dinamika pasar. Penelitian ini bertujuan untuk menganalisis bagaimana penerapan sistem informasi, seperti Enterprise Resource Planning (ERP), dapat meningkatkan efisiensi operasional di berbagai fungsi bisnis dan menyediakan data real-time untuk mendukung pengambilan keputusan strategis yang lebih cepat dan akurat.
---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Saat melakukan coding, masalahnya itu teknis yaitu bug/error, fokusnya hanya bagaimana cara supaya program dapat jalan. Tapi dalam masalah riset, kita tidak hanya buat program berjalan, tapi harus membuktikan secara ilmiah kenapa masalah itu ada dan seberapa besar pengaruh solusinya (seperti peningkatan efisiensi) berdasarkan data. Riset itu mencari jawaban kenapa dan seberapa efektif, bukan hanya bisa jalan atau tidak.