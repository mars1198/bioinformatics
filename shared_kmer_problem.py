def reverseComplement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N':'N'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t

import bisect
#Book index analogy
class Index(object):
    def __init__(self, t, k):
        ''' Create index from all substrings of size 'length' '''
        self.k = k  # k-mer length (k)
        self.index = []
        for i in range(len(t) - k + 1):  # for each k-mer
            self.index.append((t[i:i+k], i))  # add (k-mer, offset) pair
        self.index.sort()  # alphabetize by k-mer
    
    def query(self, kmer):
        ''' Return index hits for kmer '''
        i = bisect.bisect_left(self.index, (kmer, -1))  # binary search
        hits = []
        while i < len(self.index):  # collect matching index entries
            if self.index[i][0] != kmer:
                break
            hits.append(self.index[i][1])
            i += 1
        return hits
    
def shared_kmers(t, p, k):
    index = Index(t, k)
    kmers_index = []
    for i in range(len(p) - k + 1):
        kmer = p[i:i+k]
        found = index.query(kmer)
        if len(found) > 0:
            for j in found:
                kmers_index.append((j, i))
        inverse = reverseComplement(kmer)[::-1]
        #found2 = index.query(inverse)
        #if len(found2) > 0:
            #for x in found2:
                #kmers_index.append((x, i))
        found3 = index.query(reverseComplement(kmer))
        if len(found3) > 0:
            for y in found3:
                kmers_index.append((y, i))
    return kmers_index

f = open('dataset_289_5.txt')
que = f.read().strip().split()
k = int(que[0]); t = que[1]; p = que[2]
ans = shared_kmers(t, p, k)
for pair in ans:
    print (pair)

