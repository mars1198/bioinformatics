import numpy as np
f = open('blosum62_affine.txt', 'r')
score = [line.strip().split() for line in f]
alphabet = score[0]
blosum62 = np.array([i[1:] for i in score[1:]], dtype = np.float64)

def affine_globalAlign(x, y, score_matrix, sigma, epsilon):
    """Returns three levels for global alignment graph with affine gap penalty. 
    Affine penalty for a gap of length k as σ + ε · (k − 1).
    sigma - gap opening penalty; epsilon- gap extension penalty"""
    
    #Initialize the numpy array
    lower = np.zeros((len(x) + 1, len(y) + 1), dtype = np.float64)
    middle = np.zeros((len(x) + 1, len(y) + 1), dtype = np.float64)
    upper = np.zeros((len(x) + 1, len(y) + 1), dtype = np.float64)
    
    #Fill in the first column of three levels
    for i in range(1, len(x) + 1):
        lower[i,0] = -sigma -(i-1)*epsilon
        middle[i,0] = -sigma -(i-1)*epsilon
        upper[i,0] = -float('inf')
        
    #Fill in the first row of three levels
    for j in range(1, len(y) + 1):
        lower[0,j] = -float('inf')
        middle[0,j] = -sigma -(j-1)*epsilon
        upper[0,j] = -sigma -(j-1)*epsilon
    
    # Middle level- diagonal edges of weight score(x_i, y_j) representing matches and mismatches. 
    #Lower level- only vertical edges with weight −ε to represent gap extensions in x
    #Upper level- only horizontal edges with weights −ε to represent gap extensions in y
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            lower[i, j] = max(lower[i-1, j] - epsilon, middle[i-1, j] - sigma)
            upper[i, j] = max(upper[i, j-1] - epsilon, middle[i, j-1] - sigma)
            middle[i, j] = max(lower[i, j], 
                               middle[i-1, j-1] + score_matrix[alphabet.index(x[i-1]), alphabet.index(y[j-1])], 
                               upper[i, j])
                  
    return lower, middle, upper

import numpy as np
def traceback(lower, middle, upper, x, y, score_matrix, sigma, epsilon):
    """Traceback in the three level matrix to get the global alignment with affine gap penalty"""
    #get i,j for maximal cell
    i, j = len(x), len(y)
    alx, aly = [], []
    traceback = middle #Start traceback in the middle
    while i*j != 0:
        if traceback is middle:
            ls = lower[i,j]
            us = upper[i,j]
            ms = middle[i-1, j-1] + score_matrix[alphabet.index(x[i-1]), alphabet.index(y[j-1])]
            max_score = max(ls, us, ms)
            if max_score == ms:
                alx.append(x[i-1]); aly.append(y[j-1])
                i -= 1; j -= 1 
                traceback = middle
            elif max_score == ls:
                traceback = lower
            else:
                traceback = upper
        
        elif traceback is lower:
            ls = lower[i-1, j] - epsilon
            ms = middle[i-1, j] - sigma
            max_score = max(ls, ms)
            if max_score == ls:
                alx.append(x[i-1]); aly.append('-')
                i -= 1
                traceback = lower
            else:
                alx.append(x[i-1]); aly.append('-')
                i -= 1
                traceback = middle
                
        elif traceback is upper:
            us = upper[i, j-1] - epsilon
            ms = middle[i, j-1] - sigma
            max_score = max(us, ms)
            if max_score == us:
                alx.append('-'); aly.append(y[j-1]) 
                j -= 1
                traceback = upper
            else:
                alx.append('-'); aly.append(y[j-1])
                j -= 1
                traceback = middle
                
    alignment = map(lambda x: ''.join(x), [alx[::-1], aly[::-1]])
    return alignment

x, y = [i.strip() for i in open('dataset_249_8.txt', 'r')]
lower, middle, upper = affine_globalAlign(x, y, blosum62, 11, 1)
algn = traceback(lower, middle, upper, x, y, blosum62, 11, 1)
print (int(middle[len(x), len(y)]))
print ('\n'.join(algn))
