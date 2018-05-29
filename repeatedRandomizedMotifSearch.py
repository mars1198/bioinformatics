import random
import sys

def indexToAcid(i):
    return "ACGT"[i]

def acidToIndex(a):
    return "ACGT".index(a)

def readInput( file ):
    parts = file.readline().split()
    k = int(parts[0])
    t = int(parts[1])
    dna = []
    for i in range(t):
        dna.append(file.readline().strip())
    return (dna,k,t)

def repeatedRandomizedMotifSearch( k, t, dna ):
    bestScore = float('inf')
    bestMotifs = []
    i = 0
    while True:
        motifs = randomizedMotifSearch(k,t,dna)
        score = Score(motifs)
        if score < bestScore:
            bestScore = score
            bestMotifs = motifs
            i = 0
        else:
            i += 1
        if i > 100:
            break
    return bestMotifs

def randomizedMotifSearch( k, t, dna ):
    bestMotifs = randomMotifs(dna,k)
    bestScore = Score(bestMotifs)
    while True:
        profile = profileFromMotifs(bestMotifs,1)
        motifs = motifsFromProfile(dna,profile)
        score = Score(motifs)
        if score < bestScore:
            bestMotifs = motifs
            bestScore = score
        else:
            return bestMotifs

def Score( motifs ):
    score = 0
    for count in countsFromMotifs(motifs,0):
        score += sum(count) - max(count)
    return score

def motifsFromProfile( dna, profile ):
    return [bestKmerForProfile(seq, profile) for seq in dna]

def bestKmerForProfile( seq, profile ):
    k = len(profile)
    bestProb = -1
    bestKmer = ''
    for start in range(len(seq)-k+1):
        kmer = seq[start:start+k]
        prob = probKmerInProfile(kmer, profile)
        if prob > bestProb:
            bestProb = prob
            bestKmer = kmer
    return bestKmer

def probKmerInProfile( kmer, profile ):
    prob = 1.0
    for i in range(len(kmer)):
        prob *= profile[i][acidToIndex(kmer[i])]
    return prob

def profileFromMotifs( motifs, initCount ):
    counts = countsFromMotifs(motifs,initCount)
    profile = []
    for count in counts:
        total = float(sum(count))
        probs = [c/total for c in count]
        profile.append(probs)
    return profile

def countsFromMotifs( motifs, initCount ):
    k = len(motifs[0])
    for motif in motifs:
        assert k == len(motif)
    counts = []
    for i in range(k):
        currCount = [initCount] * 4
        for motif in motifs:
            currCount[acidToIndex(motif[i])] += 1
        counts.append(currCount)
    return counts

def randomMotifs( dna, k ):
    return [randomKmer(seq,k) for seq in dna]

def randomKmer( seq, k ):
    start = random.randint(0, len(seq)-k)
    return seq[start:start+k] 

(dna,k,t) = readInput(open('dataset.txt'))
R = 1000 # how many times to repeat
bestMotifs = repeatedRandomizedMotifSearch(k,t,dna)
for motif in bestMotifs:
    print (motif)
