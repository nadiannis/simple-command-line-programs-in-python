### Created on 10-04-2019
import math

print('######################################')
print('###     PRIME NUMBER GENERATOR     ###')
print('######################################')
print('###                                ###')
print('###     GENERATE PRIME NUMBERS     ###')
print('###   FROM 0 UPTO A GIVEN NUMBER   ###')
print('###                                ###')
print('######################################')

max_num = int(input('Enter the maximum number: '))

primes = []
for i in range(2, max_num+1):
    primes.append(i)

for x in range(2, int(math.sqrt(max_num)+1)):
    if x in primes:  # Remove multiples of x if x in list
        for y in range(x*2, max_num+1, x):
            if y in primes:
                primes.remove(y)

print('\nPrime numbers from 0 upto ' + str(max_num) + ': ')
print (*primes, end= '  ')
print('\n\nThere are ' + str(len(primes)) + ' prime numbers.')
