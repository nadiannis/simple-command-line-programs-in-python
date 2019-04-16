### Created on 16-04-2019
### @author: annadineyl

nums = []
even = ''
odd = ''

while True:
    num = input('Enter a number (blank to stop entering number): ')

    if num == '':
        break
    else:
        num = int(num)
        nums.append(num)

for num in nums:
    if num % 2 == 0:
        even += str(num) + ' '
    else:
        odd += str(num) + ' '

print('\nYou entered:')
for num in nums:
    print(num, end=' ')
print('\n')

print('Even:')
print(even)
print('')
print('Odd:')
print(odd)