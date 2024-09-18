import random
from random import randint

ran_num=random.randint(1,20)
print('You will be given 5 attempts in total')
guess=''

condition=True
attempts=0
end=5
while attempts<end:
    try:
        guess = int(input('Guess random number between 1 and 20: '))

        if guess < 1 or guess > 20:
            print('Invalid number. Please enter a number between 1 and 20.')
            continue
        if ran_num==guess:

            print('Correct!!!You won the game! Congratulations🎉🎉')
            attempts = attempts + 1
            print(f'Number of attempts is {attempts}')
            #condition=False

        elif ran_num<guess:
            print('Too high')
            attempts = attempts + 1




        elif ran_num>guess:
            print('Too small')
            attempts = attempts + 1
    except ValueError:
        print('Please,enter valid number')
if attempts==5 and ran_num!=guess:
       print('Exceed number of attempts')
       print('GAME OVER')
       print(f'The correct number was {ran_num}')

