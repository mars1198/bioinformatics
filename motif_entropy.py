import math

a=[0.2,0.2,0.9,0.1,0.1,0.1,0.3]
c=[0.1,0.6,0.4,0.1,0.2,0.4,0.6]
g=[1,1,0.9,0.9,0.1]
t=[0.7,0.2,0.1,0.1,0.5,0.8,0.7,0.3,0.4]
data_list=[a,c,g,t]

H=0.0
for j in data_list:
    for i in j:
        H=H+i*(math.log(i,2))
print (-H) 
