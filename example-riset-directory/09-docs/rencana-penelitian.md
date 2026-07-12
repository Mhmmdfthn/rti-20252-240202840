# Rencana Penelitian

**Judul:** Analisis Performa Algoritma Hibrida AHP-TOPSIS dalam Reduksi Subjektivitas Data pada Sistem Pengambil Keputusan
**Peneliti:** Muhammad Nuur Fathan

## Latar Belakang & Tujuan
Model AHP-TOPSIS sering dipakai untuk mereduksi bias penilaian, namun sangat jarang dievaluasi ketahanannya secara dinamis. Proyek ini bertujuan untuk menguji tingkat sensitivitas (Rank Reversal) dari algoritma AHP-TOPSIS ketika bobot kriteria terbesarnya disuntikkan gangguan (Noise Injection) secara bertahap (deviasi $\pm 10\%$ hingga $\pm 50\%$).

## Target Publikasi
- **Jurnal:** Jurnal Ilmiah (Sinta 2 / Scopus Q3-Q4)
- **Luaran:** Naskah publikasi dan Skrip Benchmarking *Open Source*.

## Roadmap Tahapan

1. **Tahap 1: Persiapan Dataset**
   Mematangkan matriks evaluasi 140 siswa (*Dataset Riil*) dan ekstrapolasi linear 10.000 baris (*Dataset Sintetis*) untuk uji beban.
2. **Tahap 2: Implementasi Skrip CLI**
   Menulis logika algoritma di `ahp_topsis.py` dan modul gangguan di `sensitivity_test.py` (tanpa GUI/database).
3. **Tahap 3: Pengujian Noise Injection**
   Mengeksekusi skrip untuk menyuntikkan deviasi bobot dan mencatat *Rank Reversal* serta *runtime*.
4. **Tahap 4: Analisis Data**
   Menghitung Koefisien Korelasi Spearman ($\rho$), Kendall Tau ($\tau$), dan mengevaluasi pelambatan komputasi akibat *Big Data*.
5. **Tahap 5: Draf Naskah Jurnal**
   Menyusun struktur Abstrak, Tinjauan Pustaka, Metodologi, hingga Kesimpulan di folder `07-manuskrip/`.
