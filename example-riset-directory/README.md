# Analisis Performa Algoritma Hibrida AHP-TOPSIS dalam Reduksi Subjektivitas Data

**Judul Penelitian:** Analisis Performa Algoritma Hibrida AHP-TOPSIS dalam Reduksi Subjektivitas Data pada Sistem Pengambil Keputusan
**Target publikasi:** Jurnal Ilmiah (Sinta 2 / Scopus Q3-Q4)

## Ringkasan

Penelitian ini mengevaluasi tingkat sensitivitas dan stabilitas hasil pemeringkatan algoritma hibrida **AHP-TOPSIS** melalui penyuntikan gangguan bobot (*noise injection*). Tujuannya adalah untuk mendeteksi kerentanan algoritma terhadap fenomena **Rank Reversal** (pembalikan peringkat) yang dapat mencederai objektivitas rekomendasi Sistem Pendukung Keputusan (SPK).

Metode yang digunakan adalah eksperimen berbasis simulasi komputasi *Command Line Interface* (CLI). Bobot kriteria dimanipulasi secara inkremental (deviasi $\pm 10\%$ hingga $\pm 50\%$) untuk melihat dampaknya pada pemeringkatan akhir TOPSIS. Stabilitas diukur menggunakan korelasi **Spearman Rank ($\rho$)** dan **Kendall Tau ($\tau$)**, sementara kinerja komputasi (*bottleneck*) dianalisis melalui perekaman **runtime (ms)** pada matriks data riil (140 baris) dan data sintetis (10.000 baris).

Detail lengkap topik & roadmap: [09-docs/rencana-penelitian.md](09-docs/rencana-penelitian.md)

## Struktur Direktori

| Folder | Isi |
|---|---|
| [00-admin/](00-admin/) | Administrasi penelitian (jadwal, korespondensi) |
| [01-proposal/](01-proposal/) | Proposal penelitian awal |
| [02-literatur/](02-literatur/) | Referensi & *paper* terkait (Matriks Literatur Sensitivitas MCDM) |
| [03-teori/](03-teori/) | Arsitektur skrip *benchmarking* & desain skema CSV |
| [04-data/](04-data/) | Data mentah berupa *dataset* riil 140 baris & sintetis 10k baris |
| [05-kode/](05-kode/) | *Source code* Python (Modul *AHP-TOPSIS Engine* & *Noise Injection*) |
| [06-output/](06-output/) | Statistik & visualisasi *Spearman*, *Kendall Tau*, dan *Runtime* |
| [07-manuskrip/](07-manuskrip/) | Draf naskah jurnal akhir |
| [08-laporan/](08-laporan/) | Laporan komprehensif penelitian |
| [09-docs/](09-docs/) | Dokumen perencanaan & *roadmap* tahap-tahap penelitian |

## Status Tahapan

- [x] **Tahap 1** — Persiapan Dataset Riil & Sintetis — *Selesai* ([detail](09-docs/tahap-1-persiapan-dataset.md))
- [x] **Tahap 2** — Implementasi Skrip CLI Python — *Selesai* ([detail](09-docs/tahap-2-implementasi-skrip.md))
- [x] **Tahap 3** — Pengujian Injeksi Noise & Pencatatan Log — *Selesai* ([detail](09-docs/tahap-3-pengujian-noise.md))
- [x] **Tahap 4** — Analisis Hasil (Korelasi & Runtime) — *Selesai* ([detail](09-docs/tahap-4-analisis-hasil.md))
- [ ] **Tahap 5** — Penyusunan Naskah Jurnal — *Sedang berjalan* ([detail](09-docs/tahap-5-publikasi.md))

## Laporan Penelitian

Laporan penelitian komprehensif (ringkasan eksekutif, metodologi, hasil eksperimen, kesimpulan): [08-laporan/laporan-penelitian.md](08-laporan/laporan-penelitian.md)


## Author

Muhammad Nuur Fathan
