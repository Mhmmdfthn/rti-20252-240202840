# Laporan Penelitian

**Judul:** Analisis Performa Algoritma Hibrida AHP-TOPSIS dalam Reduksi Subjektivitas Data pada Sistem Pengambil Keputusan
**Peneliti:** Muhammad Nuur Fathan
**Target Publikasi:** Jurnal Ilmiah
**Status Penelitian:** Tahap penyelesaian eksperimen simulasi dan penyusunan naskah jurnal.

---

## 1. Ringkasan Eksekutif

Penelitian ini mengevaluasi secara empiris ketahanan dan stabilitas algoritma hibrida **AHP-TOPSIS** terhadap anomali *Rank Reversal* akibat perubahan dinamis pada bobot kriteria pakar. Eksperimen dilakukan menggunakan pendekatan *Noise Injection* melalui skrip *benchmarking* (CLI Python) yang memanipulasi bobot kriteria tertinggi dengan rentang deviasi ($\Delta W$) antara $\pm 10\%$ hingga $\pm 50\%$.

Pengujian dilakukan menggunakan dua jenis matriks keputusan: 
1. **Dataset riil:** 140 baris (mewakili jumlah siswa).
2. **Dataset sintetis:** Skala hingga 10.000 baris (untuk uji *stress-test* dan *runtime* komputasi).

**Temuan utama:**
- Algoritma AHP-TOPSIS terbukti **sangat stabil** menghadapi fluktuasi minor. Pada deviasi $\le \pm 20\%$, nilai Koefisien Korelasi Spearman ($\rho$) dan Kendall Tau ($\tau$) bertahan di rasio stabilitas $\ge 0.95$.
- Teridentifikasi **ambang batas toleransi (safety margin)** pada deviasi $\ge \pm 30\%$, di mana terjadi penurunan korelasi drastis menuju $\rho = 0.70$ dan memicu pembalikan peringkat (*Rank Reversal*) yang signifikan pada posisi papan tengah.
- **Efisiensi komputasi (*Runtime*)** tidak dipengaruhi oleh fluktuasi penyuntikan bobot (*noise*), namun semata-mata dipengaruhi oleh pertumbuhan eksponensial matriks (volume *Big Data*), yang mendemonstrasikan titik *bottleneck* arsitektur TOPSIS konvensional.

Seluruh repositori data, instrumen skrip komputasi, dan naskah jurnal tersedia di repositori ini.

---

## 2. Latar Belakang dan Rumusan Masalah

### 2.1 Latar Belakang
Sistem Pendukung Keputusan (SPK) dirancang untuk mentransformasi evaluasi kualitatif menjadi data kuantitatif secara objektif. Dalam model *Multi-Criteria Decision Making* (MCDM), integrasi **AHP dan TOPSIS** seringkali digunakan karena AHP mampu memvalidasi konsistensi pandangan pakar secara hierarkis (melalui nilai *Consistency Ratio*/CR), sedangkan TOPSIS bertugas menyeleksi ratusan alternatif dengan efisien. 

Meskipun tangguh secara teori, arsitektur MCDM rentan terhadap fenomena *Rank Reversal*, yakni perubahan urutan rekomendasi keputusan akibat perubahan kecil pada parameter input (seperti bobot pakar yang bergeser atau bias injeksi data). Sayangnya, literatur akademis saat ini lebih banyak berfokus pada "pembuatan aplikasi web/DSS" alih-alih melakukan *stress test* algoritmik untuk mencari tahu batas keamanan logika perhitungan mesinnya.

### 2.2 Rumusan Masalah
1. Sejauh mana algoritma hibrida AHP-TOPSIS dapat mempertahankan stabilitas korelasi urutan peringkat ketika diberi intervensi gangguan pergeseran bobot secara inkremental?
2. Pada tingkat deviasi bobot ($\Delta W$) berapakah algoritma ini mulai mengalami degradasi *Rank Reversal* yang tidak dapat ditoleransi?
3. Bagaimana beban efisiensi komputasi (*runtime*) dari algoritma ini saat dieksekusi menggunakan volume matriks berdimensi besar (hingga 10.000 alternatif)?

---

## 3. Metodologi dan Pelaksanaan

Penelitian dijalankan tanpa aplikasi antarmuka grafis (GUI) maupun sistem *database* konvensional. Sebagai gantinya, eksperimen murni dieksekusi secara otomatis oleh skrip Python.

### 3.1 Skema Implementasi Modul Skrip (*Backend Engine*)
Implementasi komputasi dibagi menjadi empat fungsi Python di `05-kode/experiment/src/`:
- **`data_loader.py`**: Mengimpor matriks dataset riil (140 baris) dan membangkitkan matriks *dummy* (10.000 baris) sebagai suplai data memori. Modul ini juga mendeklarasikan *pairwise matrix* awal.
- **`ahp_topsis.py`**: *Calculation Engine* yang menghitung nilai Eigen AHP, memvalidasi rasio CR, menormalisasi data, dan menghitung jarak kedekatan absolut TOPSIS untuk membuahkan *ground truth baseline*.
- **`sensitivity_test.py`**: Inti dari eksperimen yang menyuntikkan *noise* deviasi pada bobot kriteria. Lalu, membandingkan urutan *baseline* dengan urutan terdeviasi menggunakan korelasi statistik.
- **`logger.py`**: Mencatat setiap *looping* variabel ke file rekaman hasil `.csv`.

