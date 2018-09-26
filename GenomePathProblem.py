fin = open('dataset_198_3.txt', 'r')
fout=open('output.txt', 'w')
reads=[]
for line in fin.readlines():
    reads.append(line.replace('\n',''))
k=len(reads[0])
fout.write(reads[0])
for r in reads[1:]:
    fout.write(r[k-1:])
fin.close()
fout.close()
