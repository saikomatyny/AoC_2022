ccc = open('C:\\Users\\admin-pc\\Desktop\\AoC\\input.txt', 'r')
t = ccc.read()
t = t.split('\n')
del t[-1]

c = 0
for i in t:
    i = i.split(',')
    i[0] = i[0].split('-')
    i[1] = i[1].split('-')
    if int(i[0][0]) <= int(i[1][0]) and int(i[0][1]) >= int(i[1][1]):
        c += 1
    elif int(i[0][0]) >= int(i[1][0]) and int(i[0][1]) <= int(i[1][1]):
        c += 1
print(c)