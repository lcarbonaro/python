from random import randint

rand = randint(1,20)

print('I have picked a random integer between 1 and 20.')

guess = input('Enter your guess: ')

if guess<rand:
    print('That is too low.')

if guess>rand:
    print('That is too high.')

if guess==rand:
    print('That is correct.')
    
print('The random integer was: ' + str(rand))
