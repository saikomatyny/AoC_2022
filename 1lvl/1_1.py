ccc = open('C:\\Users\\user\\Desktop\\input.txt', 'r')
f = ccc.read()
f = f.split('\n')
c = 0
c2 = 0
for i in f:
    if i == '':
        pass
        if c2 > c:
            c = c2
        c2 = 0
    else:
        c2 += int(i)
ccc.close()
print(c)