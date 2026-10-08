"""
Experiment No. 10
Study of Path Loss in an Indoor Environment (RSSI vs. Obstacles)
"""

import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Obstacle Scenario Data at 5m Distance
obstacles = ['Free Space (LOS)', 'Glass Window', 'Wooden Door', 'Single Concrete Wall', 'Double Wall']
rssi_values = np.array([-52, -55, -58, -67, -78])  # dBm
attenuation_db = np.abs(rssi_values - rssi_values[0])  # dB attenuation relative to LOS

print("EXPERIMENT 10 — Indoor Path Loss / Obstacle Analysis (at 5m)")
print()
print(f"{'Obstacle':<25} {'RSSI (dBm)':<15} {'Attenuation (dB)':<20}")
print("-" * 60)
for o, r, a in zip(obstacles, rssi_values, attenuation_db):
    print(f"{o:<25} {r:<15} {a:<20}")

# Plotting Obstacle Impact
plt.figure(figsize=(9, 4.5))
bars = plt.bar(obstacles, attenuation_db, color=['#2b5c8f', '#4682b4', '#d9822b', '#c0392b', '#7b241c'])
plt.ylabel('Signal Attenuation (dB)', fontweight='bold')
plt.title('Indoor Signal Attenuation Caused by Various Physical Obstacles (at 5m)', fontweight='bold')
plt.grid(axis='y', linestyle='--', alpha=0.6)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.5, f"{yval:.1f} dB", ha='center', va='bottom', fontweight='bold')

plt.ylim(0, 32)
plt.tight_layout()
plt.savefig('/home/chiragk/mdmlab/outputs/exp10_obstacle_attenuation.png', dpi=150, bbox_inches='tight')
print("\nGraph saved: exp10_obstacle_attenuation.png")
