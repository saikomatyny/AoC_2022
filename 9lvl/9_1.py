ccc = open('/home/sirko/Рабочий стол/9lvl/test_input.txt', 'r')
moves = ccc.read()
moves = moves.split('\n')
del moves[-1]

xT = 0
yT = 0
xH = 0
yH = 0
t = '00'
road = ['00']
#        XY

for i in range(len(moves)):
    move = moves[i].split()

    if move[0] == 'R':
        for _ in range(int(move[-1])):
            xH += 1
            if _ == 0 and i != 0 and int(move[-1]) > 1:
                if yT + 1 == yH:
                    yT += 1
                else:
                    yT -= 1
            
            elif not(xH - 1 == xT or xH == xT or xH + 1 == xT):
                xT += 1
                t = str(xT) + str(yT)
            if t not in road:
                road.append(t)

    elif move[0] == 'L':
        for _ in range(int(move[-1])):
            xH -= 1
            if _ == 0 and i != 0 and int(move[-1]) > 1:
                if yT + 1 == yH:
                    yT += 1
                else:
                    yT -= 1

            elif not(xH - 1 == xT or xH == xT or xH + 1 == xT):
                xT -= 1
                t = str(xT) + str(yT)
            if t not in road:
                road.append(t)

    elif move[0] == 'U':
        for _ in range(int(move[-1])):
            yH += 1
            if _ == 0 and i != 0 and int(move[-1]) > 1:
                if xT + 1 == xH:
                    xT += 1
                else:
                    xT -= 1
            elif not(yH - 1 == yT or yH == yT or yH + 1 == yT):
                yT += 1
                t = str(xT) + str(yT)
            if t not in road:
                road.append(t)

    else:
        for _ in range(int(move[-1])):
            yH -= 1
            if _ == 0 and i != 0 and int(move[-1]) > 1:
                if xT + 1 == xH:
                    xT += 1
                else:
                    xT -= 1
            elif not(yH - 1 == yT or yH == yT or yH + 1 == yT):
                yT -= 1
                t = str(xT) + str(yT)
            if t not in road:
                road.append(t)
    

print(len(road))
print(road)