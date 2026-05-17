# WS-06: System-Experiment Mapping

> **Bab 6 — System Design sebagai Experimental Artifact**

---

## Ringkasan Materi

### Sistem = Instrumen Pengujian, Bukan Produk

Seorang engineer bertanya "apakah sistem bekerja?" — seorang peneliti bertanya "apa yang bisa dibuktikan sistem ini?" Sistem dalam riset adalah **artifact** — objek yang sengaja dibuat untuk menguji klaim spesifik.

### System as Experiment Model

```
RQ → Variable → System Component → Experimental Setup → Output
```

Setiap komponen sistem harus bisa ditelusuri ke variabel riset (top-down), dan setiap pengukuran harus menjawab RQ (bottom-up).

### Mapping Variabel ke Komponen

| Tipe Variabel | Peran di Sistem | Contoh |
|---------------|----------------|--------|
| **IV** (Independent) | Modul yang bisa di-toggle/swap | Algoritma A vs B |
| **DV** (Dependent) | Modul pengukuran | Logger, metrics collector |
| **CV** (Control) | Config yang dikunci | Dataset, parameter tetap |

Jika variabel tidak bisa di-map ke komponen apapun → arsitektur perlu didesain ulang.

### 4 Prinsip Desain Eksperimental

| Prinsip | Pertanyaan Kunci |
|---------|-----------------|
| **Traceability** | Komponen ini melayani variabel yang mana? |
| **Modularity** | Bisakah IV diubah tanpa memengaruhi yang lain? |
| **Controllability** | Apakah CV dieksternalisasi ke config file? |
| **Measurability** | Apakah sistem otomatis menghasilkan data yang dibutuhkan? |

### Variable Isolation melalui Arsitektur

- **Modular architecture** — Pisahkan berdasarkan variabel
- **Configuration-driven** — Ubah config (YAML/JSON), bukan code
- **Feature toggles** — On/off flag untuk ablation study

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan sistem | Memenuhi kebutuhan user | Menguji hipotesis, menghasilkan bukti |
| Arsitektur | Optimasi performa & skalabilitas | Optimasi isolasi variabel & reprodusibilitas |
| Konfigurasi | Sering hardcoded | Dieksternalisasi ke config file |
| Fitur tambahan | Menambah nilai user | Menambah noise jika tidak terkait RQ |

### Istilah Penting

- **Artifact** — Objek yang sengaja dibuat untuk memecahkan masalah atau menguji proposisi
- **Traceability** — Kemampuan menelusuri hubungan RQ → variabel → komponen → output
- **Variable Isolation** — Mengubah hanya satu variabel sambil menahan yang lain konstan
- **Ablation Study** — Menguji kontribusi tiap komponen dengan melepasnya satu per satu
- **Configuration-driven Execution** — Semua parameter di config file, bukan hardcoded

---

## Template A.6 — Mapping RQ ke Arsitektur Sistem

```
SYSTEM-EXPERIMENT MAPPING

**Research Question**: Bagaimana performa dan sensitivitas algoritma hibrida AHP-TOPSIS dalam mereduksi bias penilaian pada sistem pengambil keputusan jika diuji menggunakan instrumen data multidimensional?

Variable → Component Mapping:

| Variabel | Tipe | Komponen Sistem | Cara Manipulasi/Pengukuran |
|----------|------|-----------------|---------------------------|
| Pergeseran Bobot Kriteria  | IV | Perturbation Generator Module (Modul Simulator Gangguan) | Mengubah nilai bobot kriteria secara bertahap  melalui pengulangan skrip otomatis (automated loop script). |
| Stabilitas Peringkat Akhir  | DV | Rank Spearman Evaluator Module (Modul Pengukur Korelasi Urutan) | Menghitung koefisien korelasi urutan alternatif antara matriks sebelum intervensi gangguan dengan setelah intervensi gangguan. |
| Efisiensi Komputasi | DV | Execution Time Benchmarker (Modul Logger Waktu) | Menyisipkan fungsi pewaktu (timestamp function) presisi tinggi sesaat sebelum dan sesudah fungsi kalkulasi keputusan dieksekusi. |
| Dimensi Matriks Keputusan | CV | Core Data Loader Module (Modul Pengunci Data) | Mengunci parameter dataset input pada database secara statis berukuran 140 alternatif siswa 13 indikator kriteria. |

4 Prinsip Desain:
  [X] Traceability — Setiap komponen kode uji dapat ditelusuri fungsinya secara langsung untuk melayani variabel independen, dependen, maupun kontrol.
  [X] Variable Isolation — Perubahan nilai variabel independen (bobot) dapat dilakukan secara terisolasi tanpa memengaruhi integritas data dasar (variabel kontrol).
  [X] Measurement Integration — Pengukuran koefisien korelasi dan waktu eksekusi telah terintegrasi secara otomatis di dalam pipa pemrosesan data (data pipeline).
  [X] Reproducibility — Seluruh skenario pengujian dikendalikan oleh konfigurasi terpusat sehingga dapat direkonstruksi kapan saja dengan hasil yang identik.

Experimental Setup:
  Input data     : Berkas dataset terstruktur format CSV berisi matriks nilai kualitatif 140 siswa dan nilai perbandingan berpasangan dari 3 pakar.
  Parameter      : Rentang gangguan bobot = [-50%, -40%, +50%], langkah inkremental = 10%, random seed = 42.
  Output format  : Berkas log JSON otomatis yang merangkum nilai intervensi delta bobot, nilai akhir koefisien , dan durasi waktu eksekusi dalam milidetik (ms).
```
---

## Latihan 1 — Variable-to-Component Mapping

Gunakan RQ dan variabel dari WS-05. Petakan ke komponen sistem.

