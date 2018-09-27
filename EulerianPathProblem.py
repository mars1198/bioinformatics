from random import randint


fin = open('dataset_203_6.txt', 'r')
fout=open('output.txt', 'w')
smegnosty={}
reverse_smegnosty={}
count_us = 0
count = 0
used={}
cycle=[]
count_e=1

for line in fin.readlines():
    s=line.replace('\n','').split(' -> ')
    list_temp=s[1].split(',')
    smegnosty[s[0]]=list_temp
    for v in list_temp:
        if v in reverse_smegnosty.keys():
            reverse_smegnosty[v].append(s[0])
        else:
            reverse_smegnosty[v]=[]
            reverse_smegnosty[v].append(s[0])
    count_e=count_e+len(smegnosty[s[0]])
    used[s[0]]=[]



def formCycle(v0):
    global count_us, count_e
    cycle=[]
    cycle.append(v0)
    r=randint(0,len(smegnosty[v0])-1)
    v1=smegnosty[v0][r]
    while(v1 in used[v0]):
        r=randint(0,len(smegnosty[v0])-1)
        v1=smegnosty[v0][r]
    used[v0].append(v1)


    count_us+=1
    if v1==v0:
        return cycle
    else:
        cycle.append(v1)
    while True:
        r=randint(0,len(smegnosty[v1])-1)
        while(smegnosty[v1][r] in used[v1]):
            r=randint(0,len(smegnosty[v1])-1)
        v0=v1
        v1=smegnosty[v1][r]
        used[v0].append(v1)
        count_us=count_us+1
        if v1==cycle[0]:
            return cycle
        else:
            cycle.append(v1)

def newStart(cycle):
    for v in cycle:
        if not(len(used[v])==len(smegnosty[v])):
            return v

def EULERIANCYCLE(v0):
        cycle=formCycle(v0)
        while not(count_us==count_e):
            v0=newStart(cycle)
            cycle2=formCycle(v0)
            i=0
            for v in cycle:
                if v==v0:
                    i=cycle.index(v)
                    break
            cycle=(cycle[:i]+cycle2[:]+cycle2[:1]+cycle[i+1:])
        cycle.append(cycle[0])
        return cycle
start=0
stop=0
for v in smegnosty.keys():
    if v not in reverse_smegnosty:
        reverse_smegnosty[v] = []
    if len(smegnosty[v])>len(reverse_smegnosty[v]):
        start=v
    if len(smegnosty[v])<len(reverse_smegnosty[v]):
        stop=v
for v in reverse_smegnosty.keys():
    if v not in smegnosty:
        smegnosty[v] = []
    if len(smegnosty[v])>len(reverse_smegnosty[v]):
        start=v
    if len(smegnosty[v])<len(reverse_smegnosty[v]):
        stop=v
for v in list(smegnosty.keys()):
    if smegnosty[v]==[]:
        smegnosty.pop(v,None)
print(start,stop)

if stop in smegnosty.keys():
    smegnosty[stop].append(start)
else:
    smegnosty[stop]=[]
    smegnosty[stop].append(start)
used[stop]=[]
print(smegnosty)
r=randint(0,len(smegnosty.keys())-1)
v0=list(smegnosty.keys())[r]
cycle=(EULERIANCYCLE(v0))
cycle=cycle[1:]
i=cycle.index(start, 0)

while cycle[i-1]!=stop:
    i=cycle.index(start, i+1)


print(cycle,i)
path=cycle[i:]+cycle[:i]
fout.write("->".join(path))
fin.close()
fout.close()
