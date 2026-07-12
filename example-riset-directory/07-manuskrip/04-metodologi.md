# 3. Metodologi

Penelitian ini menggunakan desain eksperimental kuantitatif untuk menguji performa model DSS. Arsitektur sistem dirancang untuk menerima input matriks evaluasi dan mengolahnya melalui dua fase komputasi: fase AHP untuk pembobotan, dan fase TOPSIS untuk perankingan alternatif.

## 3.1. Variabel dan Metrik

Penelitian ini memantau variabel operasional berikut:
1. **Pergeseran Bobot Kriteria (IV):** Menguji tingkat gangguan terhadap bobot kriteria sebesar $\pm 10\%$ hingga $\pm 50\%$.
2. **Stabilitas Peringkat Akhir (DV):** Diukur menggunakan Koefisien Korelasi Rank Spearman ($\rho$) untuk mengevaluasi sensitivitas urutan peringkat dari manipulasi bobot.
3. **Efisiensi Komputasi (DV):** Diukur menggunakan *Execution Time* dalam satuan milidetik (ms). 
4. **Dimensi Matriks Keputusan (CV):** Dikunci pada ukuran 140 baris alternatif siswa dan 13 kolom indikator (*soft skill*).

## 3.2. Prosedur Pembobotan AHP

Fase AHP mengolah kriteria utama dan 13 indikator dari 3 pakar utama. Tahapan komputasi mencakup:
1. Pembentukan matriks perbandingan berpasangan (skala 1-9 Saaty).
2. Normalisasi matriks untuk menghasilkan vektor prioritas (bobot kriteria).
3. Evaluasi *Consistency Index* (CI) dan *Consistency Ratio* (CR). Jika CR $\le 0,1$, matriks bobot diterima dan dilanjutkan ke TOPSIS. Jika CR $> 0,1$, matriks ditolak.

## 3.3. Prosedur Perankingan TOPSIS

Dengan input bobot yang telah tervalidasi, matriks penilaian 140 siswa dievaluasi melalui:
1. **Normalisasi Matriks Keputusan:** Mengonversi input mentah ke dalam skala yang dapat dibandingkan.
2. **Matriks Keputusan Ternormalisasi Terbobot:** Mengalikan hasil normalisasi dengan vektor prioritas AHP.
3. **Penentuan Solusi Ideal Positif ($A^+$) dan Solusi Ideal Negatif ($A^-$).**
4. **Perhitungan Jarak:** Mengukur deviasi setiap alternatif terhadap $A^+$ dan $A^-$.
5. **Nilai Preferensi Akhir ($C_i^*$):** Kalkulasi kedekatan relatif untuk menentukan peringkat akhir siswa.

## 3.4. Skenario Pengujian Sistem

Eksperimen komputasi dijalankan dalam *isolated local environment* untuk mengeliminasi gangguan latensi jaringan pada pengukuran metrik *execution time*. Skenario pengukuran (benchmarking tool) dijalankan pada siklus $n=5$ perulangan untuk mendapatkan rata-rata (*mean*) efisiensi sistem *baseline* dibandingkan sistem algoritma hibrida (AHP-TOPSIS). Validitas ketahanan diuji dengan simulasi pergeseran bobot ($\Delta w$) dan menghitung pergeseran posisi alternatif melalui formula korelasi Rank Spearman.
