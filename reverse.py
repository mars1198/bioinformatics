def Reverse(Pattern):
    rev = ""
    for i in range(len(Pattern)):
        rev = rev + Pattern[len(Pattern) -i -1]
    return rev
