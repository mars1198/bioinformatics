aminoacid = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'L', 'N', 'D', 'K', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']
aminoacidMass = {'G':57, 'A':71, 'S':87, 'P':97, 'V':99, 'T':101, 'C':103, 'L':113, 'N':114, 'D':115, 'K':128, 'E':129, 'M':131, 'H':137, 'F':147, 'R':156, 'Y':163, 'W':186}
def expand(leaderboard):
    """Expands each peptide/aminoacid in leaderboard by all 18 aminoacids with distinct masses."""
    expanded = []
    for i in leaderboard:
        expanded += [i+j for j in aminoacidMass.keys()]
    return expanded   

def mass(peptide):
    """Calculates the mass of peptide using the aminoacidMass dictionary"""
    massOfPeptide = 0
    for i in peptide:
        massOfPeptide += aminoacidMass[i]
    return massOfPeptide

def cyclicSpectrum(peptide):
    """Input: An amino acid string Peptide.
     Output: The cyclic spectrum of Peptide."""
    prefixMass = [0]*((len(peptide)+1))
    for i in range(len(peptide)):
        prefixMass[i+1] = prefixMass[i] + aminoacidMass[peptide[i]]
    peptideMass = prefixMass[len(peptide)]
    cyclic_spectrum = [0]
    for i in range(len(prefixMass)-1):
        for j in range(i+1, len(prefixMass)):
            cyclic_spectrum.append(prefixMass[j] - prefixMass[i])
            if i > 0 and j < (len(prefixMass)-1):
                cyclic_spectrum.append(peptideMass - (prefixMass[j] - prefixMass[i]))
    return sorted(cyclic_spectrum) 

from collections import Counter
def score_peptide(peptide, spectrum):
    """Cyclopeptide Scoring Problem: Compute the score of a cyclic peptide against a spectrum.
     Input: An amino acid string Peptide and a collection of integers Spectrum. 
     Output: The score of Peptide against Spectrum, Score(Peptide, Spectrum)."""
    spectrum_peptide = cyclicSpectrum(peptide)
    c1, c2 = Counter(spectrum_peptide), Counter(spectrum)
    return sum([min(n, c2[k]) for k,n in c1.items()])

def linearSpectrum(peptide):
    """Input: An amino acid string Peptide.
     Output: The linear spectrum of Peptide."""
    prefixMass = [0]*((len(peptide)+1))
    for i in range(len(peptide)):
        prefixMass[i+1] = prefixMass[i] + aminoacidMass[peptide[i]]
    #print 'prefixMass', prefixMass
    linear_spectrum = [0]
    for i in range(len(prefixMass)-1):
        for j in range(i+1, len(prefixMass)):
            linear_spectrum.append(prefixMass[j] - prefixMass[i])
    return sorted(linear_spectrum) 

def score_linear_peptide(peptide, spectrum):
    """Compute the score of a linear peptide with respect to a spectrum.
     Input: An amino acid string Peptide and a collection of integers Spectrum.
     Output: The linear score of Peptide with respect to Spectrum, LinearScore(Peptide, Spectrum)."""
    spectrum_linear_peptide = linearSpectrum(peptide)
    c3, c4 = Counter(spectrum_linear_peptide), Counter(spectrum)
    return sum([min(n, c4[k]) for k,n in c3.items()])

def trim_leaderboard(leaderboard, spectrum, N):
    """Input: A collection of peptides Leaderboard, a collection of integers Spectrum, and an integer N.
     Output: The N highest-scoring linear peptides on Leaderboard with respect to Spectrum."""
    scores =  [[score_linear_peptide(peptide, spectrum), peptide] for peptide in leaderboard]
    sorted_scores = sorted(scores, reverse = True)
    if len(leaderboard) <= N:
        return [i[1] for i in sorted_scores]
    else:
        return [i[1] for i in sorted_scores if i[0] >= sorted_scores[int(N)-1][0]]

def leaderboard_cyclopeptide_sequencing(spectrum, N):
    """ Input: An integer N and a collection of integers Spectrum.
     Output: LeaderPeptide after running LEADERBOARDCYCLOPEPTIDESEQUENCING(Spectrum, N)"""
    leaderboard = aminoacid
    leaderpeptide = ''
    parentmass = max(spectrum)
    while len(leaderboard) > 0:
        leaderboard = expand(leaderboard)
        for peptide in leaderboard[:]:
            if mass(peptide) == parentmass:
                if score_peptide(peptide, spectrum) > score_peptide(leaderpeptide, spectrum):
                    leaderpeptide = peptide
            elif mass(peptide) > parentmass:
                leaderboard.remove(peptide)
        leaderboard = trim_leaderboard(leaderboard, spectrum, N)   
    return leaderpeptide

f = open('dataset_102_8.txt')
N, spectrum = [int(line.strip()) if i==0 else list(map(int,line.strip().split())) for i, line in enumerate(f.readlines())]

print (spectrum)
ans = leaderboard_cyclopeptide_sequencing(spectrum, N)

print ('-'.join(str(i) for i in map(lambda i: aminoacidMass[i], ans)))