**RQ:** Bagaimana performa dan sensitivitas algoritma hibrida AHP-TOPSIS dalam mereduksi bias penilaian pada sistem pengambil keputusan jika diuji menggunakan instrumen data multidimensional?

| Variabel | Tipe | Komponen Sistem | Cara Manipulasi / Pengukuran |
|----------|------|-----------------|---------------------------|
| Pergeseran Bobot ($\Delta w$) | IV | Perturbation Simulator | Mengubah konfigurasi nilai deviasi bobot pada file experiment_config.json. |
| Stabilitas Peringkat ($\rho$) | DV | Spearman Calculator | Menghitung pergeseran indeks urutan array 140 alternatif pasca-simulasi gangguan. |
| Efisiensi Sistem | DV | Execution Benchmarker | Mencatat selisih waktu sistem dalam milidetik menggunakan fungsi microtime(). |
| Volume Matriks Data | CV | Database Core Connector | Membatasi skrip kueri SQL agar hanya mengambil dataset statis berukuran $140 \times 13$. |

**Apakah semua variabel bisa di-map?** [X] Ya / [ ] Tidak
> Jika tidak, komponen apa yang perlu ditambahkan? _________

---

## Latihan 2 — 4 Prinsip Desain

Evaluasi desain sistem terhadap 4 prinsip.

| Prinsip | Status | Bukti / Penjelasan |
|---------|--------|-------------------|
| Traceability | ✅ Telah Dipenuhi | Struktur direktori memisahkan dengan tegas antara /core_algorithm (AHP-TOPSIS) dengan /experiment_runner (simulator dan evaluator metrik). |
| Modularity | ✅ Telah Dipenuhi | Fungsi normalisasi matriks dan fungsi komputasi jarak solusi ideal dibuat sebagai fungsi independen (decoupled) sehingga tidak saling mengunci. |
| Controllability | ✅ Telah Dipenuhi | Batas deviasi gangguan dan ukuran dataset tidak ditulis secara hardcoded, melainkan dikontrol penuh via file konfigurasi eksternal. |
| Measurability | ✅ Telah Dipenuhi | Sistem secara otomatis menulis metrik hasil ukur langsung ke dalam file log setiap kali iterasi loop eksperimen selesai berjalan. |

**Prinsip mana yang paling sulit dipenuhi?** Controllability pada aspek efisiensi komputasi (waktu eksekusi).
**Strategi untuk mengatasinya:**
> Mengeliminasi faktor pengganggu eksternal dengan cara menjalankan skrip pengujian murni melalui Command Line Interface (CLI) pada kondisi sistem operasi yang terisolasi (isolated local environment), serta mematikan seluruh aplikasi latar belakang (background services) non-esensial untuk menjaga konsistensi performa CPU.

---

## Latihan 3 — Ablation Study Planning

Sistem eksperimen memiliki 3 komponen utama:
Komponen A: Modul Pembobotan Hierarkis AHP (jika dilepas, diganti dengan Equal Weighting / pembobotan rata).
Komponen B: Modul Solusi Ideal Ganda TOPSIS (jika dilepas, hanya menghitung jarak terhadap Solusi Ideal Positif saja).
Komponen C: Modul Normalisasi Vektor Matriks (jika dilepas, diganti dengan Normalisasi Linear sederhana).

| Kondisi | Komponen A | Komponen B | Komponen C | Hasil yang Diharapkan |
|---------|-----------|-----------|-----------|----------------------|
| Full | ✅ AHP | ✅ Jarak Ganda | ✅ Normalisasi Vektor | Stabilitas peringkat maksimal ($\rho \ge 0.95$) dan pembagian 4 klasifikasi kompetensi tajam. |
| – A | ❌ (Equal Weight) | ✅ | ✅ | Nilai $\rho$ jatuh drastis saat terjadi gangguan kecil, karena sistem kehilangan sensitivitas kepentingan kriteria. |
| – B | ✅ | ❌ (Jarak Positif Saja) | ✅ | Terjadi anomali fenomena pembalikan peringkat (rank reversal) pada alternatif yang memiliki nilai tengah. |
| – C | ✅ | ✅ | ❌ (Linear Norm) | Kecepatan eksekusi meningkat sedikit, namun akurasi penentuan peringkat menurun pada data ekstrim (outlier). |

**Komponen mana yang diprediksi paling berkontribusi?** Komponen A (Modul Pembobotan Hierarkis AHP).
**Mengapa?**
> Karena pembobotan AHP bertindak sebagai filter utama yang memberikan nilai bobot prioritas logis berdasarkan perspektif pakar. Jika komponen ini dilepas dan diganti dengan pembobotan rata (equal weight), sistem akan menganggap semua indikator memiliki derajat kepentingan yang sama. Akibatnya, sistem menjadi sangat sensitif dan tidak stabil terhadap gangguan kecil pada kriteria non-esensial, yang pada akhirnya merusak validitas keputusan akhir.

---

## Refleksi

> Apa risiko jika sistem dibangun seperti produk (monolitik, fitur lengkap) lalu baru dilakukan eksperimen? Mengapa arsitektur modular penting untuk riset?

**Jawaban:**
> Sistem monolitik berisiko menimbulkan kebutaan analitis (*analytical blindness*), di mana peneliti tidak bisa mengisolasi komponen penyebab anomali karena fungsinya yang saling terikat (*tightly coupled*).
> Sebaliknya, arsitektur modular wajib digunakan karena bertindak sebagai instrumen isolasi variabel. Pemisahan modul memungkinkan manipulasi variabel independen secara presisi (misal: *ablation study*) tanpa merusak sistem lain, menjamin pengujian yang objektif, valid, dan *reproducible*.
