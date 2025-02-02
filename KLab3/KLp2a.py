nTerms=int(input('Read the Fibonacci sequence of lenth: '))
n1,n2=0,1
count=0

if nTerms<=0:
    print('Cannot generate the Fibonacci sequence for the given length...')
elif nTerms==1:
    print('Fibonacci sequence upto ',nTerms)
    print(n1)
else:
    print('Fibonacci sequence: ')
    while count<nTerms:
        print(n1,end=' ')
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
