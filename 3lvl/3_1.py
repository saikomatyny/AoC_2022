ccc = open('C:\\Users\\user\\Desktop\\input.txt')
t = ccc.read()
t = t.split('\n')
# a - z; 97 - 122
# A - Z; 65 - 90 (+26)
c = 0
for i in t:
    t2 = i[(len(i) // 2):]
    t1 = i[:(len(i) // 2)]
    for x in range(len(t1)):
        if t1[x] in t2:
            if ord(t1[x]) < 97:
                c += 27 + ord(t1[x]) - 65
                break
            else:
                c += ord(t1[x]) - 96
                break
print(c)
