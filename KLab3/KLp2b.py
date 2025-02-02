def fact(n):
    return 1 if (n==1 or n==0)else n*fact(n-1)

def bC(n,r):
    c=[0 for x in range(r+1)]
    c[0]=1
    for i in range(n+1):
        for j in range(min(i,r),0,-1):
            c[j]=c[j]+c[j-1]
    return c[r]

    
num=int(input('Enter the number: '))
print('Factorial of', num ,'is')
print(fact(num))

num1=int(input('Enter N for binomial coefficient: '))
num2=int(input('Enter R for binomial coefficient: '))
num3=bC(num1,num2)
print('The value of binomial coefficient for given inputs is: ')
print(num3)
