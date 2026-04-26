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

Topik      : Efisiensi Operasional dan Pengambilan Keputusan Strategis melalui Sistem Informasi.
Database   : Google Scholar.
Query      : "Sistem Informasi Manajemen Efisiensi Operasional ERP 2024-2025".
Tahun      : 2024 – 2025.
Hasil awal : 15 paper → Screening → 5 paper final

Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
|-------|-------|--------|------|--------|------------|
| Hidayah et al.|2024|BPMN & Workflow|Data ERP|Berhasil mengidentifikasi 7 titik keputusan kritis. Validasi pesanan mengurangi waktu proses hingga 25% , dan rute optimal memotong waktu perjalanan 15%.|Sistem masih bersifat reaktif/deskriptif. Disarankan integrasi AI untuk prediksi permintaan di masa depan.|
| Ikhwan et al.|2025|VALSAT & VSM|Kualitatif|Fokus pada eliminasi pemborosan (waste) dalam prosedur bisnis dan peningkatan efektivitas sumber daya manusia.|Riset sangat spesifik pada satu lini bisnis (logistik sewa hardware), sehingga sulit untuk digeneralisasi langsung ke industri lain.|
| Fakhrezy|2025|Tematik & Literatur|Literatur terdahulu|Manajemen Risiko Operasional (MRO) krusial untuk mencegah kebocoran data dan serangan siber. Suksesnya digitalisasi bergantung pada teknologi canggih seperti AI dan Blockchain.|Adanya tantangan ketidakpastian regulasi dan keterbatasan kemampuan digital SDM dalam memitigasi risiko siber.|
| Hafiz & Nasution|2025|Mixed (Qual & Quan)|Survei & Wawancara|Produktivitas karyawan meningkat rata-rata 21-25%. Kecepatan pengambilan keputusan meningkat drastis sebesar 50% (dari 14 hari menjadi 7 hari).|Menemukan hambatan berupa resistensi dari anggota organisasi dan kebutuhan investasi awal yang besar.|
| Nandina & Firdaus|2025|Studi Kasus & Literatur|Data Sekunder|SIM berfungsi sebagai pilar integrasi data untuk keputusan efektif. Implementasi terbukti meningkatkan efisiensi operasional dan kualitas produk.|Identifikasi tantangan biaya tinggi, kebutuhan pelatihan intensif bagi karyawan, dan masalah keamanan data.|

Pola yang ditemukan:
  Metode dominan     : enggunaan metode campuran (kualitatif/kuantitatif) dan pemodelan alur kerja (BPMN)
  Dataset umum       : Hasil survei karyawan, data transaksi ERP, dan kajian literatur.
  Limitasi berulang  : Masalah integrasi dengan sistem lama, adaptasi budaya organisasi, dan tantangan keamanan data.

GAP IDENTIFICATION

Gap 1: [Jenis:  method ]
  Deskripsi    : Sebagian besar riset (termasuk Hafiz & Nasution) fokus pada mengukur dampak setelah sistem jadi, tapi sedikit yang menggabungkan analitik prediktif untuk mencegah masalah sebelum terjadi.
  Bukti        : Hasil penelitian Hafiz menunjukkan kecepatan keputusan naik 50%, namun masih bersifat reaktif terhadap data yang sudah ada.
  Signifikansi : Integrasi AI/Machine Learning dibutuhkan agar sistem tidak cuma mencatat efisiensi, tapi juga memprediksi risiko kegagalan.

Gap 2: [Jenis: data]
  Deskripsi    : Kurangnya data mengenai keberlanjutan pemeliharaan SIM setelah fase implementasi awal selesai.
  Bukti        : Hafiz & Nasution menyebutkan ketersediaan anggaran dan pemeliharaan sebagai tantangan jangka panjang yang perlu dipertimbangkan sejak awal.
  Signifikansi : Tanpa rencana pemeliharaan yang jelas, efisiensi yang dicapai di awal (seperti penghematan USD 15.000) bisa hilang karena sistem menjadi usang.
