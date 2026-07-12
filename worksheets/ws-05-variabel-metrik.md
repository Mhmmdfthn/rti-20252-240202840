# WS-05: Variabel & Metrik

> **Bab 5 — Metric, Measurement & Data**


---

## Ringkasan Materi

### Measurement Alignment Model

Setiap pengukuran yang valid harus bisa ditelusuri melalui rantai ini tanpa lompatan logis:

```
Problem → Concept → Variable → Metric → Data → Result
```

### Operationalization = Keputusan Desain

Menerjemahkan konsep abstrak menjadi variabel terukur bukan proses mekanis. "Code quality" yang diukur via SonarQube code smells membawa asumsi implisit. Setiap operasionalisasi harus didokumentasikan dan dijustifikasi.

### Empat Tipe Data (NOIR)

| Tipe | Ciri | Contoh | Operasi Valid |
|------|------|--------|---------------|
| **Nominal** | Kategori, tanpa urutan | Jenis algoritma (RF, SVM, CNN) | Modus, chi-square |
| **Ordinal** | Urutan, interval tidak sama | Skala Likert (1-5) | Median, Spearman |
| **Interval** | Jarak bermakna, tanpa nol absolut | Suhu Celsius | Mean, Pearson, t-test |
| **Ratio** | Jarak bermakna + nol absolut | Waktu eksekusi (ms) | Semua operasi |

Tipe data menentukan uji statistik yang valid. Kebanyakan metrik performa TI = ratio; persepsi pengguna = ordinal.

### Kriteria Pemilihan Metrik

- **Representative** — Mewakili konsep yang diteliti
- **Sensitive** — Cukup peka menangkap perbedaan bermakna (hindari ceiling effect)
- **Feasible** — Bisa dikumpulkan dalam batasan waktu dan biaya

### Pre-registration

Metrik harus ditentukan **sebelum** eksperimen. Memilih metrik setelah melihat data = **p-hacking**. Metrik tambahan yang ditemukan kemudian dilaporkan sebagai *exploratory*, bukan *confirmatory*.

### Primary vs Secondary Metric

- **Primary Metric** — Langsung terikat ke hipotesis, menentukan kesimpulan
- **Secondary Metric** — Pendukung, dilaporkan di samping primary; statusnya suplementer

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Pemilihan metrik | Berdasarkan kebiasaan/tool yang ada | Berdasarkan construct validity |
| Anomali | Dihapus untuk laporan bersih | Diinvestigasi — bisa jadi temuan |
| Kapan dipilih | Setelah sistem jadi (monitoring) | Sebelum eksperimen (by design) |

### Istilah Penting

- **Operationalization** — Transformasi konsep abstrak menjadi variabel terukur
- **Construct Validity** — Sejauh mana pengukuran benar-benar mengukur konsep yang dimaksud
- **Measurement Scale** — Klasifikasi data (NOIR) yang menentukan analisis valid
- **Multi-metric Evaluation** — Menggunakan beberapa metrik untuk menangkap konsep kompleks

---

## Template A.5 — Definisi Variabel, Metrik & Justifikasi

