# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

---

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Akurasi deteksi hanya 78% pada kasus tertentu |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada yang pakai transformer untuk task ini |
| **Data Gap** | Dataset terbatas/tidak representatif | Semua studi pakai dataset sintetis |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada evaluasi di negara berkembang |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database**: IEEE Xplore, ACM DL, Scopus, Google Scholar
2. **Boolean query** yang terdokumentasi eksplisit
3. **Snowballing**: backward (telusuri referensi) + forward (cari yang mengutip)
4. Klaim "belum ada penelitian" harus didukung **bukti pencarian**

### Baseline Selection — 3 Kriteria

| Kriteria | Pertanyaan |
|----------|-----------|
| **Relevan** | Apakah menyelesaikan masalah yang sama? |
| **Representatif** | Apakah mewakili common practice? |
| **State-of-the-Art** | Apakah terbaru/terbaik? |

Membandingkan deep learning 2024 dengan decision tree sederhana tanpa justifikasi = **straw man comparison** (perbandingan tidak jujur).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan baca literatur | Mencari solusi yang sudah ada | Memahami apa yang belum terjawab |
| Cara membaca paper | Tutorial, how-to | Metode, limitasi, gap |
| Baseline | Framework terpopuler | State-of-the-art yang rigorous |
| Dokumentasi pencarian | Tidak diperlukan | Wajib (reproducible) |

### Istilah Penting

- **Concept-centric** — Organisasi literatur berdasarkan konsep/metode, bukan per penulis
- **Snowballing** — Backward (telusuri referensi) + Forward (cari yang mengutip paper kunci)
- **Research Position** — Pernyataan eksplisit posisi riset terhadap studi sebelumnya
- **Straw man comparison** — Memilih baseline lemah agar metode sendiri terlihat lebih baik

---

## Template A.3 — Literature Mapping & Gap Identification

```
LITERATURE MAPPING

Topik      : Sistem Pendukung Keputusan (DSS) Berbasis Multi-Criteria Decision Making (MCDM) pada Domain Manajemen Pendidikan dan Publik.
Database   : Google Scholar.
Query      : ("Sistem Pendukung Keputusan" OR "SPK" OR "MCDM") AND ("AHP" OR "TOPSIS" OR "SAW" OR "SMART") AND ("Pendidikan" OR "Evaluasi")
Tahun      : 2024 – 2026.
Hasil awal : 27 paper → Screening → 5 paper final

Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
|-------|-------|--------|------|--------|------------|
| Pramono, Berlilana, & Barkah | 2026 | Integrasi AHP-TOPSIS | 140 siswa kelas X & XI MA Mu'allimin Sruweng dengan 4 kriteria & 13 indikator. | Mengubah penilaian kualitatif menjadi peringkat kuantitatif berbasis koefisien kedekatan solusi ideal (Cci) secara objektif. | Cakupan data terbatas pada satu lembaga pendidikan lokal, berisiko melahirkan variasi bobot berbeda jika diuji di tempat lain. |
| Afi & Lenggu | 2025 | SMART Method | 10 Alternatif kelurahan di Kota Kupang dengan 5 kriteria spasial-ekonomi. | Berhasil mengotomatisasi pemeringkatan lokasi usaha terfavorit (Sikumana peringkat 1 dengan nilai 0,6625). | Data bersifat statis dari satu instansi dan belum terintegrasi dengan pemetaan geospasial interaktif secara real-time. |
| Husnaini | 2025 | Integrasi AHP-TOPSIS | Data sampel 10 desa pesisir di Kabupaten Pidie berdasarkan 4 indikator ekonomi. | Mampu memproses data hingga 50 entri dengan waktu respons cepat < 5 detik disertai visualisasi grafik. | Keamanan data belum dilengkapi enkripsi tingkat lanjut, sehingga rentan manipulasi data jika diskalakan makro. |
| Oktari, Dernata, & Priyopradono | 2025 | Simple Additive Weighting (SAW) | 10 alternatif calon mahasiswa baru penerima beasiswa KIP Kuliah. | Mempercepat penentuan penerima bantuan finansial secara transparan berdasarkan total poin linear. | Bobot kriteria ditentukan langsung secara subjektif oleh panitia tanpa pengujian rasio konsistensi hierarkis. |
| M. Lutfi & A. Lutfi | 2024 | Analytical Hierarchy Process (AHP) | Parameter kinerja berkala petugas Dinas Kominfo Bondowoso. | Menyusun struktur matriks perbandingan berpasangan untuk meminimalkan subjektivitas kepala dinas. | Evaluasi masih bertumpu pada metode tunggal sehingga visualisasi luaran akhir kurang komprehensif. |

Pola yang ditemukan:
  Metode dominan     : Metode MCDM konvensional dan integrasinya (AHP, TOPSIS, SAW, SMART).
  Dataset umum       : Data sampel spesifik suatu instansi/daerah dengan jumlah kriteria dan alternatif yang terbatas.
  Limitasi berulang  : Subjektivitas dalam pembobotan kriteria, cakupan data yang sempit (lokal), dan hasil evaluasi yang kurang komprehensif/interaktif.

GAP IDENTIFICATION

Gap 1: [Jenis: Method Gap]
  Deskripsi    : Sebagian besar sistem pendukung keputusan seleksi bantuan dan evaluasi kinerja di bidang pendidikan masih mengandalkan metode pembobotan tunggal yang subjektif atau perhitungan linear sederhana (seperti SAW) tanpa menguji konsistensi logika dari preferensi kriteria multidimensi yang digunakan.
  Bukti        : Pada riset seleksi beasiswa KIP Kuliah, panitia menetapkan bobot 8 kriteria secara deterministik (C1=10, C2=7, dst.) tanpa melalui proses penormalan matriks perbandingan berpasangan, sehingga kebenaran relasi antar-kriteria tidak teruji secara matematis.
  Signifikansi : Kegagalan menguji konsistensi bobot kriteria berpotensi melahirkan rank reversal (pembalikan peringkat yang salah) ketika terdapat alternatif baru yang memiliki nilai kemiripan tinggi.

Gap 2: [Jenis: Data & Context Gap]
  Deskripsi    : Belum adanya model DSS evaluasi perilaku (soft skill) atau spasial yang mampu mengintegrasikan data lapangan secara dinamis (real-time) dan fleksibel dari sisi interaksi pengguna (user-level criteria adjustment).
  Bukti        : Sistem penentuan lokasi usaha masih menggunakan data statis kualitatif Dinas , dan sistem evaluasi terdahulu hanya membatasi hak penentuan kriteria pada level administrator.
  Signifikansi : Tanpa adanya pembaruan data dinamis dan fleksibilitas penyesuaian kriteria oleh pengguna akhir, rekomendasi sistem akan cepat usang dan tidak adaptif terhadap perubahan kondisi lapangan yang fluktuatif.
Baseline Selection:
| Baseline | Relevansi | Representatif | Source |
|----------|-----------|---------------|--------|
| AHP-TOPSIS Terintegrasi (Kesejahteraan Pesisir) | Menggunakan kombinasi algoritma yang sama untuk menyelesaikan masalah multi-kriteria. +1 | Mewakili state-of-the-art sistem pendukung keputusan berbasis web yang responsif (< 5 detik). +1 | Husnaini (2025) |
| Simple Additive Weighting (Seleksi Beasiswa) | Sama-sama melakukan penilaian performa individu dalam skala multi-alternatif di institusi akademik. +1 | Mewakili common practice (metode yang paling sering dijadikan pembanding klasik). +4 | Oktari et al. (2025) |
```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan Google Scholar atau database lain.

