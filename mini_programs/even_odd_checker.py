### Created on 15-04-2019
### @author: annadineyl

while True:
    num = input('Enter a number (blank to quit): ')

    if num == '':
        break

    num = int(num)
    if num % 2 == 0:
        print(str(num) + ' is even\n')
    else:
        print(str(num) + ' is odd\n')