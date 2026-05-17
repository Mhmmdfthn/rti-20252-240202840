# WS-07: Experimental Design & Validity

> **Bab 7 — Experimental Design & Validity**

---

## Ringkasan Materi

### Correlation ≠ Causality

Kausalitas membutuhkan 3 syarat:
1. **Covariance** — X dan Y bergerak bersama
2. **Temporal precedence** — X berubah sebelum Y
3. **Elimination of alternatives** — Tidak ada faktor lain yang menjelaskan Y

Controlled experiment adalah satu-satunya metode yang bisa membuktikan kausalitas.

### Empat Jenis Validitas

| Jenis | Pertanyaan | Ancaman Umum |
|-------|-----------|-------------|
| **Internal** | Apakah hubungan IV→DV nyata? | Confounding variable, selection bias |
| **External** | Apakah bisa digeneralisasi? | Dataset terlalu spesifik |
| **Construct** | Apakah mengukur konsep yang benar? | Metrik tidak sesuai |
| **Conclusion** | Apakah kesimpulan statistik valid? | Sample size kecil, uji salah |

Internal dan external validity sering berkonflik: semakin terkontrol (internal kuat) → semakin artificial (external lemah).

### Tiga Tipe Eksperimen dalam Riset TI

| Tipe | Deskripsi | Kapan Digunakan |
|------|----------|----------------|
| **Comparison Study** | Metode A vs B pada kondisi identik | Membandingkan pendekatan berbeda |
| **Ablation Study** | Full system → lepas komponen satu per satu | Mengukur kontribusi tiap komponen |
| **Parameter Study** | Variasikan satu parameter, amati dampak | Uji sensitifitas/robustness |

### Fairness dalam Perbandingan

Perbandingan yang adil = **kondisi identik** untuk semua metode: dataset sama, preprocessing sama, tuning effort sebanding, environment sama, metrik sama.

Contoh tidak adil: Transformer (30 fitur tambahan + Bayesian optimization) vs RF (default params) → hasilnya misleading.

### Threats to Validity = Diidentifikasi Sebelum Eksperimen

Ancaman validitas harus diidentifikasi **sebelum** eksperimen dan mitigasinya dirancang sebagai bagian dari desain — bukan ditulis sebagai boilerplate setelah selesai.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan testing | Memastikan sistem memenuhi requirement | Membuktikan hubungan kausal antar variabel |
| Baseline | Versi sebelumnya (last release) | Metode tervalidasi dari literatur |
| Kegagalan | Bug → fix → release | H₀ tidak ditolak → tetap kontribusi ilmiah |
| Sukses | 100% test pass | Evidence valid — mendukung atau menolak hipotesis |

### Istilah Penting

- **Causality** — Hubungan sebab-akibat (covariance + temporal + elimination)
- **Controlled Experiment** — Ubah satu variabel, kontrol sisanya, amati efek
- **Fairness** — Semua metode diuji pada kondisi yang benar-benar identik
- **Threats to Validity** — Faktor yang bisa melemahkan kesimpulan jika tidak dimitigasi
- **Conclusion Validity** — Validitas statistik: power, sample size, uji yang tepat

---

## Template A.7 — Desain Eksperimen Lengkap

