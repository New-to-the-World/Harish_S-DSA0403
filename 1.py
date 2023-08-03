import numpy as np
l=["maths","chemistry","physice","python"]
a=[]
for i in range(4):
    b=[]
    for j in range(4):
        print("Enter marks of student ",i+1," in ",l[j],":")
        n=int(input())
        b.append(n)
    a.append(b)
a=np.array(a)
print("Marks",a)
av=[]
for i in range(len(a[0])):
               s=0
               for j in a:
                   s+=j[i]
               av.append(s/4)
for i in range(4):
    print("Avg of ",l[i]," is ",av[i])
print(l[av.index(max(av))],"has highest average :",max(av))
