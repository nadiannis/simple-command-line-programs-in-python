### Created on 10-04-2019
### @author: annadineyl

num_of_prime = 0

def n_factor(num):
    num_of_factor = 0
    for i in range(1, num+1):
        if num % i == 0:
            num_of_factor += 1
    
    return num_of_factor

print('######################################')
print('###     PRIME NUMBER GENERATOR     ###')
print('######################################')
print('###                                ###')
print('###     GENERATE PRIME NUMBERS     ###')
print('###   FROM 0 UPTO A GIVEN NUMBER   ###')
print('###                                ###')
print('######################################')
maxNum = int(input('Enter the maximum number: '))

print('\nPrime numbers from 0 upto ' + str(maxNum) + ': ')
for i in range(maxNum+1):
    if n_factor(i) == 2:
        print(i, end='  ')
        num_of_prime += 1

print('\n\nThere are '+ str(num_of_prime) + ' prime numbers.')
    