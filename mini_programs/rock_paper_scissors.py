### Created on 15-1-2019
### @author: nad.

from random import randint

# List of play options
options = ['Rock', 'Paper', 'Scissors']

while True:
    computer = options[randint(0, 2)]  # Pick rock, paper, or scissors randomly for the computer
    player = input('\nRock, Paper, Scissors?\nChoose one (blank to quit): ')

    # Stop the program
    if player == '':
        break

    if player == computer:
        print('\tComputer\'s choice:', computer)
        print('\tYour choice:', player)
        print('Tie!!')
    elif player == 'Rock':
        if computer == 'Paper':
            print('\tComputer\'s choice:', computer)
            print('\tYour choice:', player)
            print('You lose!', computer, 'covers', player)
        else:
            print('\tComputer\'s choice:', computer)
            print('\tYour choice:', player)
            print('You win!', player, 'smashes', computer)
    elif player == 'Paper':
        if computer == 'Rock':
            print('\tComputer\'s choice:', computer)
            print('\tYour choice:', player)
            print('You win!', player, 'covers', computer)
        else:
            print('\tComputer\'s choice:', computer)
            print('\tYour choice:', player)
            print('You lose!', computer, 'cut', player)
    elif player == 'Scissors':
        if computer == 'Rock':
            print('\tComputer\'s choice:', computer)
            print('\tYour choice:', player)
            print('You lose!', computer, 'smashes', player)
        else:
            print('\tComputer\'s choice:', computer)
            print('\tYour choice:', player)
            print('You win!', player, 'cut', computer)
    else:
        print('Invalid play. Please check your spelling.')
