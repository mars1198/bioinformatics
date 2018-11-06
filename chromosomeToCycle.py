def chromosomeToCycle(chromosome):
    """ Input: A chromosome Chromosome containing n synteny blocks.
        Output: The sequence Nodes of integers between 1 and 2n resulting from applying ChromosomeToCycle
        to Chromosome."""
    nodes = [0]*(2*len(chromosome))
    for j in range(len(chromosome)):
        i = chromosome[j]
        if i > 0:
            nodes[2*j] = 2*i - 1
            nodes[2*j + 1] = 2*i
        if i < 0:
            nodes[2*j] = -2*i
            nodes[2*j + 1] = -2*i - 1
    return nodes

f = open('dataset_8222_4.txt')
chromosome = list(map(int, f.read().strip().lstrip('(').rstrip(')').split()))
ans = chromosomeToCycle(chromosome)
output = '(' + ' '.join(str(i) for i in ans) + ')'
print (output)
