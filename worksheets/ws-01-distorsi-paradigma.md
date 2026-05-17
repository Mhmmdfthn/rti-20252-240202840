# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---

## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Etika mencegah distorsi yang disengaja (fabrikasi, cherry-picking). Validitas mendeteksi distorsi yang tidak disengaja (confounding variable, sampling bias).

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| **Internal Validity** | Apakah hubungan kausal benar ada? | Confounding variable |
| **External Validity** | Apakah bisa digeneralisasi? | Dataset terlalu homogen |
| **Construct Validity** | Apakah mengukur hal yang benar? | Metrik tidak sesuai klaim |

### Paradigma Riset

Mata kuliah ini menggunakan pendekatan **Positivist** (fenomena TI bisa diukur objektif melalui eksperimen terkontrol) diperkuat **Design Science Research** (artefak dibuat sebagai instrumen pengujian hipotesis, bukan tujuan akhir).

### Mode Berpikir Peneliti

**Curious** (mempertanyakan fenomena) → **Critical** (mengevaluasi klaim berdasarkan bukti) → **Systematic** (merancang investigasi terstruktur dan reproducible).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Membuat sistem yang bekerja | Menghasilkan pengetahuan yang valid |
| Pertanyaan khas | "Bagaimana membuatnya jalan?" | "Apakah klaim ini benar?" |
| Ukuran sukses | Sistem berfungsi, client puas | Hipotesis terjawab, temuan tervalidasi |
| Kegagalan | Harus dihindari | Harus dilaporkan (negative result = kontribusi) |

### Istilah Penting

- **Research Mindset** — Pola pikir yang menuntut bukti dan mempertanyakan asumsi
- **Research Ethics** — Prinsip perilaku: kejujuran, objektivitas, keterbukaan, akuntabilitas
- **HARKing** — Hypothesizing After Results are Known — merumuskan hipotesis setelah melihat data
- **Falsifiability** — Hipotesis harus bisa dibuktikan salah

---

## Template A.1 — Research Mindset Self-Assessment

