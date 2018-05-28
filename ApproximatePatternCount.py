import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

Pattern = 'GATAGCT'
Text = 'AAACTTAAGCTAATTACCGACAAATTCCTTTTAAATAGATGGTCCTCGCGCACTGAGCCCCTCTCGGCCCGGTTCATCGTCTATCATCGCATCTAAACTCGATTGCTTAGTAGTCCAGCGGGCATGAGCATACAGAGACTGCCTTTAGGGCATCAACCTCTTCTTGCCGCGAACGATAGCTGGCGGCTCCGGCGTTGAGGTTGCCTGATGAGCAAAAAAGCGTATGTAACAGTTCGCCGCACCCCGAACCCCGGCTTCGATCAGCTTTCCTCGTCGCTTTGGTAGATGTGGAATGTTGAGTGCTGCATTCGCACAGGGAAAC'
d = 3

def ApproximatePatternCount(Pattern, Text, d):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:len(Pattern)+1] == Pattern:
            count += 1
        elif Text[i:len(Pattern)+1] != Pattern:
            if HammingDistance(Text[i:i+len(Pattern)], Pattern) <= d:
                count += 1
    return count

def HammingDistance(p, q):
    # your code here
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count

print (ApproximatePatternCount(Pattern, Text, d))
