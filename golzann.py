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







import golzann                                                      #Import from saved module to play the second challange.
golzann.play()
