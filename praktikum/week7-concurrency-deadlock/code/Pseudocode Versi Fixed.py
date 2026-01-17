import threading
import time

N = 5
forks = [threading.Lock() for _ in range(N)]
room = threading.Semaphore(N - 1)  # max 4 philosopher

def philosopher(i):
    left = forks[i]
    right = forks[(i + 1) % N]

    while True:
        print(f"Philosopher {i} is thinking")
        time.sleep(1)

        room.acquire()  # batasan jumlah filsuf

        left.acquire()
        right.acquire()

        print(f"Philosopher {i} is eating")
        time.sleep(2)

        left.release()
        right.release()
        room.release()

        print(f"Philosopher {i} finished eating\n")

threads = []
for i in range(N):
    t = threading.Thread(target=philosopher, args=(i,))
    threads.append(t)
    t.start()