**Topik riset:** Sistem Pendukung Keputusan (DSS) Berbasis Multi-Criteria Decision Making (MCDM) pada Domain Manajemen Pendidikan dan Publik.
**Query pencarian:** ("Sistem Pendukung Keputusan" OR "SPK" OR "MCDM") AND ("AHP" OR "TOPSIS" OR "SAW" OR "SMART") AND ("Pendidikan" OR "Evaluasi")
**Database:** Google Scholar.

| # | Study | Tahun | Method | Dataset | Result | Limitasi |
|---|-------|-------|--------|---------|--------|----------|
| Pramono, Berlilana, & Barkah | 2026 | Integrasi AHP-TOPSIS | 140 siswa kelas X & XI MA Mu'allimin Sruweng dengan 4 kriteria & 13 indikator. | Mengubah penilaian kualitatif menjadi peringkat kuantitatif berbasis koefisien kedekatan solusi ideal (Cci) secara objektif. | Cakupan data terbatas pada satu lembaga pendidikan lokal, berisiko melahirkan variasi bobot berbeda jika diuji di tempat lain. |
| Afi & Lenggu | 2025 | SMART Method | 10 Alternatif kelurahan di Kota Kupang dengan 5 kriteria spasial-ekonomi. | Berhasil mengotomatisasi pemeringkatan lokasi usaha terfavorit (Sikumana peringkat 1 dengan nilai 0,6625). | Data bersifat statis dari satu instansi dan belum terintegrasi dengan pemetaan geospasial interaktif secara real-time. |
| Husnaini | 2025 | Integrasi AHP-TOPSIS | Data sampel 10 desa pesisir di Kabupaten Pidie berdasarkan 4 indikator ekonomi. | Mampu memproses data hingga 50 entri dengan waktu respons cepat < 5 detik disertai visualisasi grafik. | Keamanan data belum dilengkapi enkripsi tingkat lanjut, sehingga rentan manipulasi data jika diskalakan makro. |
| Oktari, Dernata, & Priyopradono | 2025 | Simple Additive Weighting (SAW) | 10 alternatif calon mahasiswa baru penerima beasiswa KIP Kuliah. | Mempercepat penentuan penerima bantuan finansial secara transparan berdasarkan total poin linear. | Bobot kriteria ditentukan langsung secara subjektif oleh panitia tanpa pengujian rasio konsistensi hierarkis. |
| M. Lutfi & A. Lutfi | 2024 | Analytical Hierarchy Process (AHP) | Parameter kinerja berkala petugas Dinas Kominfo Bondowoso. | Menyusun struktur matriks perbandingan berpasangan untuk meminimalkan subjektivitas kepala dinas. | Evaluasi masih bertumpu pada metode tunggal sehingga visualisasi luaran akhir kurang komprehensif. |

