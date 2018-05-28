def ProfileMostProbablePattern(Text, k, Profile):
    # insert your code here. Make sure to use Pr(Text, Profile) as a subroutine!
	matchmax=-1
	ProbablePattern=""
	for i in range(len(Text)-k+1):
		Pattern = Text[i:i+k]
		if Pr(Pattern, Profile) > matchmax:
			matchmax=Pr(Pattern, Profile)
			ProbablePattern=Pattern       
        
	return ProbablePattern


def score(motifs):
    '''Returns the score of the given list of motifs.'''
    columns = [''.join(seq) for seq in zip(*motifs)]
    max_count = sum([max([c.count(nucleotide) for nucleotide in 'ACGT']) for c in columns])
    return len(motifs[0])*len(motifs) - max_count


def profile(motifs):
    '''Returns the profile of the dna list motifs.'''
    columns = [''.join(seq) for seq in zip(*motifs)]
    return [[float(col.count(nuc)) / float(len(col)) for nuc in 'ACGT'] for col in columns]


def greedy_motif_search(dna_list, k, t):
    '''Runs the Greedy Motif Search algorithm and retuns the best motif.'''
    # Initialize the best score as a score higher than the highest possible score.
    best_score = t*k

    # Run the greedy motif search.
    for i in range(len(dna_list[0])-k+1):
        # Initialize the motifs as each k-mer from the first dna sequence.
        motifs = [dna_list[0][i:i+k]]

        # Find the most probable k-mer in the next string.
        for j in range(1, t):
            current_profile = profile(motifs)
            motifs.append(profile_most_probable_kmer(dna_list[j], k, current_profile))

        # Check to see if we have a new best scoring list of motifs.
        current_score = score(motifs)
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs

    return best_motifs


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('dataset.txt') as input_data:
            k, t = map(int, input_data.readline().split())
            dna_list = [line.strip() for line in input_data]

    # Run the Greedy Motif Search.
    best_motifs = greedy_motif_search(dna_list, k, t)
    for word in best_motifs:
        print (word)
    

    # Print and save the answer.
    #print (best_motifs)


if __name__ == '__main__':
    main()
