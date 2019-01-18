import sys
from operator import mul
import functools

dna = 'ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'

k = 5

profile = [[0.2, 0.4, 0.3, 0.1], [0.2, 0.3, 0.3, 0.2], [0.3, 0.1, 0.5, 0.1], [0.2, 0.5, 0.2, 0.1], [0.3, 0.1, 0.4, 0.2]]


def calculate_probablity(kmer):
    t = []
    for i in range(len(kmer)):
        if kmer[i] == 'A':
            t.append(profile[i][0])
        elif kmer[i] == 'C':
            t.append(profile[i][1])
        elif kmer[i] == 'G':
            t.append(profile[i][2])
        elif kmer[i] == 'T':
            t.append(profile[i][3])
    return functools.reduce(mul, t, 1)


best_pattern = ""
best_probability = 0.0000
for i in range(len(dna) - k + 1):
    kmer = dna[i:i+k]
    if calculate_probablity(kmer) > best_probability:
        best_pattern = kmer
        best_probability = calculate_probablity(kmer)

print (best_pattern)
