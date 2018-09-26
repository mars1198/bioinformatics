fin = open('dataset_200_8.txt', 'r')
fout=open('output.txt', 'w')
reads=[]
for line in fin.readlines():
    reads.append(line.replace('\n',''))
k=len(reads[0])
edges=[]
nodes=[]
patterns=[]
smegnosty={}
for r in reads:
    prefix=r[:-1]
    suffix=r[1:]
    if not(prefix in patterns):
        patterns.append(prefix)
    if not(suffix in patterns):
        patterns.append(suffix)
for pattern in patterns:
    smegnosty[pattern]=[]
for r in reads:
    smegnosty[r[:-1]].append(r[1:])

for key in sorted(smegnosty):
    if not(smegnosty[key]==[]):
        fout.write(key+" -> "+','.join(smegnosty[key])+'\n')
fin.close()
fout.close()
