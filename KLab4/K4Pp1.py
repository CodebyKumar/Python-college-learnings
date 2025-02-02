import random
sN=random.randint(1,20)
print('Guess a number between 1 and 20')
for gT in range(1,7):
    print('Guess number: ')
    gN=int(input())
    if gN<sN:
        print('Guess is low')
    elif gN>sN:
        print('Guess is high')
    else:
        break
if gN==sN:
    print('Good job! you guessed in '+str(gT)+' guesses')
else:
    print('You loose! '+str(sN)+' is the number')
