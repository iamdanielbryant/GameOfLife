import random,time,copy, os
WIDTH = 60
HEIGHT = 20
SPEED = 0.1
c = '.'

nextCells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append(c)
        else:
            column.append(' ')
    nextCells.append(column)

while True:
    os.system('CLS')
    currentCells = copy.deepcopy(nextCells)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')
        print()


    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == c:
                numNeighbors += 1
            if currentCells[x][aboveCoord] == c:
                numNeighbors += 1
            if currentCells[rightCoord][aboveCoord] == c:
                numNeighbors += 1
            if currentCells[leftCoord][y] == c:
                numNeighbors += 1
            if currentCells[rightCoord][y] == c:
                numNeighbors += 1
            if currentCells[leftCoord][belowCoord] == c:
                numNeighbors += 1
            if currentCells[x][belowCoord] == c:
                numNeighbors += 1
            if currentCells[rightCoord][belowCoord] == c:
                numNeighbors += 1

            if currentCells[x][y] == c and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[x][y] = c
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                nextCells[x][y] = c
            else:
                nextCells[x][y] = ' '
    time.sleep(SPEED)



        

