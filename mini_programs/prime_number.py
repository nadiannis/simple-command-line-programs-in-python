### Created on 10-04-2019
### @author: annadineyl

num_of_prime = 0

def n_factor(num):
    num_of_factor = 0
    for i in range(1, num+1):
        if num % i == 0:
            num_of_factor += 1
    
    return num_of_factor

def is_prime(num, n_prime):
    if n_factor(num) == 2:
        print(num, end='  ')
        n_prime += 1
    
    return n_prime

print('######################################')
print('###     PRIME NUMBER GENERATOR     ###')
print('######################################')
print('###                                ###')
print('###     GENERATE PRIME NUMBERS     ###')
print('###   FROM 0 UPTO A GIVEN NUMBER   ###')
print('###                                ###')
print('######################################')
max_num = int(input('Enter the maximum number: '))

print('\nPrime numbers from 0 upto ' + str(max_num) + ': ')
for i in range(max_num+1):
    num_of_prime = is_prime(i, num_of_prime)

print('\n\nThere are ' + str(num_of_prime) + ' prime numbers.')