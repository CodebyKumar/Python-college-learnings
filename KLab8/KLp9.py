class Complex:
    def __init__(self,tempReal,tempImaginary):
        self.real=tempReal
        self.imaginary=tempImaginary

    def addComp(self,c1,c2):
        temp=Complex(0,0)
        temp.real=c1.real+c2.real
        temp.imaginary=c1.imaginary+c2.imaginary
        return temp
# First complex number
x1=int(input('Enter the real part of the complex number 1: '))
y1=int(input('Enter the imaginary part of the complex number 1: '))
c1=Complex(x1,y1)
print('Complex number 1 : {}+i{}'.format(c1.real,c1.imaginary))

# Second complex number
x2=int(input('Enter the real part of the complex number 2: '))
y2=int(input('Enter the imaginary part of the complex number 2: '))
c2=Complex(x2,y2)
print('Complex number 2 : {}+i{}'.format(c2.real,c2.imaginary))

c3=Complex(0,0)
c3=c3.addComp(c1,c2)
print('Sum of complex number: {}+i{}'.format(c3.real,c3.imaginary))
