ccc = open('C:\\Users\\user\\Desktop\\AoC_2022\\8lvl\\input.txt', 'r')
matrix = ccc.read()

grid = []
matrix = matrix.split('\n')
for _ in range(len(matrix)):
    t = [int(i) for i in matrix[_]]
    grid.append(t)

checkRowLeft = False
checkRowRight = False
checkColumnUp = False
checkColumnDown = False
c = (len(grid[0]) - 1) * 4

for i in range(1, len(grid) - 1):
    for j in range(1, len(grid) - 1):

        for x in range(0, j):
            if grid[i][x] >= grid[i][j]:
                checkRowLeft = True
                break
        if not checkRowLeft:
            c += 1
        else:
            checkRowLeft = False

            for x in range(j + 1, len(grid)):
                if grid[i][x] >= grid[i][j]:
                    checkRowRight = True
                    break
            if not checkRowRight:
                c += 1
            else:
                checkRowRight = False

                for k in range(0, i):
                    if grid[k][j] >= grid[i][j]:
                        checkColumnUp = True
                        break
                if not checkColumnUp:
                    c += 1
                else:
                    checkColumnUp = False

                    for k in range(i + 1, len(grid)):
                        if grid[k][j] >= grid[i][j]:
                            checkColumnDown = True
                            break
                    if not checkColumnDown:
                        c += 1
                    else:
                        checkColumnDown = False

print(c)