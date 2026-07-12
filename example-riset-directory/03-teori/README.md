# 03-teori

Arsitektur, desain, dan landasan teori instrumen penelitian — **Evaluasi Sensitivitas Algoritma Hibrida AHP-TOPSIS**.

## Isi

- Diagram arsitektur komponen benchmarking (Data Loader, Weight Manipulator, AHP-TOPSIS Engine, Metric Evaluator)
- Flowchart alur kalkulasi lengkap: dari input data → noise injection → korelasi Rank Spearman
- Skema struktur file CSV (input: `dataset_riil.csv`, `bobot_ahp.csv` — output: `experiment_log.csv`)
- Pemetaan ke implementasi modul skrip benchmarking CLI

## Berkas

- [arsitektur-dan-skema.md](arsitektur-dan-skema.md) — diagram Mermaid (arsitektur komponen, flowchart noise injection AHP-TOPSIS), dan pemetaan ke modul `data_loader`, `ahp_topsis`, `sensitivity_test`, `logger`.

## Acuan

- Proposal penelitian: [../../Proposal/Proposal_revisi.md](../../Proposal/Proposal_revisi.md)
- Matriks literatur: [../02-literatur/matriks-literatur.md](../02-literatur/matriks-literatur.md)
