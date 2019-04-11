### Created on 11-04-2019
### @author: nad.

a = 0
b = 1
sum = 0

n = int(input('How many fibonacci numbers do you want?\n'))

print('\nFibonacci sequence upto', n, ':')
for count in range(n):
    print(a, end='  ')

    sum = a + b
    a = b 
    b = sum