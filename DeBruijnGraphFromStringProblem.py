fin = open('dataset_199_6.txt', 'r')
fout=open('output.txt', 'w')
s0=fin.readline().replace('\n','').split(' ')
k=int(s0[0])
s=fin.readline().replace('\n','')
edges=[]
nodes=[]
d={}
for i in range(len(s)-k+1):
    r=s[i:i+k]
    v=s[i:i+k-1]
    edges.append(r)
    nodes.append(v)
    if v in d.keys():
        d[v].append(r[1:])
    else:
        temp=[]
        temp.append(r[1:])
        d[v]=temp
for key in d.keys():
   fout.write(key+" -> "+','.join(d[key])+'\n')


fin.close()
fout.close()
