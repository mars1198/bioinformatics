# fill in your FrequentWords() function here along with any subroutines you need.
def FrequentWords(Text, k):
    counts = {}
    for i in range(len(Text)-k+1):
        if Text[i:i+k] not in counts:
            counts[Text[i:i+k]] = 0
        counts[Text[i:i+k]] += 1
    m = max(counts.values())
    out = []
    for kmer in counts:
        if counts[kmer] == m:
            out.append(kmer)
    return out
