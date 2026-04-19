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
Tanggal          : 19 April 2026

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
> Judul: Penerapan Sistem Informasi untuk Meningkatkan Efisiensi Operasional dan Pengambilan Keputusan di Perusahaan
> Penulis (Tahun): Erwin Teguh Arujisaputra (2025)

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Mengumpulkan data sekunder dari Scopus, ScienceDirect, dan Google Scholar | Selection Bias: Hanya memilih literatur 10 tahun terakhir, sehingga teori fundamental yang lebih tua mungkin terabaikan. |
| Data → Processing | Menyaring literatur menggunakan kata kunci spesifik seperti "sistem informasi" | Language/Terminology Bias: Artikel relevan yang menggunakan istilah teknis berbeda mungkin tidak terjaring. |
| Processing → Analysis | Menggunakan analisis tematik untuk mengidentifikasi pola efisiensi | Subjective Interpretation: Penentuan tema "manfaat" dan "tantangan" sangat bergantung pada perspektif subjektif peneliti. |
| Analysis → Inference | Menyimpulkan efisiensi ERP mencapai 85-90% pada manajemen keuangan dan persediaan. | Generalization Bias: Angka efisiensi ini mungkin berbeda jauh pada UKM yang memiliki keterbatasan sumber daya dibanding perusahaan besar. |
| Inference → Knowledge | Menyatakan sistem informasi adalah komponen kunci pilar efisiensi operasional. | Confirmation Bias: Cenderung menyoroti sisi sukses implementasi, sementara data kegagalan sistem sering jarang dipublikasikan di jurnal. |

**Distorsi paling besar di tahap:** Reality → Data karena ketergantungan penuh pada data sekunder.

**Dua distorsi spesifik yang teridentifikasi:**
1. Inclusion Criteria Limitation: Pembatasan waktu publikasi 10 tahun terakhir dapat memutus konteks evolusi teknologi yang lebih panjang.
2. Operational Complexity Oversight: Angka efisiensi tinggi pada grafik sering kali mengabaikan "biaya tersembunyi" dari pelatihan berkelanjutan dan adaptasi budaya.

---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | Peneliti wajib melaporkan bahwa ERP meningkatkan efisiensi persediaan hingga 90% tetapi mungkin kurang berdampak pada fungsi lain jika integrasinya gagal. |
| Transparansi | Menjelaskan tantangan seperti biaya tinggi dan resistensi perubahan secara jujur agar pembaca tidak mendapat ekspektasi palsu |
| Peer review | Memberikan ruang bagi peneliti lain untuk melakukan validasi empiris atas klaim literatur tersebut.|

**Keputusan akhir dan justifikasi:**
> Melaporkan hasil secara komprehensif termasuk kendala teknis dan non-teknis. Justifikasi: Kegagalan atau stagnansi data adalah informasi krusial bagi manajer untuk melakukan perencanaan yang lebih matang.

---

## Latihan 3 — Posisi Paradigma

**Topik riset:** Penerapan Sistem Informasi untuk Meningkatkan Efisiensi Operasional dan Pengambilan Keputusan di Perusahaan.

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | 4 | 3 | 5 |
| Jenis data yang dikumpulkan | Data statistik efisiensi (misal: kenaikan efisiensi dari 50% ke 85%). | Deskripsi mengenai tantangan resistensi perubahan dan budaya organisasi. | Analisis peran sistem ERP sebagai instrumen untuk otomatisasi proses bisnis. |
| Limitasi paradigma | Angka efisiensi sekunder mungkin tidak mencerminkan variabel unik di tiap perusahaan. | Tidak memberikan solusi teknis yang terukur secara matematis. | Terlalu fokus pada kegunaan alat (tool) sehingga mengabaikan sisi psikologi pengguna. |

**Paradigma yang dipilih:** Design Science Research diperkuat dengan Positivis.

**Alasan:** Penelitian ini berfokus pada bagaimana sebuah artefak teknologi (Sistem Informasi/ERP) dirancang dan diterapkan untuk menyelesaikan masalah nyata di perusahaan (inefisiensi). Penggunaan paradigma Positivis juga terlihat dari cara peneliti mevalidasi keberhasilan sistem tersebut menggunakan metrik yang objektif dan terukur, seperti persentase efisiensi pada fungsi keuangan, persediaan, dan produksi.

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
>Sebelum membaca materi ini, saya sering menganggap grafik peningkatan efisiensi (seperti kenaikan dari 60% ke 90% pada stok barang) adalah kebenaran mutlak. Setelah memahami rantai distorsi, saya sekarang akan mempertanyakan "Bagaimana cara peneliti mengukur angka 90% tersebut dalam sebuah studi literatur tanpa observasi langsung?". Saya akan lebih hati hati terhadap klaim otomatisasi yang mengabaikan faktor manusia/resistensi karyawan.
