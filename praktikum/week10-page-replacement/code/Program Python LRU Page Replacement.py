# Simulasi Page Replacement LRU

# Dataset (page reference string)
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]

# Jumlah frame
frame_size = 3

frames = []
last_used = {}
page_faults = 0
page_hits = 0
time = 0

print("Simulasi LRU Page Replacement")
print("-" * 55)
print("Page\tFrames\t\tStatus")
print("-" * 55)

for page in pages:
    time += 1

    if page in frames:
        page_hits += 1
        status = "Hit"
    else:
        page_faults += 1
        status = "Fault"

        if len(frames) < frame_size:
            frames.append(page)
        else:
            # cari halaman yang paling lama tidak digunakan
            lru_page = min(frames, key=lambda p: last_used[p])
            frames[frames.index(lru_page)] = page

    last_used[page] = time
    print(f"{page}\t{frames}\t{status}")

print("-" * 55)
print(f"Total Page Hit   : {page_hits}")
print(f"Total Page Fault : {page_faults}")
