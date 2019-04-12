### Created on 11-04-2019
### @author: nad.

while True:
    n = int(input('\nHow many fibonacci numbers do you want? (0 to quit)\n'))

    if n == 0:
        break
    elif n < 0:
        print('Invalid input. Enter a positive number.')
    else:
        a = 0
        b = 1
        sum = 0

        print('\nFibonacci sequence upto ' + str(n) + ':')
        for count in range(n):
            print(a, end='  ')

            sum = a + b
            a = b 
            b = sum
        print('')