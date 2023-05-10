ccc = open('AOC_2022_d7_input.txt.txt', 'r')
SSD = ccc.read()

SSD = SSD.split('\n')
current_location = [] #shows current location in disk
memory = {} #shows all repositories and their total size
c = 0

for i in SSD:
    rep = i.split() #every line of txt file
    if len(rep) == 3 and rep[2] != '..': #adding new repositories (if they exists)
        memory[rep[2]] = 0
    elif rep[0] == 'dir':
        memory[rep[1]] = 0
    
    if len(rep) == 3 and (rep[1] == 'cd' and rep[2] != '..'): #showing our current location
        current_location.append(rep[2])
    elif len(rep) == 3 and rep[2] == '..':
        del current_location[-1]
    
    if rep[0][0].isnumeric(): #adding size of file to all available repositories
        for x in current_location:
            memory[x] += int(rep[0])
    
    if rep[0] == 'dir': #adding size of directory to all of repositories
        memory[current_location[-1]] += memory[rep[-1]]

for i in memory: #counting final result
    if memory[i] <= 100000:
        c += memory[i]

print(c)
print(memory)