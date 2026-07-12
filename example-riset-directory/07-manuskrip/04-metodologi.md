# 4. Metodologi

## 4.1. Desain Eksperimen dan Unit Analisis
Penelitian ini menggunakan desain kuantitatif eksperimental parameter (*benchmarking*) dalam lingkungan laboratorium komputer terisolasi (localhost). Unit analisis difokuskan pada perilaku struktural dan ketahanan logika algoritma hibrida AHP-TOPSIS saat diintervensi oleh gangguan bobot (*noise injection*). Alih-alih membangun aplikasi SPK, instrumen yang digunakan adalah skrip *Command-Line Interface* (CLI) khusus yang mengeksekusi komputasi secara *backend*.

## 4.2. Variabel dan Metrik Pengukuran
1. **Injeksi Deviasi Bobot / *Noise* (Variabel Independen):** Tingkat gangguan ($\Delta W$) yang ditambahkan dan dikurangkan pada kriteria utama (yang memiliki bobot awal tertinggi), dengan skala inkremental $\pm 10\%$, $\pm 20\%$, hingga $\pm 50\%$. Pasca-injeksi, seluruh bobot dinormalisasi ulang agar total tetap 1.0.
2. **Stabilitas Peringkat (Variabel Dependen):** Diukur menggunakan Koefisien Korelasi Rank Spearman ($\rho$) dan Kendall Tau ($\tau$). Membandingkan peringkat alternatif hasil intervensi terhadap peringkat acuan awal (*baseline*). Rentang korelasi bergerak dari -1 hingga 1.
3. **Efisiensi Komputasi (Variabel Dependen):** Waktu eksekusi atau *runtime* dalam milidetik (ms) untuk mengukur *bottleneck* pemrosesan saat volume alternatif diperbesar. Uji beda dilakukan melalui Wilcoxon Signed-Rank.
4. **Dataset (Variabel Kontrol):** Menggunakan dua kategori:
   - Dataset riil: 140 entri data siswa dengan 13 indikator matriks evaluasi *soft skill*.
   - Dataset sintetis: Perluasan ekstrapolasi linear hingga 10.000 entri untuk kebutuhan uji beban (*load testing*).

## 4.3. Prosedur dan Skenario Pengujian
Eksperimen diawali dengan mengalkulasi bobot prioritas kriteria murni (dari pakar) menggunakan metode AHP hingga mencapai nilai *Consistency Ratio* (CR) $\le 0.1$. Berbekal bobot terukur ini, fase TOPSIS dijalankan terhadap 140 alternatif riil dan direplikasi ke dataset sintetis untuk memproduksi urutan peringkat acuan (*baseline*).

Selanjutnya, modul *Weight Manipulator* secara iteratif menyuntikkan deviasi bobot. Untuk setiap level $\Delta W$, mesin TOPSIS mengalkulasi ulang peringkat akhir. Hasil peringkat deviatif tersebut lalu dievaluasi kemiripan urutannya dengan urutan acuan menggunakan korelasi Spearman dan Kendall Tau. Catatan mengenai deviasi, korelasi, dan *runtime* direkam secara otomatis ke dalam *file log* eksperimen (CSV).
