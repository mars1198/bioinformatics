def Profile(Motifs):
    count = {} # initializing the count dictionary
    profile = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)

    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    ## divide the number of motif strings to get frequency
    for letter in count.keys():
        profile[letter] = [x/ float(t) for x in count[letter]]
    return profile
