# Wireless and Mobile Communication Lab (MDM Lab)
## Experiments 3 to 10: Practical Execution Record & Analysis

This repository contains the Python simulation scripts, live network measurement programs, generated performance plots, observation datasets, and final Google Colab-style execution record PDF for the **Wireless and Mobile Communication Laboratory** (Experiments 3 to 10).

---

### Repository Structure

```
.
├── README.md
├── .gitignore
├── exp3.py                                                    # Experiment 3: Frequency Reuse Simulation
├── exp4.py                                                    # Experiment 4: Wi-Fi RSSI Degradation & Channel Mapping
├── exp5.py                                                    # Experiment 5: Wi-Fi RSSI vs. Distance
├── exp6.py                                                    # Experiment 6: 2.4 GHz Wi-Fi Spectral Overlap & Interference
├── exp7.py                                                    # Experiment 7: Network Latency, Jitter & Throughput Benchmarking
├── exp8.py                                                    # Experiment 8: Bluetooth Range & RSSI Log-Distance Fitting
├── exp9.py                                                    # Experiment 9: Bluetooth Data Transfer & Payload Scaling Analysis
├── exp10.py                                                   # Experiment 10: Indoor RF Obstacle Attenuation Analysis
├── generate_colab_pdf.py                                      # Colab-style HTML/PDF compiler (WeasyPrint)
├── generate_pdf.py                                            # Initial PDF compiler
├── outputs/                                                   # Generated high-resolution experiment figures
│   ├── exp3_frequency_reuse.png
│   ├── exp4_rssi_degradation.png
│   ├── exp4_channel_interference.png
│   ├── exp5_rssi_vs_distance.png
│   ├── exp6_channel_interference.png
│   ├── exp7_rtt.png
│   ├── exp7_jitter.png
│   ├── exp7_throughput.png
│   ├── exp8_bluetooth_rssi.png
│   ├── exp9_bluetooth_performance.png
│   └── exp10_obstacle_attenuation.png
├── Wireless_Mobile_Communication_Experiments_3_to_10_COLAB_OUTPUT.html # Rendered notebook HTML
├── Wireless_Mobile_Communication_Experiments_3_to_10_COLAB_OUTPUT.pdf  # Final 13-Page Colab-Style PDF Record
└── WMC_Lab_Experiments_3_to_10_Output.pdf                     # Consolidated lab output documentation
```

---

### Experiments Overview

| Exp No. | Experiment Title | Key Techniques & Models | Generated Figures |
| :---: | :--- | :--- | :--- |
| **3** | Demonstration of Frequency Reuse Concept in Cellular Systems | Hexagonal geometry, co-channel distance $D = \sqrt{3N}R$, $N=7$ cluster allocation | Cellular cluster reuse plot |
| **4** | Simulation of Wi-Fi Network Scanning, RSSI Degradation, and Channel Mapping | Log-distance path loss, log-normal shadow fading, 2.4 GHz channel occupancy | RSSI degradation curve, 2.4 GHz channel congestion bar chart |
| **5** | Wi-Fi Signal Strength (RSSI) vs Distance | Free space & indoor distance attenuation from AP | Wi-Fi RSSI vs distance plot |
| **6** | Analysis of 2.4 GHz Wi-Fi Channel Overlap and Interference | Gaussian spectral bell curves (2400–2484 MHz), Adjacent-Channel (ACI) & Co-Channel (CCI) interference | 2.4 GHz Wi-Fi spectral interference model |
| **7** | Measurement and Analysis of Network Throughput, Latency, and Jitter | Live ICMP ping (RTT variance, jitter) + Speedtest API throughput benchmarking | ICMP RTT variation, packet-to-packet jitter, network throughput chart |
| **8** | Study of Bluetooth Communication Using Mobile Devices | Least-squares log-distance model fitting, path loss exponent $n$, reference power $A$ | Bluetooth range testing curve (RSSI vs distance) |
| **9** | Data Transfer Using Bluetooth and Analysis of Performance | RFCOMM / SPP payload scaling, effective throughput (kbps), frame drop percentage | Dual-axis throughput vs packet loss curve |
| **10** | Study of Path Loss in an Indoor Environment (RSSI vs. Obstacles) | Floor & Obstacle Attenuation Factor (FAF), concrete/glass/wood penetration loss | Indoor obstacle signal attenuation bar chart |

---

### Requirements & Setup

Install the required Python dependencies:

```bash
pip install numpy pandas matplotlib weasyprint speedtest-cli pypdf
```

To re-run any individual experiment:
```bash
python3 exp3.py
python3 exp7.py
```

To regenerate the Colab-style PDF:
```bash
python3 generate_colab_pdf.py
```

---

### Deliverable

The completed, fully verified lab execution record is available in:
**`Wireless_Mobile_Communication_Experiments_3_to_10_COLAB_OUTPUT.pdf`** (13 pages, A4 Portrait with continuous box border, cell-by-cell Jupyter execution flow, observation tables, and figures).
