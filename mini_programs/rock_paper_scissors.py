from random import randint

options = ['Rock', 'Paper', 'Scissors']
computer = options[randint(0, 2)]

while True:
    player = input('\nRock, Paper, Scissors?\nChoose one (blank to quit): ')

    if player == '':
        break

    if player == computer:
        print('Tie!!')
    elif player == 'Rock':
        if computer == 'Paper':
            print('You lose!', computer, 'covers', player)
        else:
            print('You win!', player, 'smashes', computer)
    elif player == 'Paper':
        if computer == 'Rock':
            print('You win!', player, 'covers', computer)
        else:
            print('You lose!', computer, 'cut', player)
    elif player == 'Scissors':
        if computer == 'Rock':
            print('You lose!', computer, 'smashes', player)
        else:
            print('You win!', player, 'cut', computer)
    else:
        print('Invalid play. Please check your spelling.')
