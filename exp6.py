"""
Experiment No. 6
Analysis of 2.4 GHz Wi-Fi Channel Overlap and Interference
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def generate_channel_wave(channel, rssi, num_points=1000):
    """
    Generates a bell curve representing a 20 MHz wide 2.4 GHz Wi-Fi channel spectrum.
    """
    # 2.4 GHz Channel Center Frequencies in MHz
    center_freq = 2412 + 5 * (channel - 1)
    bandwidth = 20  # 20 MHz standard channel bandwidth
    
    # Generate frequency array covering the 2.4 GHz band
    freqs = np.linspace(2400, 2484, num_points)
    
    # Gaussian bell curve model for signal spectral mask
    sigma = bandwidth / 2.355  # Full Width at Half Maximum (FWHM) approximation
    signal = rssi + 100 * np.exp(-((freqs - center_freq) ** 2) / (2 * sigma ** 2))
    
    # Set floor noise level outside signal peak
    signal = np.clip(signal, -100, rssi)
    return freqs, signal

def analyze_interference():
    # Sample scanned Wi-Fi networks data (SSID, Channel, RSSI in dBm)
    wifi_data = [
        {"SSID": "Home_WiFi (Ch 1)", "channel": 1, "rssi": -45},
        {"SSID": "Neighbor_A (Ch 2 - Overlapping)", "channel": 2, "rssi": -68},
        {"SSID": "Office_Guest (Ch 6)", "channel": 6, "rssi": -55},
        {"SSID": "Neighbor_B (Ch 6 - Co-Channel)", "channel": 6, "rssi": -72},
        {"SSID": "Tech_Lab (Ch 11)", "channel": 11, "rssi": -50},
        {"SSID": "Router_Old (Ch 9 - Overlapping)", "channel": 9, "rssi": -78},
    ]

    df = pd.DataFrame(wifi_data)
    
    print("EXPERIMENT 6 — Wi-Fi Channel Interference Analysis")
    print("\nScanned Wi-Fi Networks:")
    print(df.to_string(index=False))
    
    # Setup plot
    plt.figure(figsize=(12, 6))
    freqs = np.linspace(2400, 2484, 1000)
    
    for idx, row in df.iterrows():
        _, signal = generate_channel_wave(row["channel"], row["rssi"])
        plt.plot(freqs, signal, label=f"{row['SSID']} | RSSI: {row['rssi']} dBm", linewidth=2)
        plt.fill_between(freqs, -100, signal, alpha=0.2)

    # Label channels on top x-axis
    ch_centers = [2412 + 5 * (ch - 1) for ch in range(1, 14)]
    plt.xticks(ch_centers, [f"Ch {ch}\n({2412 + 5*(ch-1)} MHz)" for ch in range(1, 14)], rotation=45)
    
    plt.title("Analysis of 2.4 GHz Wi-Fi Channel Overlap and Interference", fontsize=14, fontweight='bold')
    plt.xlabel("Frequency / Channel", fontsize=11)
    plt.ylabel("Signal Strength / RSSI (dBm)", fontsize=11)
    plt.ylim(-100, -30)
    plt.xlim(2400, 2484)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(loc="upper right", fontsize=9)
    plt.tight_layout()
    
    plt.savefig('/home/chiragk/mdmlab/outputs/exp6_channel_interference.png', dpi=150, bbox_inches='tight')
    print("\nGraph saved: exp6_channel_interference.png")

if __name__ == "__main__":
    analyze_interference()
