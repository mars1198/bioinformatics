def ComputeDistancesBetweenLeaves(n,T):
    def get_leaves():
        Froms = list(T. keys())
        Tos   = [a for v in list(T.values()) for (a,_) in v]
        X=Froms + Tos
        X.sort()
        Counts={}
        for x in X:
            if x in Counts:
                Counts[x]+=1
            else:
                Counts[x]=1
        return [node for node in Counts.keys() if Counts[node]==2]
    def D(i,j,path=[]):
        if i==j:
            return 0
        d=float('inf')
        for node,weight in T[i]:
            if node==j:
                return weight
            if node in path:
                continue
            test = weight + D(node,j,path+[node])
            if test<d:
                d=test
        return d
    Leaves=get_leaves()
    return [[D(i,j)for j in range(n)] for i in range(n) ]
    
if __name__=='__main__':
    import re
    n=-1
    T={}
    p=re.compile('([0-9]+)->([0-9]+):([.0-9]+)')
    with open('dataset_10328_12.txt') as f:
        for line in f:
            if n==-1:
                n=int(line.strip())
            else:
                m=p.match(line.strip())
                if  not int(m.group(1)) in T:
                    T[int(m.group(1))]=[(int(m.group(2)),int(m.group(3)))]
                else:
                    T[int(m.group(1))].append((int(m.group(2)),int(m.group(3))))
        for ds in ComputeDistancesBetweenLeaves(n,T):
            print(' '.join(str(d) for d in ds))
