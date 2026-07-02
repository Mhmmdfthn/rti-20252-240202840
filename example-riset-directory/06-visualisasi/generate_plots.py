import json
import os
import pandas as pd
import matplotlib.pyplot as plt

# File paths
log_file = r"d:\Project\rti-20252-240202840\example-riset-directory\05-kode\experiment\results\run_log.jsonl"
output_dir = r"d:\Project\rti-20252-240202840\example-riset-directory\06-visualisasi"

# Load data
data = []
with open(log_file, "r") as f:
    for line in f:
        line = line.strip()
        if line:
            data.append(json.loads(line))

df = pd.DataFrame(data)

# Ensure output dir exists
os.makedirs(output_dir, exist_ok=True)

# Helper function to plot lines by scenario
def plot_by_scenario(df, x_col, y_col, title, ylabel, filename):
    plt.figure(figsize=(10, 6))
    for scenario in df['scenario'].unique():
        subset = df[df['scenario'] == scenario]
        # Calculate mean for each delta_w_pct
        mean_data = subset.groupby(x_col)[y_col].mean().reset_index()
        plt.plot(mean_data[x_col], mean_data[y_col], marker='o', label=scenario)
        
    plt.title(title)
    plt.xlabel("Delta Weight (%)")
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, filename), dpi=300)
    plt.close()

# Plot 1: Spearman's Rho vs Delta W %
plot_by_scenario(df, "delta_w_pct", "spearman_rho", "Spearman's Rho vs Delta Weight (%)", "Spearman's Rho", "spearman_rho_vs_delta_w.png")

# Plot 2: Kendall's Tau vs Delta W %
plot_by_scenario(df, "delta_w_pct", "kendall_tau", "Kendall's Tau vs Delta Weight (%)", "Kendall's Tau", "kendall_tau_vs_delta_w.png")

# Plot 3: Runtime vs Delta W %
plot_by_scenario(df, "delta_w_pct", "runtime_ms", "Runtime (ms) vs Delta Weight (%)", "Runtime (ms)", "runtime_vs_delta_w.png")

print("Visualizations successfully generated in", output_dir)

