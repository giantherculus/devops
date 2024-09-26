import math
n=[]
x=set([])
for i in range(1,11):
    i=int(input("enter"))
    n.append(i)
    x.add(i)
print(x)
max=0
for j in range (0,len(n)):
    if n[j] >max:
        max=n[j]
print(max)




 