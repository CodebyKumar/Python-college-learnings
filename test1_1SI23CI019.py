name=input('Enter the Student name: ')
usn=input('Enter Student USN: ')
marks=[]
for i in range(3):
    x=int(input('Enter marks in Subject {}: '.format(i+1)))
    marks.append(x)
print('Student Name: {}'.format(name))
print('Student USN: ',usn)
print('Total marks obtained: ',sum(marks))
print('Percentage: ',sum(marks)/len(marks),'%')
avg=sum(marks)/len(marks)
if avg<35:
    print('FAIL')
elif avg<85 and avg>=35:
    print('PASS')
else:
    print('DISTINCTION')
    
