def ReverseComplement(Pattern):
    rev= Reverse(Pattern)
    revComp = Complement(rev)
    return revComp

# Copy your Reverse() function here.
def Reverse(Pattern):
    rev = ""
    for i in range(len(Pattern)):
        rev = rev + Pattern[len(Pattern) -i -1]
    return rev

# Copy your Complement() function here.
def Complement(Pattern):
    comp = '' # output variable
    pair_dict= {"A":"T", "C":"G", "T":"A", "G":"C" }
    for nucleotide in Pattern:
        comp = comp + pair_dict[nucleotide]
    return comp
