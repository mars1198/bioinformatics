aminoacidMass = {'G':57, 'A':71, 'S':87, 'P':97, 'V':99, 'T':101, 'C':103, 'I':113, 'L':113, 'N':114, 'D':115, 'K':128, 'Q':128, 'E':129, 'M':131, 'H':137, 'F':147, 'R':156, 'Y':163, 'W':186}
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

#Reading the data
with open('dataset_102_3.txt') as f:
    peptide, spectrum = [line.strip() if i==0 else map(int,line.strip().split()) for i, line in enumerate(f.readlines())]
    
#Calling the function to compute score
print (score_peptide(peptide, spectrum))
