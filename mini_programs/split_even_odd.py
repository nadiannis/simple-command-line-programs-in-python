### Created on 16-04-2019

nums = []
even = []
odd = []

while True:
    num = input('Enter a number (blank to stop entering number): ')

    if num == '':
        break
    else:
        num = int(num)
        nums.append(num)

for num in nums:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)


print('\nYou entered:', *nums, end=' ')

print('\n\nEven:', *even, end=' ')
print('\n\nodd:', *odd, end=' ')
