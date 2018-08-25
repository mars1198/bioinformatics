def Normalize(Probabilities):
    normalized = {}
    sum_prob = sum(Probabilities.values())
    keysProb = list(Probabilities)
    for i in range(len(Probabilities)):
        normalized[keysProb[i]] = Probabilities[keysProb[i]]/sum_prob
    return normalized
