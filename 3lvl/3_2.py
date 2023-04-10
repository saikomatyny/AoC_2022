ccc = open('C:\\Users\\user\\Desktop\\input.txt')
t = ccc.read()
t = t.split('\n')
# a - z; 97 - 122
# A - Z; 65 - 90 (+26)
c = 0
for i in range(2, len(t), 3):
    t1 = t[i - 2]
    t2 = t[i - 1]
    t3 = t[i]
    for x in range(len(t1)):
        if (t1.count(t1[x]) >= 1) and (t2.count(t1[x]) >= 1) and (t3.count(t1[x]) >= 1):
            if ord(t1[x]) < 97:
                c += 27 + ord(t1[x]) - 65
                break
            else:
                c += ord(t1[x]) - 96
                break

print(c)