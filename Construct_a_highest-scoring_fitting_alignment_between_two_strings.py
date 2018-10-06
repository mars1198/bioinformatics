import numpy as np
alphabet = ['A', 'C', 'G', 'T', '-']
score = np.array([[1, -1, -1, -1, -1],[-1, 1, -1, -1, -1],[-1, -1, 1, -1, -1],[-1, -1, -1, 1, -1],[-1, -1, -1, -1, -1]], 
                 dtype = 'int')
score

def fittingAlignment(p, t, score):
    """ Calculate global alignment value of sequences x and y using
        dynamic programming.  Return global alignment value. """
    
    D = np.zeros((len(p)+1, len(t)+1), dtype=int)
    # Note: First row gets zeros.  First column initialized as usual.
    for i in range(1, len(p) + 1):
        D[i,0] = D[i-1,0] + score[alphabet.index(p[i-1]), alphabet.index('-')]
    for i in range(1, len(p)+1):
        for j in range(1, len(t)+1):
            horz = D[i, j-1] + score[alphabet.index('-'), alphabet.index(t[j-1])]
            vert = D[i-1, j] + score[alphabet.index(p[i-1]), alphabet.index('-')]
            diag = D[i-1, j-1] + score[alphabet.index(p[i-1]), alphabet.index(t[j-1])]
            D[i,j] = max(horz, vert, diag)
    max_score = D[-1,].max()
    return D, max_score

def traceback(D, p, t, score):
    ''' Find and return the alignment of a substring of t to p by 
        trace back from given cell in global-alignment matrix D .  
        A highest-scoring fitting alignment between v and w. 
        If multiple alignments tie for best, we report the leftmost. '''
    # get i, j for maximal cell
    for index in range(len(t)):
        if D[-1,index] == D[-1,].max():
            max_index = index
    i, j = len(p), max_index
    alp, alt = [], []
    while i > 0:
        diag, horz, vert = -float('inf'), -float('inf'), -float('inf')
        if i > 0 and j > 0:
            diag = D[i-1, j-1] + score[alphabet.index(p[i-1]), alphabet.index(t[j-1])]
        if i > 0:
            vert = D[i-1, j] + score[alphabet.index(p[i-1]), alphabet.index('-')]
        if j > 0:
            horz = D[i, j-1] + score[alphabet.index('-'), alphabet.index(t[j-1])]
        if diag >= vert and diag >= horz:
            alp.append(p[i-1]); alt.append(t[j-1])
            i -= 1; j -= 1 
        elif vert >= horz:
            alp.append(p[i-1]); alt.append('-')
            i -= 1
        else:
            alp.append('-'); alt.append(t[j-1])
            j -= 1
    alignment = map(lambda x: ''.join(x), [alt[::-1], alp[::-1]])
    return alignment


t,p = [i.strip() for i in open('dataset_248_5.txt', 'r')]
D, max_score = fittingAlignment(p, t, score)
print (max_score)
algn = traceback(D, p, t, score)
print ('\n'.join(algn))
