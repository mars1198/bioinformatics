from random import randint


fin = open('dataset_205_5.txt', 'r')
fout=open('output.txt', 'w')
smegnosty={}
reverse_smegnosty={}

reads=[]
for line in fin.readlines():
    reads.append(line.replace('\n',''))
k=len(reads[0])
patterns=[]
for r in reads:
    prefix=r[:-1]
    suffix=r[1:]
    if not(prefix in patterns):
        patterns.append(prefix)
    if not(suffix in patterns):
        patterns.append(suffix)
for pattern in patterns:
    smegnosty[pattern]=[]
    reverse_smegnosty[pattern]=[]
for r in reads:
    smegnosty[r[:-1]].append(r[1:])

for v in smegnosty.keys():
    list_temp=smegnosty[v]
    for v1 in list_temp:
        if v1 in reverse_smegnosty.keys():
            reverse_smegnosty[v1].append(v)
        else:
            reverse_smegnosty[v1]=[]
            reverse_smegnosty[v1].append(v)

#print(smegnosty)
#print(reverse_smegnosty)
contig=''
for node0 in smegnosty.keys():
    #print(node0,'node0')
    if (not(smegnosty[node0]==[]) and (not(len(smegnosty[node0])== 1 and len(reverse_smegnosty[node0])==1))):
        for node1 in smegnosty[node0]:
            #print(node1,'node1')
            contig=node0[:]
            contig=contig+node1[-1]
            if not(smegnosty[node1]==[]):
                #print(node1, smegnosty[node1],reverse_smegnosty[node1],'!@1@!')
                if not(len(smegnosty[node1])== 1 and len(reverse_smegnosty[node1])==1):
                    print(contig)
                    fout.write(contig+'\n')
                    continue
                else:
                    node2=smegnosty[node1][0]
                    #print(node2,'node2')
                    contig=contig+node2[-1]
                    #print(node2, smegnosty[node2],reverse_smegnosty[node2],'!@@!')
                    while (not(smegnosty[node2]==[]) and (len(smegnosty[node2])==1) and (len(reverse_smegnosty[node2])==1)):
                        node2=smegnosty[node2][0]
                        contig=contig+node2[-1]
                        #print(node2,'nextnode')
                    fout.write(contig+'\n')
                    print(contig)
            else:
                fout.write(contig+'\n')
                print(contig)
                continue
fin.close()
fout.close()
