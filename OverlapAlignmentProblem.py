import numpy as np
alphabet = ['A', 'C', 'G', 'T', '-']
score = np.array([[1, -2, -2, -2, -2],[-2, 1, -2, -2, -2],[-2, -2, 1, -2, -2],[-2, -2, -2, 1, -2],[-2, -2, -2, -2, -2]], 
                 dtype = 'int')
score

def overlapAlignment(x, y, score):
    """Calculate the score of an optimal overlap alignment of suffix of x and prefix of y. 
    The maximum score for overlap alignment"""
    
    D = np.zeros((len(x)+1, len(y)+1), dtype=int)
    for j in range(1, len(y) + 1):
        D[0,j] = D[0, j-1] + score[alphabet.index('-'), alphabet.index(y[j-1])]
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            horz = D[i, j-1] + score[alphabet.index('-'), alphabet.index(y[j-1])]
            vert = D[i-1, j] + score[alphabet.index(x[i-1]), alphabet.index('-')]
            diag = D[i-1, j-1] + score[alphabet.index(x[i-1]), alphabet.index(y[j-1])]
            D[i,j] = max(horz, vert, diag)
    max_score = D[-1,].max()
    return D, max_score

def traceback(D, x, y, score):
    ''' Find and return the alignment of a substring of t to p by 
        trace back from given cell in global-alignment matrix D .  
        A highest-scoring fitting alignment between v and w. 
        If multiple alignments tie for best, we report the leftmost. '''
    # get i, j for maximal cell
    max_score = D[-1,].max()
    for index in reversed(range(len(y))):
        if D[-1,index] == max_score:
            max_index = index
    i, j = len(x), max_index
    alp, alt = [], []
    while j > 0:
        diag, horz, vert = -float('inf'), -float('inf'), -float('inf')
        if i > 0 and j > 0:
            diag = D[i-1, j-1] + score[alphabet.index(x[i-1]), alphabet.index(y[j-1])]
        if i > 0:
            vert = D[i-1, j] + score[alphabet.index(x[i-1]), alphabet.index('-')]
        if j > 0:
            horz = D[i, j-1] + score[alphabet.index('-'), alphabet.index(y[j-1])]
        if diag >= vert and diag >= horz:
            alp.append(x[i-1]); alt.append(y[j-1])
            i -= 1; j -= 1 
        elif vert >= horz:
            alp.append(x[i-1]); alt.append('-')
            i -= 1
        else:
            alp.append('-'); alt.append(y[j-1])
            j -= 1
    alignment = map(lambda x: ''.join(x), [alp[::-1], alt[::-1]])
    return alignment

x, y = [i.strip() for i in open('dataset_248_7.txt', 'r')]
D, max_score = overlapAlignment(x, y, score)
print (max_score)
algn = traceback(D, x, y, score)
print ('\n'.join(algn))
