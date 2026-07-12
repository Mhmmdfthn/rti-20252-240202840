# Tahap 1: Persiapan Dataset

**Tujuan:** Menyiapkan pasokan data evaluasi (matriks alternatif) yang akan diolah oleh kalkulator AHP-TOPSIS.

## 1. Dataset Riil (140 Baris)
Data ini bersumber dari penilaian kinerja/karakter riil siswa yang dikonversi menjadi file `datasetsimulasi_riil_140.csv`. Berisi 13 kolom indikator penilaian untuk 4 kriteria utama. Dataset ini digunakan untuk memvalidasi algoritma pada skala kasus nyata (skala institusi lokal).

## 2. Dataset Sintetis (10.000 Baris)
Skrip Python (`data_loader.py`) akan menduplikasi dan melakukan variasi *random noise* kecil pada dataset riil untuk membentuk matriks raksasa bernama `synthetic_10k.csv`.
**Fungsi:** Menguji beban ruang waktu (*Big Data* / eksekusi matriks besar) untuk membuktikan asumsi *bottleneck* dari struktur perulangan TOPSIS konvensional.
