# 5. Kesimpulan

Riset ini telah berhasil merancang, mengimplementasikan, dan mengevaluasi algoritma hibrida AHP-TOPSIS ke dalam Sistem Pendukung Keputusan (DSS) evaluasi *soft skill* siswa. Pengujian komputasi membuktikan bahwa metode AHP-TOPSIS efektif dalam mereduksi bias penilaian dengan memvalidasi inkonsistensi preferensi kriteria pakar (nilai CR $\le 0,1$). Hasil tersebut melahirkan transparansi matriks keputusan, serta menghasilkan profil urutan alternatif siswa yang stabil dan lebih objektif dibandingkan observasi kualitatif semata.

Walaupun algoritma sistem terbukti stabil, integrasi fase AHP dan kalkulasi TOPSIS meningkatkan beban metrik efisiensi, menghasilkan penambahan *execution time* sebesar 1,66 ms dibandingkan sistem tunggal sebelumnya ($p=0,008$, $d=4,89$). Penemuan ini mengungkapkan adanya fenomena limitasi *trade-off* antara ketangguhan validitas pengukuran keputusan melawan efisiensi skalabilitas komputasi pada pemrosesan bervolume ekstrem.

**Penelitian Lanjutan (Future Work)**
Untuk mengeliminasi limitasi kecepatan eksekusi dalam aplikasi sentralisasi data berskala besar (>1000 alternatif instansi pendidikan), peneliti merekomendasikan penggunaan arsitektur *caching* yang membatasi komputasi berulang dari AHP selama rasio bobot preferensi tidak diubah, sehingga fokus daya komputasi *server* hanya didelegasikan pada kalkulasi TOPSIS yang ringan.
