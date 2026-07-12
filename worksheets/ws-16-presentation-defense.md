# WS-16: Presentation & Defense (UAS)

> **Bab 16 — Presentasi & Pertahanan Ilmiah**

---

## Ringkasan Materi

### Scientific Defense Model

```
Research Work → Presentation → Questioning → Defense → Evaluation → Acceptance
```

### Presentasi ≠ Ringkasan Paper

| Paper | Presentasi |
|-------|-----------|
| Dibaca (self-paced) | Didengar (presenter-paced) |
| Detail lengkap | Ide kunci + highlight |
| Tabel numerik detail | Grafik visual + angka kunci |
| Pembaca bisa re-read | Audiens dengar sekali |

**Prinsip:** Presentasi membutuhkan **reformulasi**, bukan kompresi. Medium berbeda = pendekatan berbeda.

### Claim-Evidence-Reasoning (CER)

Setiap jawaban defense harus memiliki:
1. **Claim** — Pernyataan yang dijawab
2. **Evidence** — Data/fakta pendukung
3. **Reasoning** — Logika yang menghubungkan evidence ke claim

**Contoh:**
| Pertanyaan | Bad Answer | Good Answer (CER) |
|-----------|-----------|-------------------|
| "Kenapa hanya 3 dataset?" | "Tiga sudah cukup" | "3 dataset mewakili variasi: small-clean, medium-clean, medium-noisy [E]. Generalisasi perlu validasi lanjut — listed as limitation [R]" |
| "Hasil DS-3 menurun?" | "Itu outlier" | "Ya, karena distribusi heavy-tail melanggar asumsi Gaussian [E]. Ini menunjukkan boundary condition metode [R]" |
| "Effect size?" | "p=0.003, jadi signifikan" | "Cohen's d=1.2 (large effect) [E] — bukan hanya signifikan tapi substansial [R]" |

### Slide Design — One Slide, One Message

**Optimal 9-Slide Plan (15 menit):**

| # | Slide | Waktu | Pesan |
|---|-------|-------|-------|
| 1 | Title + context | 1 min | Apa ini tentang apa |
| 2 | Problem + motivation | 2 min | Mengapa penting |
| 3 | Gap + RQ | 1.5 min | Apa yang belum terjawab |
| 4 | Method overview | 2 min | Bagaimana dijawab (diagram) |
| 5 | Key result — tabel | 2 min | Temuan utama |
| 6 | Key result — grafik | 2 min | Pola visual |
| 7 | Interpretation + failure | 2 min | Apa artinya |
| 8 | Limitation + future | 1.5 min | Batasan & arah |
| 9 | Conclusion + contribution | 1 min | Closing message |

### Anticipatory Defense

Prediksi pertanyaan berdasarkan kategori:

| Kategori | Contoh Pertanyaan |
|---------|------------------|
| Problem | "Mengapa masalah ini penting?" |
| Gap | "Bagaimana dengan studi X yang sudah menjawab ini?" |
| Method | "Mengapa metode ini, bukan Y?" |
| Results | "Bagaimana menjelaskan anomali di DS-3?" |
| Generalization | "Apakah bisa diterapkan di domain lain?" |

### Tiga Prinsip Jawaban

1. **Direct** — Jawab dulu, elaborasi kemudian
2. **Data-based** — Tunjuk evidence spesifik
3. **Honest** — Akui limitasi jika memang ada

### Jebakan Kognitif

1. "Presentasi = semua yang ada di paper" → terlalu padat
2. "Slide cantik = presentasi bagus" → konten > estetika
3. "Tidak bisa jawab = gagal" → "I don't know, but..." menunjukkan kejujuran
4. "Tidak perlu latihan — saya paham riset saya" → latihan = menemukan celah

---

## Template A.16 — Defense Preparation Sheet

