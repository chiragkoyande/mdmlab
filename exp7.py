"""
Experiment No. 7
Measurement and Analysis of Network Throughput, Latency, and Jitter
"""

import matplotlib
matplotlib.use('Agg')
import subprocess
import time
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def measure_ping(host="8.8.8.8", count=15, interval=0.2):
    """
    Measures RTT, packet loss and jitter using ICMP Ping.
    """

    print("=" * 60)
    print("LATENCY AND PACKET LOSS MEASUREMENT")
    print("=" * 60)

    print(f"Target Host : {host}")
    print(f"Packets     : {count}")
    print()

    rtt_list = []
    packets_sent = count

    for i in range(count):

        try:
            result = subprocess.run(
                ["ping", "-c", "1", "-W", "2", host],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=4
            )

            output = result.stdout

            # Extract RTT from ping output
            match = re.search(
                r"time[=<]([\d.]+)\s*ms",
                output
            )

            if match:
                rtt = float(match.group(1))
                rtt_list.append(rtt)

                print(
                    f"Packet {i+1:02d} : "
                    f"RTT = {rtt:.2f} ms"
                )
            else:
                print(
                    f"Packet {i+1:02d} : "
                    f"Request timed out"
                )

        except Exception:
            print(
                f"Packet {i+1:02d} : "
                f"Measurement error"
            )

        time.sleep(interval)

    packets_received = len(rtt_list)

    if packets_received == 0:
        raise RuntimeError(
            "No ICMP replies were received. "
            "Check the Internet connection or try another host."
        )

    packet_loss = (
        (packets_sent - packets_received)
        / packets_sent
    ) * 100

    min_rtt = np.min(rtt_list)
    max_rtt = np.max(rtt_list)
    avg_rtt = np.mean(rtt_list)
    median_rtt = np.median(rtt_list)
    std_rtt = np.std(rtt_list)
    p95_rtt = np.percentile(rtt_list, 95)

    if len(rtt_list) > 1:
        jitter_values = np.abs(np.diff(rtt_list))
        avg_jitter = np.mean(jitter_values)
        max_jitter = np.max(jitter_values)
    else:
        jitter_values = []
        avg_jitter = 0
        max_jitter = 0

    results = {
        "Packets Sent": packets_sent,
        "Packets Received": packets_received,
        "Packet Loss (%)": packet_loss,
        "Minimum RTT (ms)": min_rtt,
        "Maximum RTT (ms)": max_rtt,
        "Average RTT (ms)": avg_rtt,
        "Median RTT (ms)": median_rtt,
        "RTT Standard Deviation (ms)": std_rtt,
        "95th Percentile RTT (ms)": p95_rtt,
        "Average Jitter (ms)": avg_jitter,
        "Maximum Jitter (ms)": max_jitter
    }

    return rtt_list, jitter_values, results


def measure_speedtest():

    print("\n")
    print("=" * 60)
    print("THROUGHPUT MEASUREMENT")
    print("=" * 60)

    try:
        import speedtest

        print("Finding the best available Speedtest server...")

        st = speedtest.Speedtest()
        st.get_best_server()

        server = st.results.server

        server_name = (
            f"{server.get('sponsor', 'Unknown')} "
            f"({server.get('name', 'Unknown')})"
        )

        print(f"Server : {server_name}")

        print("\nMeasuring Download Throughput...")
        download_bps = st.download()
        download_mbps = download_bps / 1_000_000

        print(f"Download : {download_mbps:.2f} Mbps")

        print("\nMeasuring Upload Throughput...")
        upload_bps = st.upload()
        upload_mbps = upload_bps / 1_000_000

        print(f"Upload   : {upload_mbps:.2f} Mbps")

        speedtest_latency = st.results.ping
        print(f"Latency  : {speedtest_latency:.2f} ms")

        results = {
            "Download Throughput (Mbps)": download_mbps,
            "Upload Throughput (Mbps)": upload_mbps,
            "Speedtest Latency (ms)": speedtest_latency,
            "Speedtest Server": server_name
        }

        return results

    except Exception as e:
        print("\nERROR: Speedtest measurement failed.")
        print("Reason:", str(e))
        print("\nPlease check:")
        print("• Internet connection")
        print("• Network availability")
        print("• Speedtest server availability")

        return None


# ============================================================
# EXPERIMENT 7
# Throughput and Latency Measurement
# ============================================================

TARGET = "8.8.8.8"
PING_COUNT = 15

# Measure Latency
rtt_data, jitter_data, ping_results = measure_ping(
    host=TARGET,
    count=PING_COUNT
)

# Measure Throughput
speed_results = measure_speedtest()

# Display Final Results
print("\n")
print("=" * 70)
print("          NETWORK PERFORMANCE RESULTS")
print("=" * 70)

