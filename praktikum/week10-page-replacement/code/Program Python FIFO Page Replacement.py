# Simulasi Page Replacement FIFO

# Dataset (page reference string)
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]

# Jumlah frame
frame_size = 3

frames = []
page_faults = 0
page_hits = 0
index = 0  # penunjuk FIFO

print("Simulasi FIFO Page Replacement")
print("-" * 50)
print("Page\tFrames\t\tStatus")
print("-" * 50)

for page in pages:
    if page in frames:
        page_hits += 1
        status = "Hit"
    else:
        page_faults += 1
        status = "Fault"
        if len(frames) < frame_size:
            frames.append(page)
        else:
            frames[index] = page
            index = (index + 1) % frame_size

    print(f"{page}\t{frames}\t{status}")

print("-" * 50)
print(f"Total Page Hit   : {page_hits}")
print(f"Total Page Fault : {page_faults}")
