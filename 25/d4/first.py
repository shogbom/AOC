count = 0




def isAcc(x0, y0, diagram): 
    nbrAround = 0
   
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0: 
              continue  # skip the center point

            x = x0 + dx
            y = y0 + dy
            if (x >= 0 and x < len(diagram)) and (y >= 0 and y < len(diagram[x])):
                if diagram[x][y] == '@':
                    nbrAround += 1                                  
    return nbrAround


def doShit(diagram):
    global count
    for x in range(len(diagram)):
        for y in range(len(diagram[x])):
            if diagram[x][y] == '@' :
                if isAcc(x, y, diagram) < 4:
                    count += 1


with open("list", "r") as f:
    diagram = f.read().splitlines()
    doShit(diagram)


print(count)
