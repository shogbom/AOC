
with open("list", "r") as f:
    lines = [line.strip() for line in f if line.strip() != ""]

# Split into ranges and ingredient IDs
range_lines = []
ids = []
for line in lines:
    if "-" in line:
        range_lines.append(line)
    else:
        ids.append(int(line))


ranges = []
for r in range_lines:
    start, end = map(int, r.split("-"))
    ranges.append((start, end))

count = 0
for ing in ids:
    if any(start <= ing <= end for start, end in ranges):
        count += 1

print(count)
