def IterativebackTrack(Tr,X,Y):

    m = len(X)   # up down sequence is ordered on Column
    n = len(Y)   #left right, sequence is ordered on row


    backtrackSeq1=""
    backtrackSeq2=""

    while m > 0 and n >= 0:
        if Tr[m][n]=='DIG': # diagonal
            m=m-1
            n=n-1
            backtrackSeq1=backtrackSeq1 + X[m]
            backtrackSeq2=backtrackSeq2 + Y[n]


        elif Tr[m][n]=='D':  # down
            m=m-1
            backtrackSeq1=backtrackSeq1 + X[m]
            backtrackSeq2=backtrackSeq2 + '-'

        else:  # right 'R'
            n=n-1
            backtrackSeq1=backtrackSeq1 + '-'
            backtrackSeq2=backtrackSeq2 + Y[n]

    finalseq1= backtrackSeq1[::-1] # reverse the sequence so its in the correct direction
    finalseq2= backtrackSeq2[::-1]
    print (finalseq1)
    print (finalseq2)


def global_Align(X, Y,matrix,indelPenalty):
    #indelPenalty= -5   # set this

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

            C[i][j] = max(C[i][j-1]+indelPenalty, C[i-1][j]+indelPenalty,matchMis)  # take max score from previous columns, or from previous row same column (left, or above) or from match/mismatch
                            #right                  #down                   #diag
            if C[i][j]==matchMis:
                Tr[i][j]='DIG'
            elif C[i][j]==C[i][j-1]+indelPenalty:
                Tr[i][j]='R'
            else:
                Tr[i][j]='D'

    print ("")
    #print C
    #print Tr

    print ("Score ", C[m][n])
    IterativebackTrack(Tr,X,Y)

def main(argv):
    with open('dataset_250_14.txt', "r") as fstream:
        sequence1=fstream.readline().rstrip()
        sequence2=fstream.readline().rstrip()

    print (sequence1)
    print (sequence2)

    matrix = matlist.blosum62


    global_Align(sequence1,sequence2,matrix,-5)



if __name__== "__main__":
    main(argv)
