fin = open('dataset_198_10.txt', 'r')
fout=open('output.txt', 'w')
reads=[]

for line in fin.readlines():
    reads.append(line.replace('\n',''))
reads.sort()
for r1 in reads:
    for r2 in reads:
        if r1[1:]==r2[:len(r1)-1]:
            fout.write(r1+' -> '+r2+"\n")
fin.close()
fout.close()
