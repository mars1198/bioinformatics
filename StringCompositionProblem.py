all = open('dataset_197_3.txt').read()
a = all[4:]
b = int(all[0:3])

def composition(a, b):
    kmers = []
    for i in range(len(a)-b):
        kmer = a[i:i+b]
        kmers.append(kmer)
    kmers = sorted(kmers)
    print(kmers)
    file = open("result.txt", "w")
    for item in kmers:
        file.write(item+'\n')
    file.close()

composition(a, b)
