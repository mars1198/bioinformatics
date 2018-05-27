import itertools
from collections import Counter

def frequent_words_problem(string, k):

    words = []
    results = []      
	
    for i in range(len(string)):  
        word = "".join(string[i: i+k])
		
        if len(word) == k:
            words.append(word)  
			
    return Counter(words).most_common()



def clump_finding_problem(string, k, L, t):  
  
    words = []    
	
    for i in range(len(string)):
        string_1 = string[i: i+L]
		
        if len(string_1) == L:            
            words.append(frequent_words_problem(string_1, k))
            
    dummy = list(itertools.chain(*words))
	
    return [y for y in set([x[0] for x in dummy if x[1] >= t])]
            
k = 9
L = 542
t = 16


a = str(clump_finding_problem('', k, L, t))
print (a)
