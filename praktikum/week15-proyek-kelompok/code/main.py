# main.py
from scheduling import fcfs, sjf
from pagereplacement import fifo, lru

print("=== OS Simulator ===")
print("1. CPU Scheduling - FCFS")
print("2. CPU Scheduling - SJF")
print("3. Page Replacement - FIFO")
print("4. Page Replacement - LRU")

choice = input("Pilih menu (1-4): ")

if choice == "1":
    fcfs()
elif choice == "2":
    sjf()
elif choice == "3":
    fifo()
elif choice == "4":
    lru()
else:
    print("Pilihan tidak valid")
