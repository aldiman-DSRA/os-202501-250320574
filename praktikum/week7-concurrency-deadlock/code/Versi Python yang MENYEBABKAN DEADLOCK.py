import threading
import time

N = 5
forks = [threading.Lock() for _ in range(N)]

def philosopher(i):
    left = forks[i]
    right = forks[(i + 1) % N]

    while True:
        print(f"Philosopher {i} is thinking")
        time.sleep(1)

        print(f"Philosopher {i} tries to take LEFT fork")
        left.acquire()
        print(f"Philosopher {i} took LEFT fork")

        time.sleep(1)

        print(f"Philosopher {i} tries to take RIGHT fork")
        right.acquire()
        print(f"Philosopher {i} took RIGHT fork")

        print(f"Philosopher {i} is eating")
        time.sleep(2)

        right.release()
        left.release()

threads = []
for i in range(N):
    t = threading.Thread(target=philosopher, args=(i,))
    threads.append(t)
    t.start()