```
VARIABLE & METRIC DEFINITION

**Research Question**: Bagaimana performa dan sensitivitas algoritma hibrida AHP-TOPSIS dalam mereduksi bias penilaian pada sistem pengambil keputusan jika diuji menggunakan instrumen data multidimensional?

| Variabel | Tipe | Konsep | Metrik | Skala | Satuan | Cara Mengukur | Justifikasi |
|----------|------|--------|--------|-------|--------|---------------|-------------|
| Pergeseran Bobot Kriteria | IV | Tingkat gangguan/manipulasi pada bobot keputusan pakar. | Perubahan Bobot Kriteria ($\Delta w$) | Ratio | % (Persen) | Mengubah nilai bobot kriteria secara inkremental sebesar $\pm 10\%$ hingga $\pm 50\%$ dari nilai asli AHP. | Digunakan untuk menguji batas ketahanan ketangguhan matematis algoritma terhadap fluktuasi bias penilai. |
| Stabilitas Peringkat Akhir | DV | Konsistensi urutan alternatif setelah data diintervensi. | Koefisien Korelasi Rank Spearman ($\rho$) | Interval | — | Menghitung korelasi urutan peringkat alternatif antara kondisi sebelum dan sesudah pergeseran bobot. | Menunjukkan tingkat sensitivitas algoritma dalam mempertahankan urutan keputusan yang valid dari gangguan data. |
| Efisiensi Komputasi | DV | Kecepatan pemrosesan kalkulasi matriks hibrida. | Waktu Eksekusi (Execution Time) | Ratio | ms (Milidetik) | Menggunakan fungsi timer benchmark internal sistem pada saat fungsi komputasi AHP-TOPSIS dijalankan. | Memastikan kompleksitas perhitungan hibrida ini tetap efisien dan layak untuk beban data riil berskala besar. |
| Dimensi Matriks Keputusan | CV | Beban volume data eksperimen yang dibuat konstan. | Ukuran Dataset (Baris $\times$ Kolom) | Ratio | Entri | Mengunci jumlah data uji secara tetap pada angka 140 alternatif (siswa) dan 13 indikator kriteria. | Menghilangkan variabel pengganggu berupa ukuran data agar hasil evaluasi murni menunjukkan performa intrinsik algoritma. |

Alignment Check:
  RQ → Concept → Variable → Metric → Data → Result
  [X] Setiap langkah terdokumentasi
  [X] Tidak ada "lompatan logis"
  [X] Metrik mengukur apa yang dimaksud (construct validity)
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** Bagaimana performa dan sensitivitas algoritma hibrida AHP-TOPSIS dalam mereduksi bias penilaian pada sistem pengambil keputusan jika diuji menggunakan instrumen data multidimensional?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
| Gangguan Bobot | IV | Variasi bias preferensi | Delta Pergeseran Bobot ($\Delta w$) | Ratio | % (Persen) |
| Stabilitas Peringkat | DV | Konsistensi keputusan | Koefisien Korelasi Rank Spearman ($\rho$) | Interval | — |
| Kecepatan Sistem | DV | Efisiensi algoritma | Waktu Eksekusi (Execution Time) | Ratio | ms (Milidetik) |
| Beban Data | CV | Volume data penguji | Dimensi Matriks (140 $\times$ 13) | Ratio | Entri |

**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [x] Tidak
> Jika ya, di mana? ____________________________________

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Representative | 5 | Rank Spearman secara matematis mengukur pergeseran posisi urutan entri (bukan sekadar perubahan skor absolut), sehingga sangat mewakili konsep "stabilitas peringkat". |
| Sensitive | 5 | Metrik ini mampu mendeteksi perubahan posisi urutan sekecil apa pun dari total keseluruhan sebaran 140 alternatif yang diuji. |
| Feasible | 5 | Perhitungan formula Spearman dan pencatatan milidetik execution time dapat diotomatisasi penuh di dalam baris kode program pengujian (benchmarking tool). |

**Apakah perlu secondary metric?** [X] Ya / [ ] Tidak
> Jika ya, apa dan mengapa? Perlu metrik Execution Time (Waktu Eksekusi) sebagai metrik sekunder, karena stabilitas algoritma yang tangguh tidak akan berguna secara praktis di bidang TI jika harus mengorbankan efisiensi waktu komputasi secara drastis (trade-off performa).

**Contoh kasus ceiling effect untuk metrik ini:**
> Ceiling effect terjadi jika nilai Rank Spearman ($\rho$) selalu menunjukkan angka sempurna 1.0 (konstan tidak berubah) meskipun bobot kriteria telah dimanipulasi secara ekstrem hingga pergeseran $\pm 90\%$. Hal ini menandakan metrik atau skenario pengujian gagal menangkap tingkat sensitivitas riil dari algoritma pengambil keputusan.

---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| Completeness | Apakah semua data point terkumpul? | Ya, seluruh data penilaian 140 alternatif untuk 13 indikator wajib terisi penuh. | Menerapkan sistem form validation bertipe required pada aplikasi pengumpul data agar tidak ada nilai null/missing value. |
| Consistency | Apakah ada kontradiksi internal? | Ada potensi kontradiksi logis pada pengisian matriks perbandingan berpasangan oleh pakar. | Membuat sistem otomatisasi pencegahan: algoritma menolak melanjutkan proses kalkulasi jika perhitungan Consistency Ratio menghasilkan nilai $CR > 0.1$. |
| Validity | Apakah benar-benar mengukur yang dimaksud? | Ya, metrik waktu eksekusi harus murni mengukur durasi algoritma, bukan performa jaringan. | Eksperimen komputasi dijalankan secara lokal (isolated local environment/localhost) guna mengeliminasi variabel gangguan berupa network latency. |
| Representativeness | Apakah sampel mewakili populasi target? | Ya, data masukan dari 140 siswa mencakup spektrum sebaran skor kualitatif yang heterogen. | Melakukan analisis deskriptif awal untuk memastikan sebaran nilai input tidak memusat secara ekstrem pada satu angka tunggal saja. |

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
> Memilih metrik setelah melihat data eksperimen dianggap sebagai p-hacking (atau data dredging) karena peneliti cenderung mencari, memilih, atau mengganti metrik secara sengaja (cherry-picking) hanya untuk menemukan hasil akhir yang kebetulan terlihat signifikan, menarik, atau sesuai dengan asumsi awalnya. Tindakan ini merusak validitas riset karena hasil yang dilaporkan bukan mencerminkan keandalan metode yang diuji, melainkan hasil manipulasi pemilihan parameter ukur.
> 
> Perbedaannya dengan eksplorasi data yang sah terletak pada tujuannya. Eksplorasi data (Data Exploration) dilakukan di awal tanpa tendensi pembuktian hipotesis; tujuannya murni untuk memahami karakteristik data mentah, mendeteksi anomali, atau menggali ide untuk membangun hipotesis baru (hypothesis-generating). Sementara dalam Riset Konfirmatori (Confirmatory Research), semua metrik pengujian wajib ditetapkan di awal secara kaku (by design) sebelum data dikumpulkan, agar pengujian performa sistem berjalan adil, objektif, dan dapat direplikasi secara jujur oleh peneliti lain.
