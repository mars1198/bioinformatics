def frequentWordsWithMismatchesAndReverseComplements( s, k, d ):
    counts = {}
    for i in range(len(s)-k+1):
        for sub in [s[i:i+k],reverseComplement(s[i:i+k])]:
            for neighbor in neighbors(sub,d):
                if neighbor not in counts:
                    counts[neighbor] = 0
                counts[neighbor] += 1
    m = max(counts.values())
    return [kmer for kmer in counts if counts[kmer] == m]

def neighbors( s, d ):
    if d == 0:
        return [s]
    if len(s) == 1:
        return ['A','C','G','T']
    out = []
    for neighbor in neighbors(s[1:],d):
        if hamming(s[1:],neighbor) < d:
            out.extend(['A'+neighbor,'C'+neighbor,'G'+neighbor,'T'+neighbor])
        else:
            out.append(s[0] + neighbor)
    return out

def hamming( s, t ):
    return sum([s[i] != t[i] for i in range(len(s))])

def reverseComplement( s ):
    return ''.join([complement(s[i]) for i in range(len(s)-1,-1,-1)])

def complement( s ):
    return {'A':'T','T':'A','C':'G','G':'C'}[s]

s = 'GATGAAACTAGAAAAGAAAAAATGGAGACTACTAAAACTAAAAGAGATGTGGACTAAAAGAAACTAGACTAAAAAAAAAAAATGAAGAGATGAAAAAGAGAGAGACTATGAAATGGAAAAAAAAAAAACTATGCTAAAAGACTACTAAAATGAATGGAAAACTAGATGAAGAGAGATGAAAAAAAAAAAAAAAGATGGAAAAAGAAATGCTACTAGACTACTACTAAAAAAAAACTAAAAAA'
k = 7
d = 2
a = str(frequentWordsWithMismatchesAndReverseComplements(s,k,d))
a = a.replace("'","")
a = a.replace(',','')
print (a)
