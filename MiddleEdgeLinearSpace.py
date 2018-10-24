from sys import  argv
from Bio.SubsMat import MatrixInfo as matlist

"""
CODE CHALLENGE: Solve the Middle Edge in Linear Space Problem (for protein strings).
     Input: Two amino acid strings.
     Output: A middle edge in the alignment graph in the form "(i, j) (k, l)", where (i, j) connects to (k, l).
     To compute scores, use the BLOSUM62 scoring matrix and a (linear) indel penalty equal to 5.
Sample Input:
     PLEASANTLY
     MEASNLY
Sample Output:
     (4, 3) (5, 4)
"""
def global_Align(X, Y,matrix,indelPenalty):
    m = len(X)
    n = len(Y)

    print ("")

    C = [[0 for j in range(n+1)] for i in range(m+1)]  # 2D list-zero out the list  # this is the score list
    Tr= [[0 for j in range(n+1)] for i in range(m+1)]  # 2D list-zero out the list   # this is the traceback list

    for i in range (1, n+1):   # initalize row 0
        Tr[0][i]='R'
        C[0][i]=indelPenalty+ C[0][i-1]

    for j in range(1,m+1):    # initialize column 0
        Tr[j][0]='D'
        C[j][0]=indelPenalty + C[j-1][0]


    for i in range(1, m+1):
        for j in range(1, n+1):
            if (X[i-1],Y[j-1]) in matrix:
                matchMis = C[i-1][j-1] + matrix[(X[i-1],Y[j-1])]  # score from match or mismatch
            else:
                matchMis = C[i-1][j-1] + matrix[(Y[j-1],X[i-1])]   # score from match or mismatch

            C[i][j] = max(C[i][j-1]+indelPenalty, C[i-1][j]+indelPenalty,matchMis)  # take max score from previous columns, or from previous row same column (left, or above) or from match/mismatch(diag)
                            #right                  #down                   #diag
            if C[i][j]==matchMis:
                Tr[i][j]='DIG'
            elif C[i][j]==C[i][j-1]+indelPenalty:
                Tr[i][j]='R'
            else:
                Tr[i][j]='D'

    print ("")

    print (m, m/2)
    print (n, n/2)


    middleCord_n=int(n/2+1)   # middle value
    maxValue=0
    for i in range(0,m):
        if C[i][middleCord_n]>maxValue:
            maxValue=C[i][middleCord_n]
            middleCord_m = i

    middleString= str(middleCord_m)+', '+str(middleCord_n)

    prev_middleCord_n=middleCord_n-1   # left connection to middle
    maxValue=0
    for i in range(0,m):
        if C[i][prev_middleCord_n]>maxValue:
            maxValue=C[i][prev_middleCord_n]
            prev_middleCord_m = i

    prev_middleString=str(prev_middleCord_m) + ', ' + str(prev_middleCord_n)


    print (prev_middleString, ' ', middleString)

def main(argv):
    with open('input.txt', "r") as fstream:
        sequence1=fstream.readline().rstrip()
        sequence2=fstream.readline().rstrip()

    print (sequence1)
    print (sequence2)

    matrix = matlist.blosum62


    global_Align(sequence1,sequence2,matrix,-5)



if __name__== "__main__":
    main(argv)
