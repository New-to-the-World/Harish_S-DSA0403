import numpy as np
a=[]
for i in range(3):
    b=[]
    for j in range(3):
        print("sales of product ",i+1,"in month ",j+1,":")
        n=int(input())
        b.append(n)
    a.append(b)
a=np.array(a)
av=[]
for i in range(len(a[0])):
               s=0
               for j in a:
                   s+=j[i]
               av.append(s/3)
for i in range(3):
    print("avg of products sold in month ",i+1,"is ",av[i])

