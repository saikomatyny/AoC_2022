ccc = open('C:\\Users\\user\\Desktop\\input.txt', 'r')
f = ccc.read()
f = f.split('\n')
c1 = 0
c2 = 0
c3 = 0
c = 0
for i in f:
    if i == '':
        if c > c1:
            c1, c2, c3 = c, c1, c2
        elif c > c2:
            c2, c3 = c, c2
        elif c > c3:
            c3 = c
        c = 0
    else:
        c += int(i)
if c > c1:
    c1, c2, c3 = c, c1, c2
elif c > c2:
    c2, c3 = c, c2
elif c > c3:
    c3 = c
ccc.close()
print()
print(c1 + c2 + c3)
print('', c1, c2, c3, sep = '\n')