print(f"Target Host : {TARGET}")
print("-" * 70)

for key, value in ping_results.items():
    if isinstance(value, float):
        print(f"{key:<35}: {value:.2f}")
    else:
        print(f"{key:<35}: {value}")

print("-" * 70)

if speed_results:
    for key, value in speed_results.items():
        if isinstance(value, float):
            print(f"{key:<35}: {value:.2f}")
        else:
            print(f"{key:<35}: {value}")
else:
    print("Throughput measurement : FAILED")

print("=" * 70)

# Observation Table
observation = {
    "Parameter": [
        "Packets Sent",
        "Packets Received",
        "Packet Loss",
        "Minimum RTT",
        "Maximum RTT",
        "Average RTT",
        "Median RTT",
        "RTT Standard Deviation",
        "95th Percentile RTT",
        "Average Jitter",
        "Maximum Jitter"
    ],
    "Measured Value": [
        ping_results["Packets Sent"],
        ping_results["Packets Received"],
        f'{ping_results["Packet Loss (%)"]:.2f} %',
        f'{ping_results["Minimum RTT (ms)"]:.2f} ms',
        f'{ping_results["Maximum RTT (ms)"]:.2f} ms',
        f'{ping_results["Average RTT (ms)"]:.2f} ms',
        f'{ping_results["Median RTT (ms)"]:.2f} ms',
        f'{ping_results["RTT Standard Deviation (ms)"]:.2f} ms',
        f'{ping_results["95th Percentile RTT (ms)"]:.2f} ms',
        f'{ping_results["Average Jitter (ms)"]:.2f} ms',
        f'{ping_results["Maximum Jitter (ms)"]:.2f} ms'
    ]
}

if speed_results:
    observation["Parameter"].extend([
        "Download Throughput",
        "Upload Throughput",
        "Speedtest Latency"
    ])

    observation["Measured Value"].extend([
        f'{speed_results["Download Throughput (Mbps)"]:.2f} Mbps',
        f'{speed_results["Upload Throughput (Mbps)"]:.2f} Mbps',
        f'{speed_results["Speedtest Latency (ms)"]:.2f} ms'
    ])

df = pd.DataFrame(observation)
print("\nObservation Table:")
print(df.to_string(index=False))

# Plot RTT
plt.figure(figsize=(10, 5))

plt.plot(
    range(1, len(rtt_data) + 1),
    rtt_data,
    marker='o',
    linewidth=2,
    label='RTT'
)

plt.axhline(
    ping_results["Average RTT (ms)"],
    linestyle='--',
    label=(
        f'Average RTT = '
        f'{ping_results["Average RTT (ms)"]:.2f} ms'
    )
)

plt.xlabel("Packet Number")
plt.ylabel("Round-Trip Time (ms)")
plt.title("ICMP Round-Trip Time (RTT) Variation")
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.savefig('/home/chiragk/mdmlab/outputs/exp7_rtt.png', dpi=150, bbox_inches='tight')
print("\nRTT graph saved: exp7_rtt.png")

# Plot Jitter
if len(jitter_data) > 0:

    plt.figure(figsize=(10, 5))

    plt.plot(
        range(2, len(rtt_data) + 1),
        jitter_data,
        marker='o',
        linewidth=2
    )

    plt.axhline(
        ping_results["Average Jitter (ms)"],
        linestyle='--',
        label=(
            f'Average Jitter = '
            f'{ping_results["Average Jitter (ms)"]:.2f} ms'
        )
    )

    plt.xlabel("Packet Number")
    plt.ylabel("Jitter (ms)")
    plt.title("Packet-to-Packet Jitter")
    plt.grid(True, linestyle=':')
    plt.legend()
    plt.tight_layout()
    plt.savefig('/home/chiragk/mdmlab/outputs/exp7_jitter.png', dpi=150, bbox_inches='tight')
    print("Jitter graph saved: exp7_jitter.png")

# Plot Throughput
if speed_results:

    metrics = ["Download", "Upload"]

    values = [
        speed_results["Download Throughput (Mbps)"],
        speed_results["Upload Throughput (Mbps)"]
    ]

    plt.figure(figsize=(8, 5))

    bars = plt.bar(
        metrics,
        values,
        width=0.5
    )

    plt.ylabel("Throughput (Mbps)")
    plt.title("Measured Network Throughput")
    plt.grid(axis='y', linestyle=':')

    for bar, value in zip(bars, values):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            value,
            f"{value:.2f} Mbps",
            ha='center',
            va='bottom'
        )

    plt.tight_layout()
    plt.savefig('/home/chiragk/mdmlab/outputs/exp7_throughput.png', dpi=150, bbox_inches='tight')
    print("Throughput graph saved: exp7_throughput.png")
