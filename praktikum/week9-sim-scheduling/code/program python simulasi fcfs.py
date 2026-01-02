# Simulasi Penjadwalan FCFS (Non-Preemptive)

# Data proses
processes = [
    {"pid": "P1", "arrival": 0, "burst": 6},
    {"pid": "P2", "arrival": 1, "burst": 8},
    {"pid": "P3", "arrival": 2, "burst": 7},
    {"pid": "P4", "arrival": 3, "burst": 3},
]

# Urutkan berdasarkan arrival time (FCFS)
processes.sort(key=lambda x: x["arrival"])

current_time = 0
total_waiting = 0
total_turnaround = 0

print("TABEL HASIL PENJADWALAN FCFS")
print("-" * 75)
print("Proses | Arrival | Burst | Start | Finish | Waiting | Turnaround")
print("-" * 75)

for p in processes:
    start_time = max(current_time, p["arrival"])
    finish_time = start_time + p["burst"]
    waiting_time = start_time - p["arrival"]
    turnaround_time = finish_time - p["arrival"]

    total_waiting += waiting_time
    total_turnaround += turnaround_time
    current_time = finish_time

    print(f"{p['pid']:6} | {p['arrival']:7} | {p['burst']:5} | "
          f"{start_time:5} | {finish_time:6} | "
          f"{waiting_time:7} | {turnaround_time:10}")

n = len(processes)
print("-" * 75)
print(f"Rata-rata Waiting Time    = {total_waiting / n:.2f}")
print(f"Rata-rata Turnaround Time = {total_turnaround / n:.2f}")
