processes = [
    {"pid": "P1", "arrival": 0, "burst": 12},
    {"pid": "P2", "arrival": 1, "burst": 2},
    {"pid": "P3", "arrival": 2, "burst": 1},
    {"pid": "P4", "arrival": 3, "burst": 3},
]

def sjf_non_preemptive(processes):
    time = 0
    completed = []
    ready_queue = processes.copy()

    while ready_queue:
        # Ambil proses yang sudah datang
        available = [p for p in ready_queue if p["arrival"] <= time]

        if not available:
            time += 1
            continue

        # Pilih burst time terkecil
        p = min(available, key=lambda x: x["burst"])
        ready_queue.remove(p)

        start = time
        finish = start + p["burst"]
        waiting = start - p["arrival"]
        turnaround = finish - p["arrival"]

        completed.append({
            "Process": p["pid"],
            "Start": start,
            "Finish": finish,
            "Waiting": waiting,
            "Turnaround": turnaround
        })

        time = finish

    return completed

sjf_result = sjf_non_preemptive(processes)

print("\n=== SJF Non-Preemptive ===")
for r in sjf_result:
    print(r)
