import os


sum = 0
currline = 1
total_bytes = os.path.getsize("list")

def statusbar(totallines):
    done ="█" 
    noDone = "-"
    stats = "\r" + (done * ((currline * 100) // totallines)) + (noDone * (100 - ((currline * 100) // totallines)))
    print(f"|{stats}| {currline}/{totallines}", end="")


with open("list", "r") as f:
    for line in f:
        statusbar(total_bytes // len(line))
        line = line.strip()
        if not line:
            continue
        curr = 0
        prev = 0
        for x in range(12):
            dig = max(line[0:(len(line) - 12 + x +1)])
            curr += int(dig) * pow(10, 11 - x)
            line = line[line.index(dig) + 1:]
        currline += 1
        sum += curr
print("\n" ,sum == 3121910778619, "if test data")
print(sum)