Baseline Selection:
| Baseline | Relevansi | Representatif | Source |
|----------|-----------|---------------|--------|
| SIM Standar |Fokus pada efisiensi biaya dan waktu|Digunakan di banyak organisasi sebagai patokan sukses|Hafiz & Nasution (2024)|
| BPMN & ERP |Fokus pada identifikasi titik keputusan|Metode paling umum untuk audit alur kerja|Hidayah et al. (2024)|
```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan Google Scholar atau database lain.

**Topik riset:** Dampak Implementasi Sistem Informasi terhadap Efisiensi Bisnis.
**Query pencarian:** Dampak Sistem Informasi Manajemen Efisiensi Operasional 2024.
**Database:** Google Scholar.

| # | Study | Tahun | Method | Dataset | Result | Limitasi |
|---|-------|-------|--------|---------|--------|----------|
| 1 | Hidayah et al.|2024|BPMN & Workflow|Data ERP|Berhasil mengidentifikasi 7 titik keputusan kritis. Validasi pesanan mengurangi waktu proses hingga 25% , dan rute optimal memotong waktu perjalanan 15%.|Sistem masih bersifat reaktif/deskriptif. Disarankan integrasi AI untuk prediksi permintaan di masa depan.|
| 2 | Ikhwan et al.|2025|VALSAT & VSM|Kualitatif|Fokus pada eliminasi pemborosan (waste) dalam prosedur bisnis dan peningkatan efektivitas sumber daya manusia.|Riset sangat spesifik pada satu lini bisnis (logistik sewa hardware), sehingga sulit untuk digeneralisasi langsung ke industri lain.|
| 3 | Fakhrezy|2025|Tematik & Literatur|Literatur terdahulu|Manajemen Risiko Operasional (MRO) krusial untuk mencegah kebocoran data dan serangan siber. Suksesnya digitalisasi bergantung pada teknologi canggih seperti AI dan Blockchain.|Adanya tantangan ketidakpastian regulasi dan keterbatasan kemampuan digital SDM dalam memitigasi risiko siber.|
| 4 | Hafiz & Nasution|2025|Mixed (Qual & Quan)|Survei & Wawancara|Produktivitas karyawan meningkat rata-rata 21-25%. Kecepatan pengambilan keputusan meningkat drastis sebesar 50% (dari 14 hari menjadi 7 hari).|Menemukan hambatan berupa resistensi dari anggota organisasi dan kebutuhan investasi awal yang besar.|
| 5 | Nandina & Firdaus|2025|Studi Kasus & Literatur|Data Sekunder|SIM berfungsi sebagai pilar integrasi data untuk keputusan efektif. Implementasi terbukti meningkatkan efisiensi operasional dan kualitas produk.|Identifikasi tantangan biaya tinggi, kebutuhan pelatihan intensif bagi karyawan, dan masalah keamanan data.|

**Pola yang terlihat — Metode dominan:** Penggunaan metode campuran (kualitatif/kuantitatif) dan pemodelan alur kerja (BPMN).
**Limitasi yang berulang:** Masalah integrasi dengan sistem lama, adaptasi budaya organisasi, dan tantangan keamanan data.

---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [✔] Ya / [ ] Tidak |Meskipun kecepatan keputusan naik 50% , performa ini masih bisa ditingkatkan melalui sistem yang bekerja secara proaktif. |
| Method Gap | [✔] Ya / [ ] Tidak |Riset saat ini mayoritas menggunakan pemodelan deskriptif (BPMN) , namun belum banyak mengintegrasikan kecerdasan buatan (AI) untuk prediksi otomatis.|
| Data Gap | [ ] Ya / [✔] Tidak | |
| Context Gap | [✔] Ya / [ ] Tidak |Masih terbatasnya strategi manajemen risiko operasional yang spesifik untuk membantu transformasi digital UMKM di Indonesia.|

**Gap utama yang dipilih:** Method Gap (Integrasi AI dan Analitik Prediktif)
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Karena riset dari Hafiz & Nasution (2024) membuktikan bahwa Sistem Informasi Manajemen (SIM) mampu meningkatkan produktivitas hingga 25% dan mempercepat keputusan sebanyak 50%. Namun, sistem tersebut masih bersifat reaktif atau hanya mengolah data yang sudah terjadi. Gap ini penting untuk diisi agar sistem masa depan tidak hanya mencatat efisiensi, tetapi bisa memprediksi kebutuhan operasional dan risiko sebelum masalah muncul.

---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | SIM Standar | Fokus pada efisiensi biaya dan waktu | Digunakan di banyak organisasi sebagai patokan sukses | Ya | Hafiz & Nasution (2024) |
| 2 |BPMN & ERP|Fokus pada identifikasi titik keputusan|Metode paling umum untuk audit alur kerja|Ya|Hidayah et al. (2024)|

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [✔] Tidak
> Justifikasi: Pemilihan baseline ini tidak dianggap straw man karena metode yang dijadikan pembanding (seperti SIM dan BPMN-ERP) diambil dari penelitian terbaru tahun 2024-2025 yang memang menjadi standar praktik saat ini. Misalnya, riset dari Hafiz & Nasution menunjukkan bahwa SIM standar saja sudah mampu meningkatkan kecepatan pengambilan keputusan hingga 50%. Dengan membandingkan riset baru kita terhadap sistem yang sudah punya performa tinggi tersebut, berarti kita melakukan perbandingan yang jujur dan menantang, bukan sengaja memilih lawan yang lemah atau ketinggalan zaman hanya agar metode kita terlihat lebih unggul.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> Gap riset yang valid harus didukung oleh data statistik yang nyata, seperti data peningkatan produktivitas (23-25%) pada jurnal Hafiz & Nasution. Cara membuktikannya adalah dengan menunjukkan bahwa meskipun produktivitas naik, masih ada masalah yang belum tuntas, seperti kompatibilitas teknis dan perubahan budaya yang tidak bisa diselesaikan hanya dengan install software baru.
