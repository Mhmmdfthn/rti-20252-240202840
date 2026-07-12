# Outline Manuskrip

**Judul:** Integrasi Metode AHP-TOPSIS dalam Sistem Pendukung Keputusan untuk Evaluasi Soft Skill Siswa yang Objektif

**Target:** Jurnal Nasional Sinta 2 / Konferensi Internasional

**Abstract**
Masalah subjektivitas penilaian soft skill siswa. Mengusulkan integrasi metode AHP-TOPSIS untuk penilaian yang objektif. Hasil pengujian menunjukkan CR ≤ 0.1 dan mampu merangking siswa dengan baik namun terjadi pelambatan komputasi pada sampel besar.

**1. Pendahuluan**
- Konteks: Pentingnya penilaian soft skill yang objektif (Kurikulum Merdeka).
- Gap: Metode konvensional sangat bias dan subjektif, belum ada DSS berbasis AHP-TOPSIS komprehensif untuk kasus ini.
- RQ: Bagaimana efektivitas integrasi AHP-TOPSIS dalam penilaian soft skill?

**2. Tinjauan Pustaka**
- Review metode MCDM pada DSS.
- Batasan penggunaan TOPSIS tunggal (tidak punya mekanisme pembobotan konsisten).
- Keunggulan integrasi pembobotan AHP dengan perankingan TOPSIS.

**3. Metodologi**
- Desain sistem DSS.
- Definisi 4 kriteria utama dan 13 indikator.
- Perhitungan bobot prioritas (AHP) dan pengujian rasio konsistensi (CR).
- Algoritma pemeringkatan (TOPSIS).

**4. Hasil dan Pembahasan**
- Evaluasi pada 140 sampel data siswa.
- Hasil uji konsistensi kriteria (CR ≤ 0.1).
- Distribusi peringkat dan hasil akhir Cci.
- Pengujian waktu komputasi (waktu eksekusi naik 1.66 ms, p=0.008, d=4.89).
- Trade-off antara objektivitas vs skalabilitas komputasi.

**5. Kesimpulan**
- AHP-TOPSIS efektif mereduksi bias penilaian soft skill.
- Memiliki limitasi skalabilitas pada data sangat besar (>1000).
- Future work: Penggunaan arsitektur caching.
