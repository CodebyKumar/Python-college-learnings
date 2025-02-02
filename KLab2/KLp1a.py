studentName=input('Enter student name: ')
studentUSN=input('Enter USN: ')
numberofsubjects=int(input('Number of subjects: '))

subjectList=['Physics','Chemistry','Maths']
marksList=[]

for i in range(numberofsubjects):
    print('Enter the marks obtained in ',subjectList[i],': ')
    subjectmarks=int(input())
    marksList.append(subjectmarks)

print('Name: ',studentName)
print('USN: ',studentUSN)
print('Number of subjects: ',numberofsubjects)
total=sum(marksList)
avg=total/len(marksList)
print('Total Marks obtained: ',total)
print('Percentage obtained: ',avg,'%')

if avg>=35:
    print('PASS')
else:
    print('FAIL')
