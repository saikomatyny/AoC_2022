ttt = open('C:\\Users\\user\\Desktop\\input.txt', 'r')
e = ttt.read()
e = e.split('\n')
del e[-1]
c = 0
# A - rock; B - paper; C - scissors
# X         Y          Z
# 1         2          3
#(0 if you lost, 3 if the round was a draw, and 6 if you won)
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
for i in e:
    if i[-1] == 'X':
        if i[0] == 'A':
            c += 3
        elif i[0] == 'B':
            c += 1
        elif i[0] == 'C':
            c += 2
    elif i[-1] == 'Y':
        c += 3
        if i[0] == 'A':
            c += 1
        elif i[0] == 'B':
            c += 2
        elif i[0] == 'C':
            c += 3
    elif i[-1] == 'Z':
        c += 6
        if i[0] == 'A':
            c += 2
        elif i[0] == 'B':
            c += 3
        elif i[0] == 'C':
            c += 1

print(c)