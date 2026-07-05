import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Setup paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(base_dir, '..', '..'))
    out_dir = os.path.join(project_root, '06-output', 'plots')
    log_file = os.path.join(project_root, '06-output', 'logs', 'benchmark_log.csv')
    
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    
    if not os.path.exists(log_file):
        print(f"Error: {log_file} tidak ditemukan.")
        return
        
    # Read data
    df = pd.read_csv(log_file)
    
    # Configure plotting style
    sns.set_theme(style="whitegrid")
    plt.rcParams.update({'font.size': 12})
    
    # 1. Delta W vs Spearman Rho
    plt.figure(figsize=(8, 6))
    sns.lineplot(
        data=df, x='delta_w_pct', y='spearman_rho', 
        hue='scenario', style='scenario', 
        markers=True, dashes=False
    )
    plt.title('Dampak Perturbasi Bobot thd Spearman Rho')
    plt.xlabel('Perturbasi Bobot (ΔW %)')
    plt.ylabel('Spearman Rho (Konsistensi)')
    plt.ylim(0.8, 1.05)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, 'fig_spearman_rho.png'))
    plt.close()
    
    # 2. Delta W vs Kendall's Tau
    plt.figure(figsize=(8, 6))
    sns.lineplot(
        data=df, x='delta_w_pct', y='kendall_tau', 
        hue='scenario', style='scenario', 
        markers=True, dashes=False
    )
    plt.title('Dampak Perturbasi Bobot thd Kendall\'s Tau')
    plt.xlabel('Perturbasi Bobot (ΔW %)')
    plt.ylabel('Kendall\'s Tau (Stabilitas Rank)')
    plt.ylim(0.7, 1.05)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, 'fig_kendall_tau.png'))
    plt.close()
    
    # 3. Delta W vs Runtime (with error bars)
    plt.figure(figsize=(8, 6))
    # seaborn lineplot otomatis menghitung confidence interval (error bar/band) untuk multiple seeds
    sns.lineplot(
        data=df, x='delta_w_pct', y='runtime_ms', 
        hue='scenario', style='scenario', 
        markers=True, dashes=False, err_style='bars'
    )
    plt.title('Fluktuasi Runtime Berdasarkan Skenario Data')
    plt.xlabel('Perturbasi Bobot (ΔW %)')
    plt.ylabel('Runtime (ms)')
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, 'fig_runtime.png'))
    plt.close()
    
    print(f"Berhasil membuat grafik line chart di folder: {out_dir}")

if __name__ == "__main__":
    main()
