import random
# then, copy Pr, Normalize, and WeightedDie below this line
def Normalize(Probabilities):
    normalized = {}
    sum_prob = sum(Probabilities.values())
    keysProb = list(Probabilities)
    for i in range(len(Probabilities)):
        normalized[keysProb[i]] = Probabilities[keysProb[i]]/sum_prob
    return normalized

def Pr(Text, Profile):
    p = 1
    for i in range(len(Text)):
        p = p * Profile[Text[i]][i]
    return p

def WeightedDie(Probabilities):
    n = random.uniform(0, 1)
    for p in Probabilities:
        n -= Probabilities[p]
        if n <= 0:
            return p

# Input:  A string Text, a profile matrix Profile, and an integer k
# Output: ProfileGeneratedString(Text, profile, k)
def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {}
    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)