```
EXPERIMENT DESIGN

**Research Question**: Bagaimana performa dan sensitivitas algoritma hibrida AHP-TOPSIS dalam mereduksi bias penilaian pada sistem pengambil keputusan jika diuji menggunakan instrumen data multidimensional?

**Hypothesis**: 
- H0: Intervensi pergeseran bobot kriteria (Delta W) tidak memengaruhi stabilitas urutan peringkat alternatif secara signifikan pada model hibrida AHP-TOPSIS.
- H1: Integrasi metode AHP-TOPSIS secara signifikan mampu mempertahankan stabilitas peringkat alternatif terhadap gangguan pergeseran bobot kriteria (Delta W) hingga batas toleransi tertentu.

**Tipe Eksperimen**: [ ] Comparison  [ ] Ablation  [X] Parameter

Kondisi Eksperimen:
| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | Kondisi murni awal tanpa gangguan (baseline stabilitas). | Delta w = 0 (Bobot AHP asli hasil panel pakar). | Dataset statis 140 siswa $\times$ 13 kriteria, seed 42, dieksekusi via CLI pada isolated local environment. |
| Treatment | Kondisi manipulasi dengan injeksi gangguan inkremental. | Delta w = 10%, 20%,  30%, 40\%, 50\%$. | Dataset statis 140 siswa $\times$ 13 kriteria, seed 42, dieksekusi via CLI pada isolated local environment. |

Fairness Checklist:
  [X] Dataset identik untuk semua kondisi: Menggunakan berkas data masukan 140 siswa yang sama persis di setiap iterasi pengujian.
  [X] Preprocessing setara: Metode normalisasi matriks keputusan terkunci menggunakan rumus Vector Normalization baku pada semua kondisi.
  [X] Tuning effort setara: Algoritma komputasi dijalankan secara otomatis lewat skrip pengulangan (looping script) tanpa intervensi manual di tengah jalan.
  [X] Environment identik: Seluruh skenario pengujian dieksekusi pada perangkat keras, sistem operasi, dan runtime environment yang sama.
  [X] Metrik evaluasi sama: Seluruh hasil akhir diukur secara konsisten menggunakan metrik Rank Spearman dan Execution Time (ms).

Threat Analysis:
| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal | Performa CPU fluktuatif (CPU throttling) akibat proses latar belakang OS yang mendistorsi metrik Execution Time. | Menjalankan eksperimen murni lewat CLI, mematikan seluruh layanan latar belakang non-esensial, melakukan warm-up loops, serta mengambil nilai rata-rata (mean) dari 30 kali running. |
| External | Karakteristik data sampel yang homogen dari satu sekolah membuat karakteristik sensitivitas algoritma sulit digeneralisasi. | Menyediakan fitur injeksi dataset sintetis dengan variasi distribusi data (Normal, Uniform, dan Skewed) untuk menguji batas ketahanan algoritma. |
| Construct | Koefisien Rank Spearman tidak peka terhadap pergeseran urutan jika terdapat banyak nilai alternatif yang kembar (tied ranks). | Mengintegrasikan penanganan komponen tied ranks yang ketat pada fungsi kalkulasi Spearman dan menyandingkannya dengan metrik Kendall's Tau-b. |
| Conclusion | Penarikan kesimpulan bias atau mengalami error tipe I karena hanya melihat selisih nilai deskriptif absolut tanpa uji signifikansi. | Menerapkan uji statistik inferensial non-parametrik formal untuk membuktikan apakah pergeseran peringkat benar-benar signifikan secara statistik. |

**Statistical Plan**:
  Uji statistik   : Wilcoxon Signed-Rank Test.
  Justifikasi      : Data luaran berbentuk peringkat (ordinal/interval) dan didasarkan pada sampel berpasangan (paired sample) antar-kondisi gangguan untuk melihat signifikansi pergeseran urutan alternatif.
  Alpha            : 0.05
  Effect size min  : r >=0.3 (kategori efek moderat untuk uji non-parametrik).
```

---

## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** Bagaimana performa dan sensitivitas algoritma hibrida AHP-TOPSIS dalam mereduksi bias penilaian pada sistem pengambil keputusan jika diuji menggunakan instrumen data multidimensional?
**Tipe eksperimen:** [ ] Comparison / [ ] Ablation / [X] Parameter

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | Mengukur performa peringkat dan kecepatan awal pada bobot kriteria murni. | $\Delta w = 0\%$ | Matrix $140 \times 13$, runtime Node.js/PHP CLI, spesifikasi RAM & CPU terkunci. |
| Treatment | Mengukur tingkat degradasi peringkat dan fluktuasi waktu akibat gangguan bobot. | $\Delta w = \pm 10\% \dots \pm 50\%$ | Matrix $140 \times 13$, runtime Node.js/PHP CLI, spesifikasi RAM & CPU terkunci. |

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria | Status | Detail |
|----------|--------|--------|
| Dataset identik | ✅ Fair | Berkas input CSV berisi data penilaian 140 siswa bersifat read-only selama eksperimen. |
| Preprocessing setara | ✅ Fair | Skrip kalkulasi pembobotan dan pembentukan matriks tidak mengalami perubahan baris kode sedikit pun. |
| Tuning effort setara | ✅ Fair | Semua variasi nilai gangguan ($\Delta w$) dikonfigurasi melalui satu file JSON eksternal secara otomatis oleh sistem. |
| Environment identik | ✅ Fair | Dieksekusi secara lokal pada komputer server uji terisolasi tanpa koneksi jaringan luar untuk menghindari network latency. |
| Metrik evaluasi sama | ✅ Fair | Seluruh kondisi mutlak dinilai berdasarkan nilai $\rho$ akhir dan durasi compute-time. |

**Ada yang tidak fair?** [ ] Ya / [x] Tidak
> Jika ya, bagaimana cara memperbaikinya? ________________

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal | Terjadinya data leakage atau tumpang tindih variabel kontrol saat iterasi loop berjalan berurutan. | Skrip penguji diwajibkan melakukan pembersihan memori (garbage collection) dan inisialisasi ulang array objek pada setiap awal iterasi. |
| External | Penilaian kriteria pakar bersifat sangat subjektif lokal, sehingga hasil pembobotan awal rawan bias kultur institusi. | Melakukan pengujian silang menggunakan variasi bobot acak (randomized weights scenario) untuk memvalidasi performa algoritma secara makro. |
| Construct | Metrik execution time dapat terdistorsi oleh waktu pembacaan file I/O (disk read/write). | Penghitungan waktu eksekusi dipasang super ketat, hanya mengapit baris fungsi algoritma inti AHP-TOPSIS, tidak menghitung proses load data dari disk. |
| Conclusion | Ukuran sampel 140 entri dianggap kurang besar untuk membuktikan kestabilan performa batas atas komputasi algoritma. | Menambahkan skenario uji skalabilitas (scalability stress testing) dengan duplikasi entri data hingga tingkat 1000, 5000, dan 10000 alternatif. |

**Ancaman mana yang paling sulit dimitigasi?** External Validity (Generalisasi Karakteristik Dataset).
**Mengapa?**
> Karena dataset riil diperoleh dari instansi spesifik (MA Mu'allimin Sruweng) yang memiliki kultur dan pola penilaian internal tersendiri. Sangat sulit menjamin bahwa tingkat sensitivitas algoritma hibrida ini akan berperilaku sama persis jika dihadapkan pada dataset sekolah lain yang memiliki karakteristik sebaran nilai atau dinamika konflik kepentingan antar-pakar yang bertolak belakang.

---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
1. Apakah pemilihan dan konfigurasi baseline sudah adil (Fair Baseline Tuning)? Apakah metode baseline yang dijadikan pembanding telah dioptimasi dengan usaha yang setara (hyperparameter tuning), atau sengaja dibiarkan berjalan pada konfigurasi default yang lemah agar metode usulan peneliti terlihat unggul secara instan (straw man comparison)?
2. Apakah seluruh metode diuji pada pipa data dan lingkungan komputasi yang identik (Identical Pipeline & Environment)? Apakah pembanding menggunakan dataset, metode penanganan data hilang (missing value), teknik normalisasi, dan arsitektur perangkat keras yang sama persis, atau terdapat bias eksternal yang menguntungkan metode usulan?
3. Apakah keunggulan performa tersebut terbukti signifikan secara statistik (Statistical Significance Test)? Apakah keunggulan metode usulan didasarkan pada pengujian statistik inferensial (seperti nilai p-value atau pengujian effect size) untuk membuktikan bahwa perbedaan tersebut nyata, atau jangan-jangan klaim keunggulan itu hanya berdasarkan selisih angka desimal absolut yang sangat tipis dan tidak berarti pada hasil rata-rata?
