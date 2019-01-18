import sys

#NUMBER2SYMBOL = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

def hamming_distance(p, q):
#    return len(list(filter(lambda x: x[0] != x[1], zip(p, q))))
    return sum(c1 != c2 for c1, c2 in zip(p, q))
def distance_between_pattern_and_strings(pattern, dna):
    k = len(pattern)
    distance = 0
    for text in dna:
        min_hamming_distance = sys.maxsize
        for i in range(len(text) - k + 1):
            pattern_in_text = text[i:i + k]
            min_hamming_distance = min(min_hamming_distance, hamming_distance(pattern, pattern_in_text))
        distance += min_hamming_distance
    return distance

def number_to_pattern(index, k):
    if k == 1:
        return NUMBER2SYMBOL(index)
    return number_to_pattern(index//4, k-1) + NUMBER2SYMBOL(index%4)
#    prefix_index, r = divmod(index, 4)
#    prefix_pattern = number_to_pattern(prefix_index, k - 1)
#    symbol = NUMBER2SYMBOL[r]
#    return prefix_pattern + symbol
    
def NUMBER2SYMBOL(x):
    if x == 0:
        return 'A'
    if x == 1:
        return 'C'
    if x == 2:
        return 'G'
    if x == 3:
        return 'T'
    
    
def median_string(dna, k):
    distance = sys.maxsize
    for i in range(4 ** k - 1):
        pattern = number_to_pattern(i, k)
        if distance > distance_between_pattern_and_strings(pattern, dna):
            distance = distance_between_pattern_and_strings(pattern, dna)
            median = pattern
    return median

def main():

    k = 3
    dna = ['AAATTGACGCAA', 'GACGACCACGTT', 'CGTCAGCGCCTG', 'GCTGAGCACCGG', 'AGTACGGGACAG']
    print(median_string(dna, k))

if __name__ == '__main__':
    main()
