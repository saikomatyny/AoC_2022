cc = open('C:\\Users\\admin-pc\\Desktop\\AoC\\6lvl\\input.txt', 'r')
ws = cc.read()

def  sygnal(ws):
    flag = True
    for i in range(len(ws) - 13):
        t = ws[i:i + 14]
        for x in t:
            if t.count(x) != 1:
                flag = False
                break
        if not flag:
            flag = True
        else:
            return i + 14


print(sygnal(ws))