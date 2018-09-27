from random import randint
fin = open('dataset_203_2.txt', 'r')
fout=open('output.txt', 'w')
smegnosty={}
reverse_smegnosty={}
count_us = 0
count = 0
used={}
cycle=[]
count_e=0

for line in fin.readlines():
    s=line.replace('\n','').split(' -> ')
    list_temp=s[1].split(',')
    smegnosty[s[0]]=list_temp
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

r=random.randint(0,len(smegnosty.keys())-1)
v0=list(smegnosty.keys())[r]
cycle=(EULERIANCYCLE(v0))
print(len(cycle))
fout.write("->".join(cycle))
fin.close()
fout.close()