```
DEFENSE PREPARATION

Slide Deck Plan:
  Total slides   : ____ (target: 10-12 konten + title/closing)
  Time per slide : ~2 min
  Total time     : ____ menit

Slide Outline:
| # | Pesan Utama | Visual | Waktu |
|---|-------------|--------|-------|
| 1 | Title       |        | 30s   |
| 2 | Problem     |        | 2min  |
| 3 | Gap + RQ    |        | 2min  |
| ..|             |        |       |

Anticipatory Defense Matrix:
| Kategori | Pertanyaan Potensial | Jawaban (CER) |
|----------|---------------------|---------------|
| Problem  |                     |               |
| Gap      |                     |               |
| Method   |                     |               |
| Results  |                     |               |
| Generalization |               |               |

Latihan:
  Latihan 1: [tanggal] — [catatan timing & feedback]
  Latihan 2: [tanggal] — [catatan timing & feedback]
  Latihan 3: [tanggal] — [catatan timing & feedback]
```

---

## Latihan 1 — Slide Outline

Rencanakan presentasi 15 menit untuk riset Anda.

| # | Pesan Utama | Visual yang Digunakan | Waktu |
|---|-------------|----------------------|-------|
| 1 | Judul + konteks — Evaluasi Soft Skill Siswa | Title slide, ilustrasi sistem DSS | 1 min |
| 2 | Problem — Penilaian kualitatif yang bias dan subjektif | Bar chart: inkonsistensi penilaian antar guru pada siswa yang sama | 2 min |
| 3 | Gap + RQ — Belum ada DSS AHP-TOPSIS komprehensif | Tabel gap literatur metode MCDM | 1.5 min |
| 4 | Method overview — Integrasi AHP-TOPSIS | Diagram alir proses (AHP untuk bobot, TOPSIS untuk rank) | 2 min |
| 5 | Key result — Validitas & Objektivitas | Tabel nilai CR dan sampel hasil pemeringkatan siswa | 2 min |
| 6 | Key result — Waktu Komputasi | Grafik bar perbandingan runtime baseline vs model | 2 min |
| 7 | Interpretation + failure — Trade-off komputasi | Analisis boundary condition sistem pada volume data >1000 | 2 min |
| 8 | Limitation + future — Skalabilitas sistem | Poin-poin batasan N sampel dan ide metode caching AHP | 1.5 min |
| 9 | Conclusion + contribution | Pesan penutup: objektivitas vs efisiensi skala | 1 min |

**Total waktu estimasi:** 15 menit

---

## Latihan 2 — Anticipatory Defense

Prediksi 5 pertanyaan yang mungkin diajukan penguji, lalu siapkan jawaban CER.

| # | Kategori | Pertanyaan | Claim | Evidence | Reasoning |
|---|----------|-----------|-------|----------|-----------|
| 1 | Problem | Mengapa fokus pada evaluasi soft skill, bukan akademik? | Evaluasi akademik sudah punya standar kuantitatif baku (nilai ujian) | Kurikulum merdeka menuntut evaluasi karakter, tapi instrumen guru di lapangan masih sangat subjektif | Gap standardisasi justru ada di penilaian non-akademik |
| 2 | Method | Mengapa menggabungkan AHP dan TOPSIS? Kenapa tidak AHP saja? | AHP unggul di pembobotan kriteria, TOPSIS efisien di perankingan jumlah alternatif banyak | AHP sulit menghitung konsistensi jika membandingkan 140 siswa sekaligus | Gabungan keduanya saling menutupi kelemahan masing-masing metode |
| 3 | Results | Apakah perlambatan komputasi 1.66 ms menjadi masalah krusial? | Secara praktis tidak masalah untuk data kecil, namun menjadi boundary condition skalabilitas | Lonjakan effect size sangat besar (d=4.89). Simulasi ekstrapolasi ke 10.000 data memakan waktu 14.2 detik | Sistem ini andal di skala institusi namun butuh optimasi arsitektur jika menjadi platform terpusat |
| 4 | Generalization | Bisakah kriteria soft skill ini diterapkan di sekolah lain? | Kurikulum bisa sama, tapi pembobotan prioritas (AHP) bisa berbeda antar institusi | Matriks penilaian perbandingan dilakukan oleh 3 pakar lokal dari sekolah yang diteliti | Algoritma dan DSS-nya bisa digeneralisasi, tapi isi indikator dan matriks bobotnya bersifat kontekstual pada masing-masing institusi |
| 5 | Method | Bagaimana memastikan subjektivitas pakar di awal (AHP) tidak merusak validitas? | Penggunaan metrik Consistency Ratio (CR) dari teori AHP | Kami menetapkan CR ≤ 0.1 sesuai standar Saaty. Jika > 0.1, pakar wajib merevisi matriksnya | Algoritma ini memiliki filter logis untuk mendeteksi penilaian pakar yang tidak konsisten, sehingga subjektivitas tetap terukur |

