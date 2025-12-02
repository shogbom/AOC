
sum = 0



def shit(y):
    temp = str(y)
    if len(temp) % 2 != 0:
        return False
    mid = len(temp) // 2
    return temp[:mid] == temp[mid:]


with open("list", "r") as f:
    line = f.read()
    ranges = line.split(",")
    for ran in (ranges):
        temp = ran.split("-")
        min = int(temp[0])
        max = int(temp[1])
        for x in range(min , max + 1):
            if shit(x):
                sum += x

print(sum)
