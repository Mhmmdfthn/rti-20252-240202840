# WS-15: Scientific Writing

> **Bab 15 — Penulisan Ilmiah**

---

## Ringkasan Materi

### Scientific Argument Flow

```
Problem → Gap → RQ → Method → Result → Analysis → Conclusion → Contribution
```

Paper ilmiah adalah **satu argumen utuh** dari masalah ke kontribusi. Setiap node harus terhubung logis ke node sebelum dan sesudahnya.

### Struktur IMRAD

| Section | Peran | Pertanyaan Kunci |
|---------|-------|-----------------|
| **Introduction** | Motivasi + frame | Why is this needed? |
| **Method** | Deskripsi (reproducible) | How was it done? |
| **Results** | Laporan objektif | What was found? |
| **Discussion** | Interpretasi + refleksi | What does it mean? |
| **Conclusion** | Ringkasan + kontribusi | So what? |

### Logical Flow — "Red Thread"

Setiap paragraf menjawab satu pertanyaan dan memicu pertanyaan berikutnya. Alur logis ini harus terasa di tiga level:
1. **Antar-kalimat** dalam paragraf
2. **Antar-paragraf** dalam section
3. **Antar-section** dalam paper

### Internal Consistency

Setiap elemen yang dijanjikan di Introduction harus hadir di Discussion/Conclusion.

**Consistency Matrix:**
```
           Intro  Method  Result  Discuss  Conclude
RQ1          ✓      ✓       ✓       ✓        ✓
RQ2          ✓      ✓       ✓       ✗ ←      ✓
Metrik-X     ✗      ✗       ✓ ←     ✗        ✗
```
**Masalah:** RQ2 dibahas di semua bagian kecuali Discussion. Metrik-X muncul di Result tapi tidak diperkenalkan di Method.

### Writing Quality Triad

| Kualitas | Deskripsi | Contoh Buruk → Baik |
|----------|----------|---------------------|
| **Clarity** | Dipahami sekali baca | "Performa meningkat" → "Accuracy meningkat dari 85.3% ke 89.7%" |
| **Precision** | Istilah eksak, tanpa ambiguitas | "signifikan" → "signifikan secara statistik (p=0.003, d=1.2)" |
| **Conciseness** | Setiap kata menambah informasi | Hapus kalimat redundan, filler words |

### Urutan Penulisan yang Disarankan

1. **Method & Results** — paling stabil, tulis pertama
2. **Discussion** — interpretasi berdasarkan hasil
3. **Introduction** — frame sesuai temuan aktual
4. **Abstract & Conclusion** — terakhir

### Target Jumlah Kata

| Section | Target |
|---------|--------|
| Introduction | 500–700 |
| Related Work | 700–1000 |
| Method | 800–1200 |
| Results | 500–800 |
| Discussion | 600–900 |
| Conclusion | 200–400 |

### Jebakan Kognitif

1. "Lebih panjang = lebih lengkap" → conciseness lebih berharga
2. "Introduction harus ditulis pertama" → justru ditulis terakhir
3. "Jargon teknis = lebih ilmiah" → clarity lebih penting
4. "Discussion = ringkasan Results" → Discussion = interpretasi + konteks

---

## Template A.15 — Paper Structure Checklist

```
PAPER STRUCTURE CHECKLIST

Title   : ____________________
Target  : [ ] Jurnal  [ ] Konferensi  [ ] Laporan

Section Check:
  [ ] Abstract — masalah, metode, hasil utama, kontribusi (max 250 kata)
  [ ] Introduction — konteks → gap → RQ → kontribusi → struktur paper
  [ ] Related Work — concept-centric, gap positioning
  [ ] Method — reproducible: desain, variabel, metrik, setup, prosedur
  [ ] Results — tabel + grafik + observasi (tanpa interpretasi)
  [ ] Discussion — interpretasi, perbandingan, implikasi, limitation
  [ ] Conclusion — jawaban RQ, kontribusi, future work

Consistency Matrix:
  [ ] RQ di Introduction = RQ di Method = RQ di Conclusion
  [ ] Variabel di Method = variabel di Results
  [ ] Klaim di Discussion didukung data di Results
  [ ] Limitasi di Discussion di-address di Conclusion/Future Work

Writing Quality:
  [ ] Clarity — mudah dipahami tanpa re-read
  [ ] Precision — tidak ada istilah ambigu
  [ ] Conciseness — tidak ada kalimat redundan
```

---

## Latihan 1 — Paper Outline

Buat outline paper untuk riset Anda menggunakan struktur IMRAD.

