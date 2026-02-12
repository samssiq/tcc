import pandas as pd

file = pd.read_csv("output_csv_2026-02-11-22:29:15/kube_pod_status_phase.csv")

file = file[file["value"] == 1]

minimo = file["timestamp"].min()

file["timestamp"] = [ts - minimo for ts in file["timestamp"]]

timestamps = file["timestamp"].unique()

for ts in timestamps:

    pending = file[file["phase"] == "Pending"]

    pending = pending[pending["timestamp"] == ts]["pod"].unique()

    pending = [pod for pod in pending if pod.startswith("otel-")]

    print(f"Timestamp: {ts} tem {len(pending)} pods pendentes")

    running = file[file["phase"] == "Running"]

    running = running[running["timestamp"] == ts]["pod"].unique()

    running = [pod for pod in running if pod.startswith("otel-")]

    print(f"Timestamp: {ts} tem {len(running)} pods rodando")

    pods = file[file["timestamp"] == ts]["pod"].unique()

    pods = [pod for pod in pods if pod.startswith("otel-")]

    # print(f"Timestamp: {ts} tem {len(pods)} pods")
