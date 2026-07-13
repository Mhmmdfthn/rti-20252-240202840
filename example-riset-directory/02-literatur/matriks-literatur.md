# Matriks Literatur: Analisis Sensitivitas & Rank Reversal AHP-TOPSIS

Matriks ini merangkum studi-studi kunci yang mendasari eksperimen pengujian ketahanan algoritma hibrida AHP-TOPSIS terhadap fenomena *rank reversal*.

| Study | Tahun | Method | Data | Result | Limitation |
|-------|-------|--------|------|--------|------------|
| Pramono, Berlilana, & Barkah | 2026 | Integrasi AHP-TOPSIS | 140 siswa kelas X & XI MA Mu'allimin Sruweng dengan 4 kriteria & 13 indikator. | Mengubah penilaian kualitatif menjadi peringkat kuantitatif berbasis koefisien kedekatan solusi ideal (Cci) secara objektif. | Tidak menguji kestabilan peringkat jika opini atau prioritas pakar bergeser (analisis sensitivitas). |
| Afi & Lenggu | 2025 | SMART Method | 10 Alternatif kelurahan di Kota Kupang dengan 5 kriteria spasial-ekonomi. | Berhasil mengotomatisasi pemeringkatan lokasi usaha terfavorit. | Mengabaikan dampak korelasi antar kriteria, sangat rentan terhadap manipulasi bobot tunggal. |
| Husnaini | 2025 | Integrasi AHP-TOPSIS | Data sampel 10 desa pesisir di Kabupaten Pidie berdasarkan 4 indikator ekonomi. | Mampu memproses data hingga 50 entri dengan waktu respons cepat < 5 detik. | Kapasitas uji beban belum diekstrapolasi ke ribuan baris data untuk melihat *bottleneck* komputasi. |
| Oktari, Dernata, & Priyopradono | 2025 | SAW | 10 alternatif calon mahasiswa baru penerima beasiswa KIP Kuliah. | Mempercepat penentuan penerima bantuan finansial secara transparan. | Bobot kriteria ditentukan langsung secara subjektif, memicu fenomena *rank reversal* tanpa terdeteksi. |
| Wibowo & Santoso | 2023 | AHP-TOPSIS & Analisis Sensitivitas | Dataset simulasi 500 alternatif. | Menemukan bahwa perubahan bobot sekecil 5% pada kriteria dominan dapat menggeser urutan peringkat 3 teratas. | Hanya diuji pada data hipotetis murni dan tidak membandingkan dengan korelasi Spearman. |
| Kusuma & Pratama | 2024 | Robustness Evaluation MCDM | Eksperimen komputasi pada metode SAW, AHP, dan TOPSIS. | Mengukur tingkat ketahanan masing-masing algoritma terhadap injeksi *noise* pada data evaluasi. | Tidak fokus pada algoritma hibrida (AHP-TOPSIS) yang arsitektur pembobotannya saling bertautan. |

## Pola dan Sintesis

- **Fokus Historis MCDM:** Mayoritas penelitian masih berfokus pada "pembangunan" aplikasi DSS untuk studi kasus lokal spesifik (siswa, beasiswa, desa) tanpa melakukan pengujian batas keamanan logika algoritmanya.
- **Kesadaran Kerapuhan Algoritma:** Literatur terbaru (Wibowo & Santoso; Kusuma & Pratama) mulai menyoroti bahwa arsitektur MCDM (termasuk TOPSIS) sangat rapuh terhadap *Rank Reversal* akibat perubahan bobot kriteria yang dinamis atau gangguan (*noise*).
- **Limitasi Pengujian:** Literatur sensitivitas belum memadukan dataset riil berskala besar (penggunaan data lapangan asli) dengan pengujian komputasi eksperimental yang mengukur *runtime* efisiensi mesin.
- **Research Gap Teridentifikasi:** Belum adanya pengujian eksperimental struktural (*benchmarking* dengan skrip otomatis) yang menyuntikkan deviasi bobot terukur (*noise injection*) untuk memetakan secara pasti ambang batas toleransi *rank reversal* dari model algoritma hibrida AHP-TOPSIS pada skala dataset riil dan *Big Data*.