### 3.2 Skenario Pengukuran (Benchmarking)
Pengujian dijalankan pada lingkungan terisolasi untuk merekam *execution time* secara akurat (tanpa latensi jaringan). Eksperimen menyuntikkan rentang deviasi $\pm 10\%$, $\pm 20\%$, $\pm 30\%$, $\pm 40\%$, dan $\pm 50\%$ secara sekuensial. Tiap iterasi merekam: nilai $\Delta W$, korelasi Rank Spearman ($\rho$), korelasi Kendall Tau ($\tau$), dan lama *runtime* (ms).

---

## 4. Hasil Penelitian

Analisis mendalam dari eksperimen dapat dibaca pada naskah jurnal bagian [Hasil dan Pembahasan](../07-manuskrip/05-hasil-analisis.md). Berikut rangkuman utamanya:

### 4.1 Stabilitas Peringkat dan Penemuan Rank Reversal
- **Validasi Awal (Baseline):** Uji konsistensi pakar AHP mencatatkan $CR \le 0.1$, mengonfirmasi bahwa bobot asli memenuhi syarat validitas matematis.
- **Daya Tahan Tinggi ($\Delta W \le \pm 20\%$):** Algoritma menunjukkan *robustness* yang kuat; mayoritas urutan peringkat (terutama kuartil atas) tidak mengalami pembalikan posisi, menghasilkan nilai $\rho$ dan $\tau$ $\ge 0.95$.
- **Ambang Toleransi (Threshold):** Saat injeksi *noise* diperbesar ke $\pm 30\%$ dan $\pm 50\%$, terjadi *Rank Reversal* signifikan. Nilai korelasi $\rho$ anjlok membentuk kurva eksponensial menuju $0.70$. Pergeseran urutan terekstrem terjadi pada alternatif data di papan tengah.

### 4.2 Kinerja Komputasi Komputasional (*Runtime*)
- Deviasi bobot pada modul *Weight Manipulator* tidak memberi tekanan tambahan pada spesifikasi memori mesin (karena hanya menambah 1 siklus vektor). 
- Namun, saat skala data didorong ke angka 10.000 baris alternatif (Dataset Sintetis), tahap penentuan skor ideal TOPSIS mengalami pelambatan *runtime* yang sangat eksponensial ($p < 0.05$ menggunakan uji Wilcoxon Signed-Rank), yang mengindikasikan bahwa struktur pengulangan *for-loop* klasik TOPSIS adalah *bottleneck* komputasi absolut.

---

## 5. Kesimpulan dan Saran

### 5.1 Kesimpulan
Skema arsitektur integrasi AHP-TOPSIS sangat efektif dan stabil di lingkungan operasional biasa asalkan pergeseran bias bobot tidak melampaui $\pm 20\%$. Namun, algoritma ini menampakkan batas limitasi strukturalnya pada deviasi bobot yang lebih masif (terjadinya *rank reversal*) dan pada paparan matriks skala *Big Data* (pelambatan kecepatan eksekusi).

### 5.2 Saran (*Future Work*)
Penelitian ke depan disarankan menggunakan struktur array teroptimasi (misal, fungsionalitas vektorisasi `NumPy` penuh) untuk mengakali batas *runtime* pada skala alternatif masif. Metode simulasi *Noise Injection* berbasis CLI ini juga patut direplikasi ke algoritma MCDM lain (seperti VIKOR atau PROMETHEE) untuk menetapkan protokol standar ketahanan algoritma.

---

## 6. Lampiran — Peta Artefak Penelitian

| Direktori/Folder | Keterangan Artefak |
|---|---|
| [`01-proposal/`](../01-proposal/) | Proposal awal riset, lengkap dengan definisi matriks pengujian dan indikator evaluasi. |
| [`02-literatur/`](../02-literatur/) | Matriks literatur kajian dan daftar pustaka `.bib` (mengidentifikasi minimnya *stress test* MCDM). |
| [`03-teori/`](../03-teori/) | Diagram skematik *flowchart* eksperimen, arsitektur *engine CLI*, dan pola CSV. |
| [`04-data/`](../04-data/) | Data mentah berupa dataset 140 baris dan 10.000 baris matriks, beserta log eksperimen. |
| [`05-kode/`](../05-kode/) | Kode sumber implementasi skrip Python (Data Loader, AHP-TOPSIS Engine, Logger, Sensitivity Test). |
| [`07-manuskrip/`](../07-manuskrip/) | Draf lengkap penulisan Naskah Jurnal Publikasi. |
| [`08-laporan/`](../08-laporan/) | Laporan Penelitian ini. |
