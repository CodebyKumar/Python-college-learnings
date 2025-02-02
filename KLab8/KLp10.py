class students:
    count=0
    def __init__(self,name):
        self.name=name
        self.marks=[]
        students.count=students.count+1
    def enterMarks(self):
        for i in range(3):
            m=int(input('Enter marks in subject %d: '%(i+1)))
            self.marks.append(m)
    def disp(self):
        sum=sum(self.marks)
        print(f'\nScore Card Details\nSudent Name: {self.name}\nTotal Marks: {sum}\nPercentage: {sum/3}%')


for i in range(2):
    name=input('\nEnter the name of Student: ')
    s1=students(name)
    s1.enterMarks()
    s1.disp()

