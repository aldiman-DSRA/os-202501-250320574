# scheduling.py
# Modul CPU Scheduling: FCFS & SJF (Non-Preemptive)

def fcfs():
    processes = [
        {"pid": "P1", "arrival": 0, "burst": 5},
        {"pid": "P2", "arrival": 1, "burst": 3},
        {"pid": "P3", "arrival": 2, "burst": 8},
        {"pid": "P4", "arrival": 3, "burst": 6},
    ]

    time = 0
    total_wt = 0
    total_tat = 0

    print("\n=== FCFS Scheduling ===")
    print("PID | WT | TAT")

    for p in processes:
        wt = max(0, time - p["arrival"])
        tat = wt + p["burst"]
        time += p["burst"]

        total_wt += wt
        total_tat += tat

        print(f"{p['pid']}  | {wt}  | {tat}")

    n = len(processes)
    print(f"Rata-rata Waiting Time    : {total_wt / n}")
    print(f"Rata-rata Turnaround Time : {total_tat / n}")


def sjf():
    processes = [
        {"pid": "P1", "arrival": 0, "burst": 5},
        {"pid": "P2", "arrival": 1, "burst": 3},
        {"pid": "P3", "arrival": 2, "burst": 8},
        {"pid": "P4", "arrival": 3, "burst": 6},
    ]

    time = 0
    total_wt = 0
    total_tat = 0
    completed = []

    print("\n=== SJF Scheduling (Non-Preemptive) ===")
    print("PID | WT | TAT")

    while processes:
        ready = [p for p in processes if p["arrival"] <= time]

        if not ready:
            time += 1
            continue

        p = min(ready, key=lambda x: x["burst"])
        processes.remove(p)

        wt = time - p["arrival"]
        tat = wt + p["burst"]
        time += p["burst"]

        total_wt += wt
        total_tat += tat
        completed.append(p)

        print(f"{p['pid']}  | {wt}  | {tat}")

    n = len(completed)
    print(f"Rata-rata Waiting Time    : {total_wt / n}")
    print(f"Rata-rata Turnaround Time : {total_tat / n}")
