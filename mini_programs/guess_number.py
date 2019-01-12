### Created on 09-01-2019
### @author: nad.

import random

# Generates a random number between 1 and 100 (1 <= num <= 100)
num = random.randint(1, 100)
print('\tI\'m thinking of a number between 1 and 100')
print('\tYou only have 8 chances to guess.')

guesses_taken = 0
while guesses_taken < 8:
    guess = int(input('Take a guess: '))

    guesses_taken += 1

    if guess > num:
        print('Too high!\n')
    elif guess < num:
        print('Your guess is too low.\n')
    elif guess == num:
        break 

if guess == num:
    print('Congratulations! You guessed my number in', guesses_taken, 'guesses!')
else:
    print('Sorry, you\'re wrong. The number is', num)