```
Nama Peneliti    : Muhammad Nuur Fathan
Tanggal          : 17 Mei 2026

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: "Bagaimana cara pengukuran akurasi dilakukan (metrik apa yang digunakan dan pada dataset seperti apa)?"
   - Data yang dibutuhkan untuk verifikasi: Dataset uji (test set), metode validasi (train-test split atau cross-validation) serta perbandingan dengan metode lain.

2. Posisi paradigma:
   - Pendekatan: [✔] Positivis  [ ] Interpretivis  [ ] Design Science  [ ] Mixed
   - Alasan: Penelitian berfokus pada pengukuran kuantitatif (akurasi) dan menggunakan data serta eksperimen untuk membuktikan hipotesis secara objektif.

3. Identifikasi distorsi:
   - Asumsi tersembunyi: Dataset yang digunakan merepresentasikan kondisi dunia nyata secara menyeluruh.
   - Sumber bias potensial: Data tidak seimbang (imbalanced dataset), overfitting pada data latih, atau pemilihan data yang terlalu “bersih”.
   - Langkah mitigasi: Menggunakan cross-validation, dataset yang beragam, evaluasi dengan beberapa metrik (precision, recall, F1-score), serta uji pada data baru (unseen data).

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Seluruh data hasil eksperimen, termasuk hasil yang buruk atau tidak sesuai harapan.
   - Batasan yang diakui sejak awal: Keterbatasan jumlah data, potensi bias dataset, serta keterbatasan generalisasi model ke kondisi berbeda.
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

**Paper yang dipilih:**
> Judul: Sistem Pendukung Keputusan Penilaian Soft skill Siswa Menggunakan Metode AHP-TOPSIS
> Penulis (Tahun): Yuwono Wisudo Pramono, Berlilana, Azhari Shouni Barkah (2026)

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Mengumpulkan data soft skill dari 140 siswa menggunakan kuesioner penilaian mandiri dan lembar observasi guru. | Selection Bias & Self-Reporting Bias: Teknik purposive sampling  berisiko memilih sampel yang kurang heterogen, serta siswa cenderung menilai dirinya lebih baik dari realitas asli|
| Data → Processing | Mengubah data kualitatif menjadi numerik (skala 1-5) , menguji instrumen lewat PLS-SEM , dan menormalisasi matriks keputusan | Information Loss: Mengubah penilaian perilaku manusia yang kompleks menjadi skala angka kaku (1-5) berpotensi menghilangkan konteks atau anomali perilaku tertentu |
| Processing → Analysis | Menghitung bobot kriteria melalui matriks perbandingan berpasangan AHP dan menghitung kedekatan solusi ideal dengan TOPSIS |Expert Subjectivity Bias: Bobot kriteria sepenuhnya bergantung pada penilaian 3 pakar internal. Jika pandangan para pakar tersebut bias, seluruh hasil pembobotan sistem ikut terdistorsi |
| Analysis → Inference | Mendapatkan nilai koefisien kedekatan  untuk meranking siswa dan mengelompokkannya ke dalam 4 kategori kompetensi | Penentuan batas interval kategori ditentukan secara subjektif oleh peneliti tanpa justifikasi teoretis yang kuat |
| Inference → Knowledge | Menyimpulkan bahwa integrasi AHP-TOPSIS efektif, objektif, transparan , dan dapat diadaptasi luas di lingkungan pendidikan. | Overgeneralization: Menarik kesimpulan umum bahwa model ini siap menjadi standar evaluasi berskala besar, padahal validasinya baru diuji pada satu sekolah spesifik. |

**Distorsi paling besar di tahap:** Reality → Data dan Processing → Analysis.

**Dua distorsi spesifik yang teridentifikasi:**
1. Keterbatasan jumlah pakar (hanya 3 orang internal sekolah) dalam mengisi matriks perbandingan berpasangan AHP, sehingga bobot prioritas kriteria yang dihasilkan sangat rentan terhadap bias cara pandang manajemen internal institusi tersebut.
2. Adanya gap validitas pada data input akibat penggunaan self-assessment oleh siswa yang rentan terhadap penilaan subjektif yang tidak jujur atau terlalu optimis (halo effect/social desirability bias).

---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan. (Konteks paper: Misal nilai matriks perbandingan pakar awalnya tidak konsisten (CR > 0.1), namun menjadi konsisten (CR = 0) setelah membuang penilaian salah satu pakar yang dianggap outlier ).

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | Peneliti wajib melaporkan seluruh data point secara utuh. Menghapus outlier hanya demi mengejar target angka agar terlihat "sempurna" atau konsisten (CR = 0) tanpa alasan teknis yang valid adalah bentuk manipulasi data. |
| Transparansi | Jika outlier terpaksa dihapus (misal karena adanya kesalahan input atau kerusakan instrumen), alasan tersebut harus didokumentasikan dan dijelaskan secara eksplisit pada bagian metodologi naskah. |
| Peer review | Menyembunyikan data point outlier akan menyesatkan reviewer dan pembaca, serta membuat riset tersebut kehilangan sifat reproducible (tidak dapat ditiru secara akurat oleh peneliti lain).|

**Keputusan akhir dan justifikasi:**
> Outlier tidak boleh dihapus jika data tersebut merupakan representasi valid dari lapangan. Peneliti harus menyajikan kedua versi analisis (dengan dan tanpa outlier) atau melakukan analisis ketahanan (robustness check). Justifikasi penghapusan hanya sah jika terbukti ada kegagalan teknis/prosedural saat pengambilan data point tersebut.

---

## Latihan 3 — Posisi Paradigma

**Topik riset:** Sistem Pendukung Keputusan Penilaian Soft skill Siswa Menggunakan Metode AHP-TOPSIS

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | 4 | 2 | 5 |
| Jenis data yang dikumpulkan | Metrik numerik skala Likert , nilai eigenvector , indeks konsistensi (CI/CR) , dan koefisien preferensi (Cci)  | Data wawancara awal dengan guru, wali kelas, dan pembina ekskul mengenai kebutuhan kontekstual. | Spesifikasi rancangan model hierarki kriteria , formula integrasi algoritma AHP-TOPSIS , dan hasil uji efektivitas artefak DSS. |
| Limitasi paradigma | Mengabaikan faktor psikologis atau alasan mendalam mengapa nilai soft skill siswa tertentu rendah secara angka | Tidak mampu memberikan standardisasi, peringkat, dan klasifikasi yang objektif untuk skala 140 alternatif siswa. | Artefak model DSS yang sukses di satu sekolah belum tentu bekerja optimal di sekolah lain jika sistem kurikulum dan budayanya berbeda. |

**Paradigma yang dipilih:** Design Science Research diperkuat dengan Positivis.

**Alasan:** Tujuan utama penelitian ini adalah menghasilkan solusi praktis berupa produk/artefak metode baru (Sistem Pendukung Keputusan)  untuk mengevaluasi soft skill. Keberhasilan dan kinerja dari artefak tersebut kemudian diukur dan divalidasi menggunakan perhitungan matematis-kuantitatif yang objektif (Positivis).

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
>Sebelum membaca materi ini, saya sering menganggap grafik peningkatan efisiensi (seperti kenaikan dari 60% ke 90% pada stok barang) adalah kebenaran mutlak. Setelah memahami rantai distorsi, saya sekarang akan mempertanyakan "Bagaimana cara peneliti mengukur angka 90% tersebut dalam sebuah studi literatur tanpa observasi langsung?". Saya akan lebih hati hati terhadap klaim otomatisasi yang mengabaikan faktor manusia/resistensi karyawan.
