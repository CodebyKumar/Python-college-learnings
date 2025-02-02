personName=input('Enter  person name: ')
personYOB=int(input('Enter year of birth: '))
currentYear=int(input('Enter current year: '))

age=currentYear-personYOB

if age>=60:
    print(personName,'is a senior citizen...')
else:
    print(personName,'is not senior citizen...')
