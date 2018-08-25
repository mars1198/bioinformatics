# first, import the random package
import random

# Input:  Integers k, t, and N, followed by a collection of strings Dna
# Output: GibbsSampler(Dna, k, t, N)
def getIndexOfChar(chr):
    return "ACGT".index(chr)

def getRandomMotifs( dna, k ):
    return [createRandomKmer(seq,k) for seq in dna]

def createRandomKmer( seq, k ):
    start = random.randint(0, len(seq)-k)
    return seq[start:start+k] 

def Score( motifs ):
    score = 0
    for count in countsFromMotifs(motifs,0):
        score += sum(count) - max(count)
    return score

def countsFromMotifs( motifs, initCount ):
    k = len(motifs[0])
    for motif in motifs:
        assert k == len(motif)
    counts = []
    for i in range(k):
        currCount = [initCount] * 4
        for motif in motifs:
            currCount[getIndexOfChar(motif[i])] += 1
        counts.append(currCount)
    return counts


def Random( pr ):
    total = float(sum(pr))
    r = random.random()
    partialSum = 0.0
    for i in range(len(pr)):
        partialSum += pr[i]
        if partialSum/total >= r:
            return i
    return -1

def findProfile( motifs, initCount ):    
    counts = countsFromMotifs(motifs,initCount)
    profile = []
    for count in counts:
        total = float(sum(count))
        probs = [c/total for c in count]
        profile.append(probs)
    return profile

def findProbKmerInProfile( kmer, profile ):
    prob = 1.0
    for i in range(len(kmer)):
        prob *= profile[i][getIndexOfChar(kmer[i])]
    return prob
def GibbsSampler( Dna, k,t, N ):
    BestMotifs = []
    motifs = getRandomMotifs(Dna,k)
    BestMotifs = motifs
    bestScore = Score(BestMotifs)
    for step in range(N):
        i = random.randint(0, t-1)
        profile = findProfile(motifs[:i] + motifs[i+1:], 1)
        pr = [findProbKmerInProfile(Dna[i][s:s+k],profile) for s in range(len(Dna[i])-k+1)]
        s = Random(pr)
        motifs[i] = Dna[i][s:s+k]
        score = Score(motifs)
        if score < bestScore:
            BestMotifs = motifs[:]
            bestScore = score
    
    return BestMotifs

# place all subroutines needed for GibbsSampler below this line
