def expand(leaderboard, frequent_aa):
    """Expands each peptide/aminoacid in leaderboard by all 18 aminoacid masses."""
    return [i+(j,) for i in leaderboard for j in frequent_aa]

def cyclicSpectrum(peptide):
    """Input: (aminoacid masses)
     Output: The cyclic spectrum of Peptide."""
    prefixMass = [0]*((len(peptide)+1))
    for i in range(len(peptide)):
        prefixMass[i+1] = prefixMass[i] + peptide[i]
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
     Input: (aa masses) and a collection of integers Spectrum. 
     Output: The score of Peptide against Spectrum, Score(Peptide, Spectrum)."""
    spectrum_peptide = cyclicSpectrum(peptide)
    c1, c2 = Counter(spectrum_peptide), Counter(spectrum)
    return sum([min(n, c2[k]) for k,n in c1.items()])

def linearSpectrum(peptide):
    """Input: An amino acid string Peptide.
     Output: The linear spectrum of Peptide."""
    prefixMass = [0]*((len(peptide)+1))
    for i in range(len(peptide)):
        prefixMass[i+1] = prefixMass[i] + peptide[i]
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
    leaderboard = expand([()], aa)
    leaderpeptide = ()
    parentmass = max(spectrum)
    while len(leaderboard) > 0:
        leaderboard = expand(leaderboard, aa)
        for peptide in leaderboard[:]:
            mass = sum(peptide)
            if mass == parentmass:
                if score_peptide(peptide, spectrum) > score_peptide(leaderpeptide, spectrum):
                    leaderpeptide = peptide
            elif mass > parentmass:
                leaderboard.remove(peptide)
        leaderboard = trim_leaderboard(leaderboard, spectrum, N)   
    return leaderpeptide

def convolution(spectrum):
    
    """Input: A collection of integers Spectrum.
     Output: The list of elements in the convolution of Spectrum. If an element has
     multiplicity k, it should appear exactly k times; you may return the elements in any order."""
    
    spectrum = sorted(spectrum)
    return [i-j for i in spectrum for j in spectrum if i-j > 0]

from collections import Counter
def convolution_cyclopeptide_sequencing(M, N, spectrum):
    
    #Get the sorted convolution
    convoluted_spectrum = sorted(convolution(spectrum))
    
    #Select elements from convolution betweeen 57 and 200
    aa = [i for i in convoluted_spectrum if 57<=i<=200]
    
    #Select the M most frequent elements between 57 and 200 in the convolution with ties
    if len(aa) < M:
        frequent_aa = aa
    else:
        c = Counter(aa).most_common()
        frequent_aa = [k for (k,v) in c if v >= c[M-1][1]]
    
    leaderboard = expand([()], frequent_aa)
    leaderpeptide = ()
    parentmass = max(spectrum)
    while len(leaderboard) > 0:
        leaderboard = expand(leaderboard, frequent_aa)
        for peptide in leaderboard[:]:
            mass = sum(peptide)
            if mass == parentmass:
                if score_peptide(peptide, spectrum) > score_peptide(leaderpeptide, spectrum):
                    leaderpeptide = peptide
            elif mass > parentmass:
                leaderboard.remove(peptide)
        leaderboard = trim_leaderboard(leaderboard, spectrum, N)   
    return leaderpeptide

f = open('dataset_104_7.txt')
spectrum = list(map(int, f.read().strip().split()))

output = convolution_cyclopeptide_sequencing(20, 385, spectrum)
#Get output in desired format
print ('-'.join(str(i) for i in output))
