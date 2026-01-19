# pagereplacement.py
# Modul Page Replacement: FIFO & LRU

def fifo():
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    frames = 3

    memory = []
    page_fault = 0
    hit = 0

    print("\n=== FIFO Page Replacement ===")
    print("Page | Frame | Status")

    for page in pages:
        if page in memory:
            hit += 1
            status = "HIT"
        else:
            page_fault += 1
            status = "FAULT"

            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)

        print(f"{page}    | {memory} | {status}")

    total = len(pages)
    print(f"Total Page Fault : {page_fault}")
    print(f"Hit Ratio        : {hit / total}")


def lru():
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    frames = 3

    memory = []
    last_used = {}
    page_fault = 0
    hit = 0
    time = 0

    print("\n=== LRU Page Replacement ===")
    print("Page | Frame | Status")

    for page in pages:
        time += 1

        if page in memory:
            hit += 1
            status = "HIT"
        else:
            page_fault += 1
            status = "FAULT"

            if len(memory) < frames:
                memory.append(page)
            else:
                lru_page = min(memory, key=lambda x: last_used[x])
                memory.remove(lru_page)
                memory.append(page)

        last_used[page] = time
        print(f"{page}    | {memory} | {status}")

    total = len(pages)
    print(f"Total Page Fault : {page_fault}")
    print(f"Hit Ratio        : {hit / total}")
