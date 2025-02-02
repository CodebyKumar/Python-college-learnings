birthdays={'Alice':'Apr 1','Bob':'Dec 12','Corol':'mar 4'}
while True:
    print("Enter a name:(blank to quit)")
    name=input().capitalize()
    if name=='':
        break
    if name in birthdays:
        print(birthdays[name] +' is the birthday of '+ name)
    else:
        print('I dont have birthday information for '+ name)
        print('What is their birthday?')
        bday=input()
        birthdays[name]=bday
        print('Birthday database updated.')
