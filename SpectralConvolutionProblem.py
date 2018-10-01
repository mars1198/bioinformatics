def convolution(spectrum):
    
    """Input: A collection of integers Spectrum.
     Output: The list of elements in the convolution of Spectrum. If an element has
     multiplicity k, it should appear exactly k times; you may return the elements in any order."""
    
    spectrum = sorted(spectrum)
    return [i-j for i in spectrum for j in spectrum if i-j > 0]    

#Read input data
f = open('dataset_104_4.txt')
spectrum = map(int, f.read().strip().split())

# Call function
ans = convolution(spectrum)

#Output in right format
print (' '.join(str(i) for i in ans))
