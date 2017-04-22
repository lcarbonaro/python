from random import randint

rand = randint(1,20)

print('Thinking of a number between 1 and 20...')

def getGuess():
    _cont = True
    while _cont:
        try:
            g = int ( input('Enter your guess: ') )
            _cont = False
        except ValueError:
            print('You must enter an integer.')
            continue
    return g

guess = getGuess()

while guess!=rand:
    if guess>rand:
        print('That is too high.')
    if guess<rand:
        print('That is too low.')
    guess = getGuess()
    
print('That is correct!')

print('The number is: ' + str(rand) )

