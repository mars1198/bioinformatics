from itertools import product

def hamming( s, t ):
    return sum([s[i] != t[i] for i in range(len(s))])


def median_string(k, dna_list):
    # Initialize the best pattern score as one greater than the maximum possible score.
    best_score = k*len(dna_list) + 1

    # Check the scores of all k-mers.
    for pattern in product('ACGT', repeat=k):
        current_score = sum([motif_score(''.join(pattern), dna) for dna in dna_list])
        if current_score < best_score:
            best_score = current_score
            best_pattern = ''.join(pattern)

    return best_pattern


def motif_score(pattern, motif):
    '''Returns the score of d(pattern, motif).'''
    return min([hamming(motif[i:i+len(pattern)], pattern) for i in range(len(motif)-len(pattern)+1)])


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
   
    k = 6
    dna_list = ['CCTTGCTTACTGTAGACAACACATTCAAAACGGCTTTTGGTG', 'AGTCCATTACTGCCGGACAGATTTACATGAACTCTTACAAGA', 'TCACTGCTTTAGACAGGACCCAGGACCGAGAGTTGTAACGGG', 'CCATCACCGAGCTCTCAATGACTGTTAGTAATGTGATCAAAC', 'TAACTGCATTTAAAACGATCATCGAGACTTTCCCACTAGAGG', 'GGCGAGCCGCGCCGAGTTTGACTGGTCCAAGGGTTTTTGTAA', 'ATAGAAGATGTGGTGTCCTTACTGCGACGTATACTCTTGGGG', 'TGTTGGAACGGTTGACTGGAAGCGGGAAGTCGATTACATGGC', 'GAGATCAATGATTTTCCGGAGAGGGGACTGTAACTGAGAACA', 'CTCTCGGGCTACTGCCGAACCGTTTTACTGTTCATTCTAAAG']

    # Get the best pattern.
    best_pattern = median_string(k, dna_list)

    # Print and save the answer.
    print (best_pattern)


if __name__ == '__main__':
    main()
