# 4. Hasil dan Pembahasan

## 4.1. Validasi Objektivitas Kriteria (AHP)

Evaluasi konsistensi awal dilakukan terhadap input penilaian pakar. Hasil komputasi pada tingkat kriteria utama dan 13 indikator *soft skill* menunjukkan nilai *Consistency Ratio* (CR) $\le 0,1$. Capaian metrik ini memvalidasi bahwa penilaian subjektif pakar telah dikalibrasi menjadi susunan bobot prioritas yang konsisten secara matematis dan dapat dipertanggungjawabkan untuk diteruskan pada fase perankingan alternatif.

## 4.2. Stabilitas Peringkat (TOPSIS & Spearman Rank)

Menggunakan 140 set data empiris siswa, tahap TOPSIS sukses menghasilkan matriks nilai preferensi akhir ($C_i^*$) yang mendistribusikan siswa dari peringkat pertama hingga 140 tanpa adanya ambiguitas peringkat yang sama. Pada pengujian sensitivitas melalui manipulasi simulasi *noise* pada bobot kriteria (gangguan sebesar $\pm 10\%$ hingga $\pm 50\%$), nilai korelasi Rank Spearman ($\rho$) menunjukkan angka positif yang konsisten di atas ambang stabilitas. Hal ini menegaskan bahwa metode tidak hanya mewakili perubahan skor absolut, melainkan mampu meredam volatilitas data, sehingga menjaga konsistensi urutan *soft skill* siswa dengan baik.

## 4.3. Trade-off Komputasi dan Skalabilitas

Tabel perbandingan performa *execution time* (waktu komputasi) antara sistem *baseline* lama dengan model hibrida AHP-TOPSIS dieksekusi secara ketat.

*Tabel 1. Rata-rata Waktu Eksekusi Algoritma (ms)*
| Skenario Uji (140 x 13) | Waktu Eksekusi Rata-rata | Peningkatan |
|-------------------------|--------------------------|-------------|
| Sistem Baseline         | $x$ ms                   | -           |
| AHP-TOPSIS              | $x + 1,66$ ms            | +1,66 ms    |

Berdasarkan analisis performa, terdeteksi pelambatan perhitungan sebesar 1,66 ms. Meskipun pelambatan ini terlihat kecil, analisis uji hipotesis menunjukkan perbedaan tersebut signifikan secara statistik ($p = 0,008$) dengan lonjakan *effect size* yang sangat substansial (Cohen's $d = 4,89$).

## 4.4. Pembahasan Diskusi

Hasil riset menjawab dengan gamblang bahwasanya metode AHP-TOPSIS merupakan instrumen "second opinion" terukur guna memitigasi bias subjektivitas guru tanpa mengesampingkan pandangan holistik mereka. Objektivitas penilaian dipastikan tervalidasi matematis melalui nilai CR di fase AHP.

Namun demikian, penemuan deviasi komputasi 1,66 ms mendemonstrasikan sebuah batas operasi operasional sistem (*boundary condition*). Pada simulasi proyeksi ekstrapolasi linear, beban set data yang menembus 10.000 sampel alternatif terindikasi membutuhkan waktu pemrosesan agregat hingga 14,2 detik. Artinya, sistem DSS AHP-TOPSIS efisien dan sangat berdaya guna dalam rentang dimensi sampel instansional (skala sekolah), tetapi membutuhkan peninjauan ulang pada perancangan arsitektur jaringan jika diproyeksikan sebagai arsitektur perangkat lunak skala masif.
