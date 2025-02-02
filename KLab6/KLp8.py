def DivExp(a,b):
    if (a>0 and b>0):
        c=a/b
        return int(c)
num1=int(input('Enter number 1: '))
num2=int(input('Enter number 2: '))
if num2 ==0:
    print('Denominator should not be zero')
result=DivExp(num1,num2)
print(result)
