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

Gap Statement  : Sistem informasi saat ini (seperti SIM dan ERP standar) mayoritas masih bersifat reaktif dan deskriptif, sehingga pengambilan keputusan hanya didasarkan pada data masa lalu tanpa kemampuan prediksi otomatis untuk masa depan.

Research Question:
  Tipe         : [ ] Comparison  [x] Improvement  [ ] Exploratory
  Formulasi    : Apakah integrasi algoritma Machine Learning (seperti Random Forest) untuk prediksi permintaan layanan dapat menghasilkan waktu pengambilan keputusan yang lebih singkat dibandingkan sistem SIM reaktif standar pada operasional organisasi?
  Variabel IV  : Jenis Sistem Informasi (Reaktif standar vs Prediktif berbasis ML)
  Variabel DV  : Kecepatan pengambilan keputusan.
  Metrik       : Waktu pemrosesan keputusan (dalam satuan hari/jam).
  Dataset      : Data historis transaksi dan operasional dari sistem ERP.
  Baseline     : Hasil riset Hafiz & Nasution (2024) yang mencatat kecepatan keputusan 7 hari (peningkatan 50% dari sistem manual).

Quality Check RQ:
  [x] Variabel spesifik
  [x] Metrik jelas
  [x] Baseline ada
  [x] Konteks disebutkan
  [x] Memerlukan eksperimen (bukan hanya survei literatur)

Contribution Statement:
  Apa yang baru diketahui : Sejauh mana model prediktif dapat mengotomatisasi titik keputusan strategis yang sebelumnya dilakukan secara manual oleh manajer.
  Jenis kontribusi        : [x] Improvement  [ ] Comparison  [ ] Novel approach
  Gap yang diisi          : Method Gap (Integrasi AI/ML pada sistem manajemen tradisional).

Hypothesis Pair:
  H₀ : Tidak ada perbedaan signifikan dalam kecepatan pengambilan keputusan antara sistem SIM prediktif berbasis ML dengan sistem SIM reaktif standar.
  H₁ : Sistem SIM prediktif berbasis ML menghasilkan waktu pengambilan keputusan yang secara signifikan lebih singkat dibandingkan sistem SIM reaktif standar.
  Threshold              : 0,5
  Justifikasi threshold  : Ambang batas ini umum digunakan dalam riset sistem informasi untuk meminimalkan risiko kesalahan pengambilan kesimpulan.
```

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:** Sistem saat ini masih reaktif dan hanya mengolah data yang sudah terjadi, belum memiliki fitur prediksi otomatis berbasis AI.

**RQ versi pertama (tulis bebas):**
> Bagaimana pengaruh penggunaan AI untuk membantu manajer mengambil keputusan di perusahaan?.

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| Metode spesifik |YA|Integrasi algoritma prediktif (AI/ML)|
| Metrik terukur |YA|Kecepatan pengambilan keputusan (hari).|
| Baseline |YA|Sistem SIM reaktif standar (Hafiz & Nasution, 2024).|
| Dataset/konteks |YA|Operasional organisasi/perusahaan otobus|

**Tipe RQ:** [ ] Comparison / [x] Improvement / [ ] Exploratory

**RQ versi revisi (setelah evaluasi):**
> Apakah model prediksi berbasis Random Forest dapat mempercepat pengambilan keputusan manajerial hingga di bawah 7 hari pada operasional perusahaan dibandingkan sistem SIM standar?
---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen | Isi |
|----------|-----|
| H₀ | Penggunaan model prediksi Random Forest tidak memberikan percepatan yang signifikan dibandingkan durasi 7 hari pada sistem baseline. |
| H₁ |Penggunaan model prediksi Random Forest secara signifikan mempercepat waktu pengambilan keputusan menjadi kurang dari 7 hari.|
| Metrik |Mean Lead Time (Rata-rata waktu keputusan).|
| Threshold |P-value < 0,05.|
| Justifikasi threshold |Menjamin bahwa percepatan yang ditemukan bukan karena faktor kebetulan.|

**Apakah hipotesis ini falsifiable?** [x] Ya / [ ] Tidak
> Bagaimana cara membuktikannya salah? Jika setelah eksperimen dilakukan, rata-rata waktu keputusan tetap 7 hari atau bahkan lebih lama, maka H₁ ditolak dan riset membuktikan metode prediktif tersebut tidak efektif.
---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| RQ |Apakah sistem prediktif berbasis ML mempercepat keputusan dibandingkan SIM standar?.|
| Variable (IV) |Penggunaan Algoritma Prediktif (ML) vs Deskriptif (SIM standar).|
| Variable (DV) |Durasi waktu pengambilan keputusan.|
| Metric |Satuan waktu (hari).|
| Data source |Log transaksi ERP dan data survei waktu manajerial.|
| Analysis method |T-Test untuk membandingkan rata-rata waktu dua sistem.|

**Apakah rantai lengkap?** [x] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? ______________

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:** Analisis Dampak Implementasi Sistem Informasi Manajemen pada Efisiensi Proses Bisnis.
**RQ yang diekstrak:** Sejauh mana implementasi SIM memengaruhi efisiensi operasional organisasi?.
**Komponen yang hilang:** Kurangnya penyebutan metode spesifik (jenis algoritma atau sistem yang digunakan tidak dirinci secara teknis) dan tidak ada baseline pembanding dari riset lain yang setara di bagian RQ-nya.
