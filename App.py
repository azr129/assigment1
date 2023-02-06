
import random

print('Welcome to Kalanburg')               #Introduction to the game
print('''A long time ago,in a place called Kalanburg,
a place called the Sky Secret Realm appeared,and a steady stream of monsters came out 
of this secret realm, disturbing the peacefulness of the continent of Kalanburg.''')
print('Upon learning that the princess has been kidnapped, the warriors are anxious andworried.')
print('You have been selected to rescue the princess.')
print('Warrior ultimate goal is by killing monsters to bring back the princess.')
print('System prompt: Welcome to "kalanburg: Sky Secret World", Dear Brave, please choose your career!')
print('Careers: Knight, priest')
print('Knight: has a strong strength and defense, but the initial attack is low, the movement speed is slow')
print('Priest:Spell attack, deal extra damage to the undead, but blood and defense is low')

ch=int(input("Enter choice:"))                                 #Character choice making so can start the game with chosen character by user.
if ch==1:                                                      #If user choose number 1, knight will be selected character.
  print('The player has chosen the career: Knight')
  #m=('Career: Knight; Defense: 30; attack: 10~15；luck：70')              #Characters attributes    
elif ch==2:
  print('The player has chosen the career: priest')
  #n=('Career: Priest;  Defense: 15; Spell Attack: 12~17, Spiritual Power: 30'；luck：60)

print('You have left kalanburg and are heading to the place where the princess was kidnapped.')                   # character has ben chosen and the game began. 
print('In order to save pricess, you need to challenge three monsters.')
print('The first monster appears when you have traveled 36,000 miles... Monster Durban')
print('Durban brings you the first challenge is roll dice')
print('The rules are simple, Monster Durban will give you a number, You win by rolling a number larger than Monster Durban with the dice.')
print('Otherwise, you will die.')
print('You have to win two out of three games')
print('Good luck.')

import rps                                           #Import from saved module to play the first challange.

rps.play()

warrior=int(input("What is your score, warrior?"))             #Input scored score to compare the result 
if warrior > 3:                                                #If function to pereper for possibles
  print('Congratulations! 1-0')
elif warrior < 3:
  print('Unfortunately, you have lost the game')
else:
  print('It is a tie, do it again')


  
print('Second round')                                           #second round of first challenge

import rps                                                  #Import from saved module to play the first challange.

rps.play()

warrior=int(input("What is your score, warrior?"))               #Input scored score to compare the result
if warrior > 18:                                                 #If function to pereper for possibles
  print('Congratulations! you have took a win against Monster Durban')
elif warrior < 18:
  print('Unfortunately, 1-1')
else:
  print('It is a tie, do it again')

print('Warrior, this is your last chance to defeat Monster Durban')

import rps                                           #Import from saved module to play the first challange.

rps.play()

warrior=int(input("What is your score, warrior?"))                  #Input scored score to compare the result
if warrior > 5:                                                     #If function to pereper for possibles
  print('Congratulations! you have took a win against Monster Durban')
  print('defense;+3, attack;+4, luck;+2')
elif warrior < 5:
  print('Unfortunately, you have lost against Monster Durban game over.')
  print('defense;-3, attack;-4, luck;-2')
else:
  print('It is a tie, do it again')

print('Once again, congratulations, you have defeated the first monster.')                  #Statements to travel to second challenge
print('The second monster appears after you have traveled 36,000 miles again... Monster Golzan')
print('The game called rock-paper-scissors, warrior has to win two games out of three to defeat Monster Golzan.')
print('Good luck!')

import random

w=(0)                        #Win rate counter
l=(0)                        #Loose rate counter

punches = ['rock','scissors','paper']                     #Options selection
golzann = random.choice(punches)
Warrior=''
Warrior = input('please select your choice: (Rock, Paper, Scissors)')  
while  Warrior not in punches:                            #In case wrong option typed by user
    print('There is an input error, please re-punch')  
    Warrior= input()

print('golzann：%s' % golzann)                             # Dice rolls 
print('warrior：%s' % Warrior)                             #Dice rolls

print('—————result—————')                            #Results
if Warrior == golzann:  
    print('tie！') 
elif (Warrior== 'rock' and golzann == 'scissors') or (Warrior == 'scissors' and golzann == 'paper')or (Warrior == 'paper' and golzann == 'rock'):
    print('you won！') 
    w+=1
else: 
    print('you lost！')
    l+=1

print(l,w)                               #Score after first game 





punches = ['rock','scissors','paper']
golzann = random.choice(punches)
Warrior=''
Warrior = input('please select your choice: (Rock, Paper, Scissors)')  
while  Warrior not in punches:
    print('There is an input error, please re-punch')  
    Warrior= input()

print('golzan：%s' % golzann)
print('warrior：%s' % Warrior)

print('—————result—————') 
if Warrior == golzann:  
    print('tie！') 
elif (Warrior== 'rock' and golzann == 'scissors') or (Warrior == 'scissors' and golzann == 'paper')or (Warrior == 'paper' and golzann == 'rock'):
    print('you won！') 
    w+=1
else: 
    print('you lost！')
    l+=1

print(l,w)




punches = ['rock','scissors','paper']
golzann = random.choice(punches)
Warrior=''
Warrior = input('please select your choice: (Rock, Paper, Scissors)')  
while  Warrior not in punches:
    print('There is an input error, please re-punch')  
    Warrior= input()

print('golzan：%s' % golzann)
print('warrior：%s' % Warrior)

print('—————result—————') 
if Warrior == golzann:  
    print('tie！') 
elif (Warrior== 'rock' and golzann == 'scissors') or (Warrior == 'scissors' and golzann == 'paper')or (Warrior == 'paper' and golzann == 'rock'):
    print('you won！') 
    w+=1
else: 
    print('you lost！')
    l+=1

print(l,w)





print('----final results----')
if w > l:  
    print('you won the second challenge.') 
    print('defense;+1, attack;+3, luck;+3')
elif w < l:
    print('you have lost the challenge, game over.') 
    print('defense;-1, attack;-3, luck;-3')
else: 
    print('it is a tie, extra game')
    punches = ['rock','scissors','paper']
    golzann = random.choice(punches)
    Warrior=''
    Warrior = input('please select your choice: (Rock, Paper, Scissors)')  
    while  Warrior not in punches:
        print('There is an input error, please re-punch')  
        Warrior= input()
    
    print('golzan：%s' % golzann)
    print('warrior：%s' % Warrior)
    
    print('—————result—————') 

    if Warrior == golzann:  
        print('tie！') 
    elif (Warrior== 'rock' and golzann == 'scissors') or (Warrior == 'scissors' and golzann == 'paper')or (Warrior == 'paper' and golzann == 'rock'):
        print('you won！') 
        print('defense;+1, attack;+3, luck;+3')
    else: 
        print('you lost！Game over!') 
        print('defense;-1, attack;-3, luck;-3')

print('Congrats, you have completed your sencond challenge')
print('It is time for you to complete the journey and save the princess')
print('The last challenge is simple,you have to answer the questions to defeat the final monster')
print('Lets start the game')

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
    print('Princess has ben save.')
    print('Game over!')
else:
    print('You have been defeated by monster, game over.')





















