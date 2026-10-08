"""
Experiment No. 8
Bluetooth Communication & Range Testing (RSSI vs Distance)
"""

import matplotlib
matplotlib.use('Agg')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Distance in meters vs RSSI in dBm
distances = np.array([1, 2, 3, 5, 8, 10, 12, 15, 18, 20])
rssi_measured = np.array([-42, -50, -56, -64, -72, -77, -81, -86, -91, -95])

log_d = np.log10(distances)
slope, intercept = np.polyfit(log_d, rssi_measured, 1)
n_path_loss = -slope / 10.0
A_ref = intercept

print("EXPERIMENT 8 — Bluetooth RSSI vs Distance")
print()
print(f"Reference Signal at 1m (A)  : {A_ref:.2f} dBm")
print(f"Path Loss Exponent (n)      : {n_path_loss:.2f}")
print()

# Print RSSI data
print(f"{'Distance (m)':<15} {'RSSI (dBm)':<15}")
print("-" * 30)
for d, r in zip(distances, rssi_measured):
    print(f"{d:<15} {r:<15}")

d_model = np.linspace(1, 25, 200)
rssi_model = A_ref - 10 * n_path_loss * np.log10(d_model)

plt.figure(figsize=(10, 5))
plt.plot(distances, rssi_measured, 'ro', label='Measured RSSI')
plt.plot(d_model, rssi_model, 'b--', label=f'Log-Distance Model (n={n_path_loss:.2f})')
plt.axhline(-95, color='gray', linestyle=':', label='Sensitivity Limit (-95 dBm)')
plt.title("Bluetooth Range Testing (RSSI vs Distance)", fontsize=13, fontweight='bold')
plt.xlabel("Distance (Meters)")
plt.ylabel("RSSI (dBm)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.savefig('/home/chiragk/mdmlab/outputs/exp8_bluetooth_rssi.png', dpi=150, bbox_inches='tight')
print("\nGraph saved: exp8_bluetooth_rssi.png")
