"""
Experiment No. 5
Wi-Fi Signal Strength vs Distance
"""

import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Distance from Wi-Fi router in metres
distance = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Enter measured RSSI values in dBm (SAMPLE DATA from manual)
rssi = np.array([
    -40,
    -45,
    -49,
    -53,
    -57,
    -61,
    -65,
    -68,
    -72,
    -75
])

print("EXPERIMENT 5 — Wi-Fi Signal Strength vs Distance")
print("(SAMPLE DATA as provided in the manual)")
print()
print(f"{'Distance (m)':<15} {'RSSI (dBm)':<15}")
print("-" * 30)
for d, r in zip(distance, rssi):
    print(f"{d:<15} {r:<15}")

# Plot RSSI versus distance
plt.figure(figsize=(9, 6))
plt.plot(
    distance,
    rssi,
    marker='o',
    linewidth=2
)
plt.xlabel("Distance from Wi-Fi Router (m)")
plt.ylabel("Received Signal Strength (dBm)")
plt.title("Wi-Fi Signal Strength vs Distance")

plt.grid(True)
plt.xticks(distance)

plt.savefig('/home/chiragk/mdmlab/outputs/exp5_rssi_vs_distance.png', dpi=150, bbox_inches='tight')
print("\nGraph saved: exp5_rssi_vs_distance.png")
