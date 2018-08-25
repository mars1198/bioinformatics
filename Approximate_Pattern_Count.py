# Input:  Strings Pattern and Text, and an integer d
# Output: The number of times Pattern appears in Text with at most d mismatches
def ApproximatePatternCount(Pattern, Text, d):
    positions = [] # initializing list of positions
    for i in range(len(Text)- len(Pattern) +1):
        if HammingDistance(Pattern, Text[i:i + len(Pattern)]) <= d:
            positions.append(i)
    return len(positions)


# Insert your HammingDistance function on the following line.
def HammingDistance(p, q):
    # your code here
    dist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            dist +=1
    return dist

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
print(ApproximatePatternCount(lines[0],lines[1],int(lines[2])))
