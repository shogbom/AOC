#0  - 99
count = 0
curr = 50 # starting

with open("list", "r") as f:
    for line in f:
        print(curr)
        ist = line.strip()
        ch = ist[0]
        num = int(ist[1:])
        for _ in range (num):
            if ch == 'R':
                curr = (curr+1)%100
            elif ch == 'L':
                curr = (curr - 1) % 100
            else: 
                print("error")
            if curr == 0:
                count += 1

    print(count)
            
