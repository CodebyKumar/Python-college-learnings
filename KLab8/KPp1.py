x=input('Object: ')
y=int(input('Length: '))
z=int(input('Bredth: '))
for i in range(y):
    if i==0 or i==y-1:
        print(x*z)
        
    else:
        print(x,''*(z-1),x)