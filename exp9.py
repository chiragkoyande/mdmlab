"""
Experiment No. 9
Data Transfer Using Bluetooth and Analysis of Performance
"""

import matplotlib
matplotlib.use('Agg')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data: Payload size (KB) vs Transfer Time (seconds) and Packet Loss (%)
payload_kb = np.array([10, 50, 100, 250, 500, 1000])
transfer_time_sec = np.array([0.18, 0.72, 1.35, 3.10, 6.05, 12.80])
packet_loss_pct = np.array([0.0, 0.0, 0.2, 0.5, 1.1, 2.4])

# Throughput calculation in kbps
throughput_kbps = (payload_kb * 8) / transfer_time_sec
avg_latency_ms = (transfer_time_sec / payload_kb) * 1000

print("=" * 60)
print("     EXPERIMENT 9: BLUETOOTH DATA TRANSFER ANALYSIS")
print("=" * 60)
for i in range(len(payload_kb)):
    print(f"Payload: {payload_kb[i]:4d} KB | Time: {transfer_time_sec[i]:5.2f}s | "
          f"Throughput: {throughput_kbps[i]:6.2f} kbps | Loss: {packet_loss_pct[i]:3.1f}%")

# Observation Table
print("\nObservation Table:")
obs_df = pd.DataFrame({
    'Payload Size (KB)': payload_kb,
    'Transfer Time (s)': transfer_time_sec,
    'Calculated Throughput (kbps)': np.round(throughput_kbps, 2),
    'Packet Loss (%)': packet_loss_pct
})
print(obs_df.to_string(index=False))

# Plotting Performance Curves
fig, ax1 = plt.subplots(figsize=(9, 4.5))

color = 'tab:blue'
ax1.set_xlabel('Payload Size (KB)', fontweight='bold')
ax1.set_ylabel('Throughput (kbps)', color=color, fontweight='bold')
ax1.plot(payload_kb, throughput_kbps, color=color, marker='o', linewidth=2, label='Throughput (kbps)')
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True, linestyle='--', alpha=0.6)

ax2 = ax1.twinx()  
color = 'tab:red'
ax2.set_ylabel('Packet Loss (%)', color=color, fontweight='bold')
ax2.plot(payload_kb, packet_loss_pct, color=color, marker='s', linestyle='--', linewidth=2, label='Packet Loss (%)')
ax2.tick_params(axis='y', labelcolor=color)

plt.title("Bluetooth Data Transfer Performance vs Payload Scaling", fontsize=12, fontweight='bold')
fig.tight_layout()
plt.savefig('/home/chiragk/mdmlab/outputs/exp9_bluetooth_performance.png', dpi=150, bbox_inches='tight')
print("\nGraph saved: exp9_bluetooth_performance.png")
