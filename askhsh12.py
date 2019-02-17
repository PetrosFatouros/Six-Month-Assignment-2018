#ASKHSH 12

#An uparxoun 2 h perissotera min h max grammata allazei auta pou emfanizontai prwta sto keimeno

import string
f=open('text.txt','r')
content=f.readlines()
freqs = {}
for line in content:
    line = filter(lambda x: x in string.letters, line.upper())
    for char in line:
        if char in freqs:
            freqs[char] += 1
        else:
            freqs[char] = 1
counters=[]
for freq in freqs:
    counters.append(freqs[freq])
min=min(counters)
max=max(counters)
for letter,freq in freqs.items():
    if freq == max:
        maxletter=letter
    if freq == min:
        minletter=letter
newcontent=[]
for line in content:
    for letter in line:
        if letter==minletter.lower() or letter==minletter:
            line=line.replace(letter,maxletter)
        if letter==maxletter.lower() or letter==maxletter:
            line=line.replace(letter,minletter)
    newcontent.append(line)
f.close()
f=open('text.txt','w').close()
f=open('text.txt','a')
for line in newcontent:
    f.write(line)
f.close()