---

## Latihan 3 — Simulasi Q&A

Minta teman/kolega mengajukan 3 pertanyaan tentang riset Anda. Catat pertanyaan dan evaluasi jawaban Anda.

| # | Pertanyaan | Jawaban Saya | Evaluasi |
|---|-----------|-------------|---------|
| 1 | "Kenapa repot-repot pakai AHP-TOPSIS jika guru BK sudah biasa menilai kualitatif?" | "Metode kualitatif rentan terhadap bias individu dan inkonsisten antar guru. Sistem ini memberikan standardisasi kuantitatif (CR ≤ 0.1) sehingga data profil siswa lebih objektif." | [✓] Direct [✓] Data-based [✓] Honest |
| 2 | "Bagaimana memastikan pengisi matriks AHP benar-benar pakar?" | "Kami memilih 3 representasi stakeholder utama (Kepala Madrasah, Waka Kurikulum, Guru BK). Namun, subjektivitas awal pakar tetap ada, ini adalah batasan metode MCDM yang kami mitigasi dengan uji rasio konsistensi." | [✓] Direct [✓] Data-based [✓] Honest |
| 3 | "Apakah sistem ini akan menggantikan peran observasi guru?" | "Tidak, sistem ini adalah Decision Support System (DSS). Keputusan final tetap ada pada guru. Output sistem berfungsi sebagai metrik referensi (second opinion) untuk memvalidasi feeling observasi guru." | [✓] Direct [ ] Data-based [✓] Honest |

**Pertanyaan yang paling sulit dijawab:**
> Bagaimana memastikan subjektivitas di awal (saat input matriks perbandingan berpasangan oleh pakar) tidak merusak "klaim objektivitas" akhir dari output pemeringkatan sistem ini?

**Apa yang perlu disiapkan lebih baik:**
> Memperkuat argumen pemahaman di bagian validasi pakar dan peran metrik konsistensi (CR). Harus mampu menjelaskan bahwa sistem tidak menghilangkan 100% subjektivitas, tetapi mengubah subjektivitas yang bias menjadi preferensi kriteria yang konsisten, matematis, dan terukur.

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-16 — dari paradigma riset hingga presentasi — bagian mana yang paling mengubah cara Anda berpikir tentang riset? Apa satu hal yang akan selalu Anda terapkan di riset berikutnya?

**Insight terbesar:**
> Bahwa riset adalah satu kesatuan argumen logis yang mengalir ("Red Thread") dari rumusan masalah hingga sidang presentasi. Kegagalan (hipotesis tidak terbukti atau metode memiliki kelemahan) bukanlah "aib" yang harus disembunyikan. Sebaliknya, melalui Failure Analysis, mengetahui batasan operasional (boundary condition) dari suatu algoritma adalah sumbangsih ilmiah yang sangat krusial. Selain itu, cara presentasi riset sangat jauh berbeda dengan membaca paper; presentasi bukan tentang kompresi teks, melainkan menyeleksi dan membingkai ide sentral agar mudah diserap oleh audiens secara oral.

**Yang akan selalu diterapkan:**
> Saya akan selalu menulis draft paper dimulai dari Method & Results (bukan Introduction) untuk menjaga kejujuran ilmiah, serta mempraktikkan framework Claim-Evidence-Reasoning (CER) setiap kali mempertahankan atau menulis argumen agar terstruktur dengan data, alih-alih sekadar opini.
