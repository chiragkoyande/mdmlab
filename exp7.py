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


if __name__ == '__main__':
    rtt_list, jitter_values, results = measure_ping('8.8.8.8', count=15)
    print('Ping measurement finished successfully.')
