#0  - 99
count = 0
curr = 50 # starting

with open("list", "r") as f:
    for line in f:
        ist = line.strip()
        ch = ist[0]
        num = int(ist[1:])
        
        if ch == 'R':
            curr += num
        elif ch == 'L':
            curr -= num
        else: 
            print("error")
        
        curr = curr % 100
        if curr == 0:
            count += 1
    print(counta):
