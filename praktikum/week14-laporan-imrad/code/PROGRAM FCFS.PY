processes = [
    {"pid": "P1", "arrival": 0, "burst": 12},
    {"pid": "P2", "arrival": 1, "burst": 2},
    {"pid": "P3", "arrival": 2, "burst": 1},
    {"pid": "P4", "arrival": 3, "burst": 3},
]

def fcfs(processes):
    time = 0
    result = []

    # Urutkan berdasarkan arrival time
    processes = sorted(processes, key=lambda x: x["arrival"])

    for p in processes:
        start = max(time, p["arrival"])
        finish = start + p["burst"]
        waiting = start - p["arrival"]
        turnaround = finish - p["arrival"]

        result.append({
            "Process": p["pid"],
            "Start": start,
            "Finish": finish,
            "Waiting": waiting,
            "Turnaround": turnaround
        })

        time = finish

    return result

fcfs_result = fcfs(processes)

print("=== FCFS ===")
for r in fcfs_result:
    print(r)
