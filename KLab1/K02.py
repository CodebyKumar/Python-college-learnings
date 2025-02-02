# Program to print pattern
n=int(input('Enter n: '))

for j in range(1,n+1):
    print('#'*j)
for i in range(n,0,-1):
    print('#'*i)
