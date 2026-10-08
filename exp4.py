"""
Experiment No. 4
Simulation of Wi-Fi Network Scanning, RSSI Degradation, and Channel Mapping
"""

import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Set random seed for consistent and reproducible stochastic simulation
np.random.seed(42)
print("Google Colab Environment Initialized Successfully.")

# Model Parameters
d0 = 1.0                  # Reference distance in meters
rssi_d0 = -30.0           # Baseline RSSI at reference distance 1m (dBm)
n_indoor = 2.8            # Indoor path loss exponent accounting for walls/partitions
distances = np.linspace(1, 50, 100) # Client distance vector from 1m to 50m

# Calculate RSSI values with shadow fading noise
shadow_fading = np.random.normal(0, 2.5, len(distances))
rssi_values = rssi_d0 - (10 * n_indoor * np.log10(distances / d0)) - shadow_fading

# Create a sample summary table for students
sample_indices = np.linspace(0, len(distances)-1, 6, dtype=int)
df_simulation = pd.DataFrame({
    'Distance (m)': np.round(distances[sample_indices], 1),
    'Simulated RSSI (dBm)': np.round(rssi_values[sample_indices], 2),
    'Connection Status': ['Excellent' if val > -50 else 'Good' if val > -70 else 'Fair' if val > -80 else 'Poor' for val in rssi_values[sample_indices]]
})

print("--- Table: Distance vs. RSSI Degradation ---")
print(df_simulation.to_string(index=False))

# Plotting RSSI Degradation Curve
plt.figure(figsize=(10, 5))
plt.plot(distances, rssi_values, label='Simulated RSSI Curve', color='blue', linewidth=2)
plt.axhline(y=-75, color='red', linestyle='--', label='Poor Connection Threshold (-75 dBm)')
plt.title('Wi-Fi RSSI Degradation over Distance (Log-Distance Path Loss Model)')
plt.xlabel('Distance from Access Point (meters)')
plt.ylabel('Received Signal Strength Indicator (dBm)')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.savefig('/home/chiragk/mdmlab/outputs/exp4_rssi_degradation.png', dpi=150, bbox_inches='tight')
print("\nRSSI Degradation graph saved: exp4_rssi_degradation.png")

# Define 2.4 GHz channels 1 through 13
channels = np.arange(1, 14)
congestion_levels = np.zeros(len(channels))

# Assign signal activity / power peaks across channels
congestion_levels[0] = 95   # Channel 1 (AP Alpha - Non-overlapping)
congestion_levels[2] = 65   # Channel 3 (Overlapping neighbor router - causes interference)
congestion_levels[5] = 90   # Channel 6 (AP Beta - Non-overlapping)
congestion_levels[7] = 40   # Channel 8 (Weak overlapping interference)
congestion_levels[10] = 85  # Channel 11 (AP Gamma - Non-overlapping)

plt.figure(figsize=(10, 4))
bars = plt.bar(channels, congestion_levels, 
               color=['forestgreen' if c in [1, 6, 11] else 'darkorange' for c in channels], 
               edgecolor='black', width=0.6)

plt.title('2.4 GHz Wi-Fi Channel Mapping and Interference Spectrum')
plt.xlabel('Wi-Fi Channel Number')
plt.ylabel('Spectrum Utilization / Activity Level')
plt.xticks(channels)
plt.grid(axis='y', linestyle=':', alpha=0.7)

# Custom Legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='forestgreen', edgecolor='black', label='Non-Overlapping Channels (1, 6, 11) - Optimal'),
    Patch(facecolor='darkorange', edgecolor='black', label='Overlapping Channels - Prone to Interference')
]
plt.legend(handles=legend_elements, loc='upper right')
plt.savefig('/home/chiragk/mdmlab/outputs/exp4_channel_interference.png', dpi=150, bbox_inches='tight')
print("Channel Interference graph saved: exp4_channel_interference.png")
