### Created on 09-01-2019

import random

print('###     Choose Level     ###')
print('### Easy | Medium | Hard ###')
level = input('Enter level: ').lower()

if level == 'easy':
    chance = 10
elif level == 'medium':
    chance = 6
elif level == 'hard':
    chance = 4

# Generates a random number between 1 and 100 (1 <= num <= 100)
num = random.randint(1, 100)
print('\n\tI\'m thinking of a number between 1 and 100')
print('\tYou only have ' + str(chance) + ' chances to guess.')

guesses_taken = 0
while guesses_taken < chance:
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
