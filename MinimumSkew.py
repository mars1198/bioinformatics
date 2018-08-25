def MinimumSkew(Genome):
    positions = [] # output variable
    skew = Skew(Genome)
    minimum = min(skew.values())
    for i in range(len(Genome)):
        if skew[i] == minimum:
            positions.append(i)
    return positions

# Input:  A String Genome
# Output: SkewArray(Genome)
# HINT:   This code should be taken from the last Code Challenge.
def Skew(Genome):
    skew = {} #initializing the dictionary
    skew[0] = 0
    for i in range(len(Genome)):
        if Genome[i] == "C":
            skew[i + 1] = skew[i]  -1
        elif Genome[i] == "G":
            skew[i +1] = skew[i] +1
        else:
            skew[i+1] = skew[i]
    # your code here
    return skew
