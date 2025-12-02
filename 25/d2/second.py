sum = 0
def is_repeating(y):
    id = str(y)
    for i in range(1, len(id)//2 + 1):
        if len(id) % i == 0:
            pattern = id[:i]
            if pattern * (len(id) // i) == id:
                print(pattern * (len(id)//i))
                print(y)
                return True
    return False


with open("list", "r") as f:
    line = f.read()
    ranges = line.split(",")
    for ran in (ranges):
        temp = ran.split("-")
        min = int(temp[0])
        max = int(temp[1])
        for x in range(min , max + 1):
            if is_repeating(x):
                sum += x

print(sum)
