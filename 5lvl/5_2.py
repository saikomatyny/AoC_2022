
col1 = '  GBDCPR'
col2 = '     GVH'
col3 = ' MPJDQSN'
col4 = 'MNCDGLSP'
col5 = 'SLFPCNBJ'
col6 = 'STGVZDBQ'
col7 = ' QTFHMZB'
col8 = '   FBDMC'
col9 = '    GQCF'
listCol = [col1, col2, col3, col4, col5, col6, col7, col8, col9]

ccc = open('C:\\Users\\user\\Desktop\\AoC_2022\\5lvl\\input.txt', 'r')
moves = ccc.read()
moves = moves.replace('move', ' ')
moves = moves.replace('from', ' ')
moves = moves.replace('to', ' ')
moves = moves.split('\n')

# move 3 from 9 to 5
check = True
gruz = ''
for m in moves:
    m = m.split()
    for i in range(9):
        if i + 1 == int(m[1]):
            for t in range(len(listCol[i])):
                if listCol[i][t].isalpha():
                    gruz = listCol[i][t:t + int(m[0])]
                    listCol[i] = (' ' * len(gruz)) + listCol[i][:t] + listCol[i][t + int(m[0]):]
                    break
            break
    for i in range(9):
        if i + 1 == int(m[2]):
            for t in range(len(listCol[i])):
                if listCol[i][t].isalpha():
                    check = False
                    listCol[i] = listCol[i][t:]
                    listCol[i] = gruz + listCol[i]
                    break
            if check:
                listCol[i] = listCol[i][t:]
                listCol[i] = gruz + listCol[i]
                check = True
            check = True
            break
        

for i in listCol:
    print(i.strip(' ')[0], end = '')