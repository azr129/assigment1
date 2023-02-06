import random 
answer=()                          #Answer statement
score=(0)                          #Score to calculate after all
totalquestions=3                   #Questions in total
answerS=()

answer=int(input('Question 1: 2**2**3 '))                #Question #1

if answer==256:                       #Answer of question #1
        score+=1                      #score if user answer is correct
        print('correct')
else:
        print('Wrong Answer :(')
 
 
answer=input('Question 2: what is the first 5 decimal digits of pi? ')
if answer=='14159':
        score += 1
        print('correct')
else:
        print('Wrong Answer :(')
 
answerS=input('Question 3: what can fly but has no wings')
if answerS.lower()=='time':
        score += 1
        print('correct')
else:
        print('Wrong Answer :(')
 

mark=(score/totalquestions)*100
print('Marks obtained:',mark)
if score > 60:
    print('Monster defeated!')
    print('defense;+3, attack;+4, luck;+2')
    print('You made a good job warrior, Princess has been saved.')
    print('Game over!')
else:
    print('You have been defeated by monster, game over.')

import q
q.play()                                                         #Import from saved module to play the last challange.

