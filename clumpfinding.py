from collections import defaultdict
def ClumpFinding(genome, k, L, t):
    lookup = defaultdict(list)
    result = set()

    for cursor in range(len(genome) - k + 1):
        seg = genome[cursor:cursor + k]

        # remove prior positions of the same segment
        # if they are more than L distance far
        while lookup[seg] and cursor + k - lookup[seg][0] > L:
            lookup[seg].pop(0)

        lookup[seg].append(cursor)
        if len(lookup[seg]) == t:
            result.add(seg)

    return result
