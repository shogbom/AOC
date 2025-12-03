sum = 0
status = 1
with open("list", "r") as f:
    for line in f:
        print(status)
        line = line.strip()
        tiotal, num = 0, 0
        if not line:
            continue
        #WHY? because i can.
        max = 0
        for a in range(0 , len(line)):
            for b in range(a + 1 , len(line)):
                for c in range(b + 1, len(line)):
                    for d in range(c + 1, len(line)):
                        for e in range(d + 1, len(line)):
                            for f in range(e + 1, len(line)):
                                for g in range(f + 1, len(line)):
                                    for h in range(g + 1, len(line)):
                                        for i in range(h + 1, len(line)):
                                            for j in range(i + 1, len(line)):
                                                for k in range(j + 1, len(line)):
                                                    for l in range(k + 1, len(line)):
                                                        if max < int(line[a]) * pow(10, 11) + int(line[b]) * pow(10, 10) + int(line[c]) * pow(10, 9) + int(line[d]) * pow(10, 8) + int(line[e]) * pow(10, 7) +int(line[f]) * pow(10, 6) + int(line[g]) * pow(10, 5) + int(line[h]) * pow(10, 4) + int(line[i]) * pow(10, 3) +  int(line[j]) * pow(10, 2) + int(line[k]) * 10 + int(line[l]):
                                                            max = int(line[a]) * pow(10, 11) + int(line[b]) * pow(10, 10) + int(line[c]) * pow(10, 9) + int(line[d]) * pow(10, 8) + int(line[e]) * pow(10, 7) +int(line[f]) * pow(10, 6) + int(line[g]) * pow(10, 5) + int(line[h]) * pow(10, 4) + int(line[i]) * pow(10, 3) +  int(line[j]) * pow(10, 2) + int(line[k]) * 10 + int(line[l]) 


        sum += max
print(sum)
