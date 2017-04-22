from random import randint

rand = randint(1,20)

print('I have picked a random integer between 1 and 20.')

def getGuess():
    guess = input('Enter your guess: ')
    return guess

guess = getGuess()

while guess != rand:
    if guess<rand:
        print('That is too low.')
    
    if guess>rand:
        print('That is too high.')
    
    guess = getGuess()
    
print('That is correct.')
    
print('The random integer was: ' + str(rand))
