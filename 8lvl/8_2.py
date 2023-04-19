ccc = open('C:\\Users\\user\\Desktop\\AoC_2022\\8lvl\\input.txt', 'r')
matrix = ccc.read()

grid = []
matrix = matrix.split('\n')
for _ in range(len(matrix)):
    t = [int(i) for i in matrix[_]]
    grid.append(t)

cm = 0
c = 1
ct = 0

for i in range(1, len(grid) - 1):
    for j in range(1, len(grid) - 1):
        for k in range(j + 1, len(grid)):
            if grid[i][k] >= grid[i][j]:
                ct += 1
                break
            else:
                ct += 1
        c *= ct
        ct = 0

        for k in range(j - 1, -1, -1):
            if grid[i][k] >= grid[i][j]:
                ct += 1
                break
            else:
                ct += 1
        c *= ct
        ct = 0
        
        for x in range(i + 1, len(grid)):
            if grid[x][j] >= grid[i][j]:
                ct += 1
                break
            else:
                ct += 1
        c *= ct
        ct = 0
        
        for x in range(i - 1, -1, -1):
            if grid[x][j] >= grid[i][j]:
                ct += 1
                break
            else:
                ct += 1
        c *= ct
        ct = 0

        if c > cm:
            cm = c
        c = 1

print(cm)