def Complement(Pattern):
    comp = '' # output variable
    pair_dict= {"A":"T", "C":"G", "T":"A", "G":"C" }
    for nucleotide in Pattern:
        comp = comp + pair_dict[nucleotide]
    return comp
