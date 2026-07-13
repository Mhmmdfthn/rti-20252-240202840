# Jadwal & Log Pelaksanaan Penelitian

Catatan kronologis pelaksanaan tiap tahap (sumber: riwayat commit git & dokumen `09-docs/tahap-N-*.md`). Tanggal mengikuti `git log`.

## Log Pelaksanaan

| Tanggal | Tahap | Aktivitas | Referensi |
|---|---|---|---|
| 2026-06-25 | Tahap 2 | Penyusunan draf awal dokumen integrasi proposal riset | [ws-08](../../worksheets/ws-08-proposal-integration.md) |
| 2026-06-26 | Tahap 3 | Pencarian referensi data dan penyusunan draf implementasi kode | [ws-09](../../worksheets/ws-09-implementation.md) |
| 2026-06-26 | Tahap 3 | Mengirim email ke jurnal rujukan untuk meminta data riil 140 entri | - |
| 2026-06-26 | Tahap 2 | Finalisasi integrasi proposal & matriks evaluasi (Pesan: "ws08-selesai") | [ws-08](../../worksheets/ws-08-proposal-integration.md) |
| 2026-06-29 | Tahap 3 | Finalisasi rancangan arsitektur implementasi skrip (Pesan: "ws09-selesai") | [ws-09](../../worksheets/ws-09-implementation.md) |
| 2026-07-02 | Tahap 3 | Menyiapkan struktur direktori kode (05-kode, 06-output) & inisialisasi draf worksheet (Pesan: "Update worksheets and add experiment/visualization files") | - |
| 2026-07-04 | Tahap 3 | Melengkapi rencana parameter eksekusi (5 seed, delta 10%-50%) (Pesan: "ws10-selesai") | [ws-10](../../worksheets/ws-10-execution-data.md) |
| 2026-07-06 | Tahap 3 | Menyelesaikan checklist validasi kebersihan data & mitigasi (Pesan: "ws11-selesai") | [ws-11](../../worksheets/ws-11-data-validation.md) |
| 2026-07-06 | Tahap 4 | Mengunggah dataset (riil & sintetis 10.000) serta modul skrip utama (`main.py`, AHP-TOPSIS) (Pesan: "Upload 04-data" & "Upload 05-code") | [04-data](../04-data), [05-kode](../05-kode) |
| 2026-07-06 | Tahap 4 | Eksekusi program AHP-TOPSIS skala penuh (60 runs: 30 dataset riil, 30 dataset sintetis) dan ekstraksi anomali | `benchmark_log.csv` |
| 2026-07-06 | Tahap 4 |  Reorganisasi direktori output ke sub-folder `/logs` & `/plots`, serta pembaruan path pada `experiment_config.json` | - |
| 2026-07-06 | Tahap 2 |  Validasi keselarasan instrumen eksperimen dengan rumusan masalah pada dokumen proposal | - |
| 2026-07-06 | Tahap 4 | Eksekusi 60 runs simulasi, plotting 3 grafik hasil, & penulisan kesimpulan tabel data,serta pengerjaan ws13 (Pesan: "ws12-selesai") | [ws-12](../../worksheets/ws-12-result-presentation.md) |
| 2026-07-06 | Tahap 4 | Mendokumentasikan *cleaning* & justifikasi normalisasi TOPSIS (Pesan: "ws13-selesai") | [ws-13](../../worksheets/ws-13-preprocessing.md) |


## Status Ringkas 

- **Tahap 1: Konseptualisasi & Perumusan Masalah (WS 01-04)**: Selesai.
- **Tahap 2: Desain & Perancangan Eksperimen (WS 05-08)**: Selesai.
- **Tahap 3: Implementasi & Pengumpulan Data (WS 09-11)**: Selesai.
- **Tahap 4: Analisis & Interpretasi Data (WS 12-14)**: Sedang berlangsung (Penyelesaian WS-12 & WS-13).
- **Tahap 5: Penulisan & Publikasi (WS 15-16)**: Belum dimulai.

## Item Tindak Lanjut (Checklist Sebelum Submission)

- [x] Lengkapi matriks literatur dengan paper *related work* nyata ([02-literatur/matriks-literatur.md](../02-literatur/matriks-literatur.md)) — 18 referensi terverifikasi
- [x] Verifikasi CVE-2026-48524 terhadap basis data NVD/MITRE — terkonfirmasi via GHSA-fhv5-28vv-h8m8 (PyJWT, CVSS 3.7)
- [ ] Tetapkan bahasa final naskah (Indonesia/Inggris) sesuai jurnal tujuan
- [ ] Pindahkan konten [07-manuskrip/naskah-jurnal.md](../07-manuskrip/naskah-jurnal.md)/`.docx` ke template jurnal tujuan
- [ ] Finalisasi penempatan figure/tabel sesuai gaya jurnal
- [ ] Review akhir seluruh klaim numerik agar konsisten antar dokumen (lihat daftar pada [07-manuskrip/00-outline.md](../07-manuskrip/00-outline.md))

## Korespondensi

- **2026-06-26 16:34**: Mengirim email ke jurnal rujukan untuk meminta data riil untuk pengujian.