| Section | Konten Utama (2-3 kalimat) | Target Kata |
|---------|---------------------------|------------|
| Abstract | Masalah subjektivitas penilaian soft skill siswa. Mengusulkan integrasi metode AHP-TOPSIS untuk penilaian yang objektif. Hasil pengujian menunjukkan CR ≤ 0.1 dan mampu merangking siswa dengan baik namun terjadi pelambatan komputasi pada sampel besar. | 200-250 |
| Introduction | Konteks: Pentingnya penilaian soft skill yang objektif. Gap: Metode konvensional sangat bias dan subjektif, belum ada DSS berbasis AHP-TOPSIS komprehensif untuk kasus ini. RQ: Bagaimana efektivitas integrasi AHP-TOPSIS dalam penilaian soft skill? | 500-700 |
| Related Work | Review metode MCDM pada DSS, batasan penggunaan TOPSIS tunggal, dan keunggulan integrasi pembobotan AHP dengan perankingan TOPSIS. | 700-1000 |
| Method | Desain sistem DSS, definisi 4 kriteria utama dan 13 indikator, perhitungan bobot prioritas (AHP), pengujian rasio konsistensi (CR), dan algoritma pemeringkatan (TOPSIS). | 800-1200 |
| Results | Evaluasi pada 140 sampel data siswa. Hasil uji konsistensi kriteria, tabel hasil akhir Cci, distribusi peringkat, dan pengujian waktu komputasi (baseline vs model) dalam n=5. | 500-800 |
| Discussion | Interpretasi objektivitas hasil, trade-off antara komprehensivitas kriteria dengan kompleksitas/waktu komputasi (boundary condition pada >1000 data). | 600-900 |
| Conclusion | AHP-TOPSIS efektif meningkatkan transparansi penilaian soft skill, namun memiliki limitasi skalabilitas data. Future work disarankan menggunakan arsitektur caching. | 200-400 |

---

## Latihan 2 — Consistency Matrix

Buat consistency matrix untuk memverifikasi internal consistency paper Anda.

|  | Intro | Method | Result | Discussion | Conclusion |
|--|-------|--------|--------|-----------|-----------|
| RQ1 (Efektivitas AHP-TOPSIS) | ✓ | ✓ | ✓ | ✓ | ✓ |
| RQ2 (Efisiensi Waktu Komputasi) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Metrik utama (CR & Waktu Komputasi) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Variabel IV (Kriteria Soft Skill) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Variabel DV (Nilai Peringkat Siswa) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Klaim/kontribusi (Objektivitas meningkat, komputasi berat) | ✓ | ✓ | ✓ | ✓ | ✓ |

**Isi setiap sel:** ✓ (ada & konsisten), ✗ (missing), ~ (ada tapi inkonsisten)

**Inkonsistensi yang ditemukan:**
> Semua bagian telah konsisten membahas metode, metrik, dan trade-off komputasional dari pendahuluan hingga kesimpulan.

**Tindakan perbaikan:**
> Menjaga alur argumen (Red Thread) agar tetap berfokus pada efektivitas objektivitas versus skalabilitas performa sistem pada semua bagian, memastikan setiap claim didukung angka dari results.

---

## Latihan 3 — Writing Quality Check

Ambil satu paragraf dari tulisan Anda (atau tulis paragraf baru) dan evaluasi kualitasnya.

**Paragraf asli:**
> Pengujian sistem menghasilkan nilai yang bagus dimana CR kurang dari 0.1 dan waktu untuk menghitung rank siswa sedikit lebih lama dibanding sistem yang lama tapi hasil urutan siswa cukup masuk akal.

| Kriteria | Evaluasi | Perbaikan |
|----------|---------|-----------|
| Clarity | Kalimat bertele-tele dan kurang profesional ("nilai yang bagus", "cukup masuk akal") | "Nilai Rasio Konsistensi (CR) ≤ 0.1 mengindikasikan pembobotan kriteria valid. Sistem mengurutkan alternatif secara akurat meskipun membutuhkan tambahan waktu komputasi." |
| Precision | Tidak menyebutkan angka spesifik atau signifikansi perbandingan komputasi | "Waktu komputasi meningkat sebesar 1.66 ms dibandingkan sistem baseline (p=0.008, d=4.89)." |
| Conciseness | Ada filler words ("dimana", "tapi") dan penggabungan gagasan yang terlalu panjang | Hapus kata hubung redundan, gabungkan fakta utama secara lugas. |

**Paragraf setelah perbaikan:**
> Pengujian metode AHP-TOPSIS menghasilkan nilai Rasio Konsistensi (CR) ≤ 0.1, mengindikasikan validitas pembobotan kriteria. Meskipun waktu komputasi meningkat sebesar 1.66 ms dibandingkan sistem baseline (p=0.008, d=4.89), metode ini secara akurat mampu mengklasifikasikan peringkat soft skill siswa.

---

## Refleksi

> Apa perbedaan antara menulis "tentang" riset dan menulis sebagai "argumen" riset? Bagaimana urutan penulisan (Method → Discussion → Introduction) mengubah kualitas tulisan?

> Menulis "tentang" riset sekadar melaporkan aktivitas kronologis (apa yang dilakukan dari awal ke akhir), sedangkan menulis sebagai "argumen" riset berarti menyusun alur logis dari masalah hingga kontribusi, meyakinkan pembaca bahwa metode dan hasil yang didapat benar-benar menjawab problem statement (Red Thread). Urutan penulisan (Method → Results → Discussion → Introduction) sangat membantu kualitas tulisan karena kita membangun argumen dari pondasi yang paling pasti (data dan metode), lalu memberikan interpretasi (discussion), dan akhirnya membingkai pendahuluan (introduction) agar sesuai persis dengan apa yang benar-benar ditemukan di lapangan. Hal ini menghindari terjadinya overclaiming dan inkonsistensi janji di awal dengan temuan riil di akhir.
