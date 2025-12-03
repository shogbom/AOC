


sum = 0

with open("list", "r") as f:
    for line in f:
        line = line.strip()
        tiotal, num = 0, 0
        if not line:
            continue
        #brute force!
        max = 0
        for x in range(0 , len(line)):
            for y in range(x + 1 , len(line)):
                if max < (int(line[x]) * 10) + int(line[y]):
                    max = (int(line[x]) * 10) + int(line[y])

        sum += max
print(sum)
