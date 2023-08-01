# This is a guess the number game.
import random
import sys

secretNumber = random.randint(1, 20)
maxcount = 6

print('I am thinking of a number between 1 and 20.')
print('You get', maxcount, 'guesses!')

# This function returns the players guess and reprompts until the player enters
# a valid number.
def getGuess():
    while True:
        print('Take a guess', end=' ->')
        try:
            return int(input())
        except: 
            print('Invalid entry!')

guess = getGuess()
count = 1
while guess != secretNumber:
    if guess < secretNumber:
        print('Your guess is too low')
    else:
        print('Your guess is too high')

    if count > maxcount - 1:
        print('Nope. The number I was thinking of was', secretNumber)
        sys.exit()
    guess = getGuess()
    count += 1

print('Good job! You guessed my number in', str(count), 'guesses!')
