ttt = open('C:\\Users\\user\\Desktop\\input.txt', 'r')
e = ttt.read()
e = e.split('\n')
del e[-1]
c = 0
c2 = 0
# A - rock; B - paper; C - scissors
# X         Y          Z
# 1         2          3
#(0 if you lost, 3 if the round was a draw, and 6 if you won)
for i in e:
    if i[-1] == 'X':
        c2 += 1
        if i[0] == 'A':
            c2 += 3
        elif i[0] == 'C':
            c2 += 6
    elif i[-1] == 'Y':
        c2 += 2
        if i[0] == 'B':
            c2 += 3
        elif i[0] == 'A':
            c2 += 6
    elif i[-1] == 'Z':
        c2 += 3
        if i[0] == 'C':
            c2 += 3
        elif i[0] == 'B':
            c2 += 6
    
    c += c2
    c2 = 0

print(c)