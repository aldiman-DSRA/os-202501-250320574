# Deteksi Deadlock menggunakan Wait-For Graph

# Dataset
processes = {
    "P1": {"allocation": "R1", "request": "R2"},
    "P2": {"allocation": "R2", "request": "R3"},
    "P3": {"allocation": "R3", "request": "R1"}
}

# Membuat mapping resource -> process yang memegangnya
resource_owner = {}
for p, data in processes.items():
    resource_owner[data["allocation"]] = p

# Membuat wait-for graph
wait_for = {}
for p, data in processes.items():
    requested_resource = data["request"]
    if requested_resource in resource_owner:
        wait_for[p] = resource_owner[requested_resource]

# Deteksi siklus (cycle detection)
visited = set()
stack = set()
deadlock_processes = set()

def detect_cycle(process):
    if process in stack:
        deadlock_processes.update(stack)
        return True
    if process in visited:
        return False

    visited.add(process)
    stack.add(process)

    if process in wait_for:
        if detect_cycle(wait_for[process]):
            return True

    stack.remove(process)
    return False

for p in processes:
    if detect_cycle(p):
        break

# Output
if deadlock_processes:
    print("Sistem dalam kondisi DEADLOCK")
    print("Proses yang terlibat deadlock:", ", ".join(deadlock_processes))
else:
    print("Sistem TIDAK mengalami deadlock")
