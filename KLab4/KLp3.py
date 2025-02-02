import numpy as np
lst=[]
n=int(input('Enter number of elements: '))
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
print(lst)
print(np.average(lst))
print(np.var(lst))
print(np.std(lst))