**Pola yang terlihat — Metode dominan:** Penggabungan metode hibrida (hybrid MCDM) jauh lebih dominan digunakan pada tahun 2025–2026 dibandingkan metode tunggal karena mampu memisahkan tahap pembobotan dan tahap eliminasi jarak alternatif secara objektif.
**Limitasi yang berulang:** Ketiadaan pengujian reliabilitas instrumen data input sebelum masuk ke rumus perhitungan inti DSS, menyebabkan sistem sangat rentan terhadap data pencilan (outlier) atau data kualitatif yang bias.

---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [X] Ya / [ ] Tidak | Metode tunggal seperti SAW atau SMART gagal memberikan diferensiasi nilai yang tajam saat alternatif memiliki skor kualitatif yang mirip, sehingga memicu inkonsistensi peringkat. +1 |
| Method Gap | [X] Ya / [ ] Tidak | Jarangnya penggunaan model PLS-SEM sebagai fondasi validitas konvergen instrumen kualitatif sebelum data tersebut diproses ke dalam matriks normalisasi AHP-TOPSIS. +4 |
| Data Gap | [X] Ya / [ ] Tidak | Penggunaan parameter pengukur yang bersifat statis dari kuesioner lembar observasi tradisional tanpa adanya data pembanding sekunder yang bersifat objektif. +1 |
| Context Gap | [X] Ya / [ ] Tidak | Implementasi integrasi algoritma analitis komprehensif untuk mengukur indikator perilaku non-teknis (soft skill) siswa di sekolah formal masih sangat langka. |

**Gap utama yang dipilih:** Method Gap (Integrasi PLS-SEM sebagai validator instrumen pra-MCDM) dikombinasikan dengan Context Gap (Penilaian struktur kriteria hierarkis untuk kompetensi soft skill abad ke-21)
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Karena soft skill memiliki sifat yang tidak berwujud (intangible) dan sangat bergantung pada persepsi psikologis guru penilai. Jika instrumen penilaian tidak divalidasi terlebih dahulu menggunakan pengujian statistik yang ketat seperti PLS-SEM (untuk mengukur Average Variance Extracted dan Cronbach's Alpha) , maka data angka yang dimasukkan ke dalam rumus AHP-TOPSIS hanyalah akumulasi dari bias subjektif guru semata. Penataan inter-relasi metode statistik kuantitatif dan MCDM ini krusial untuk menjamin bahwa luaran rekomendasi peringkat benar-benar valid secara ilmiah dan dapat dipertanggungjawabkan

---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | Model Kombinasi AHP-TOPSIS Web-Based | Menyelesaikan persoalan kalkulasi multi-kriteria menggunakan integrasi dua algoritma penentu bobot dan jarak ideal yang serupa. +1 | Menjadi standar arsitektur sistem berbasis web (PHP-MySQL via XAMPP) yang memiliki efisiensi waktu respons tinggi. +1 | Ya, dipublikasikan pada Februari 2025. | Husnaini (2025) |
| 2 | Model Komparasi SAW & AHP Tingkat Sekolah | Memiliki ranah/domain objek penelitian yang sama, yaitu seleksi dan pemeringkatan siswa di institusi pendidikan formal. +1 | Menggunakan metode Simple Additive Weighting yang menjadi standar acuan evaluasi performa linear di sekolah. +3 | Tidak, namun merupakan common practice yang wajib dijadikan pembanding. +2 | Ningtyas & Diartono (2024) |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [✔] Tidak
> Justifikasi: Pemilihan baseline di atas sama sekali bukan perbandingan yang lemah (straw man). Penelitian ini menghadapkan sistem yang diusulkan langsung dengan model AHP-TOPSIS kontemporer (2025) untuk menguji keandalan fungsionalitas sistem , serta membandingkannya dengan metode SAW yang merupakan penguasa standar common practice dalam evaluasi multi-kriteria di dunia pendidikan. Dengan demikian, pengujian keunggulan sistem dilakukan secara adil, jujur, dan menantang metode yang setara (rigorous evaluation).

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> Gap riset yang valid harus didukung oleh data statistik yang nyata, seperti data peningkatan produktivitas (23-25%) pada jurnal Hafiz & Nasution. Cara membuktikannya adalah dengan menunjukkan bahwa meskipun produktivitas naik, masih ada masalah yang belum tuntas, seperti kompatibilitas teknis dan perubahan budaya yang tidak bisa diselesaikan hanya dengan install software baru.
