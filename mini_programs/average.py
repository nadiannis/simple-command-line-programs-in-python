### Created on 12-05-2019

nums = input('Enter some numbers (separate by space): ').split()

# Calculate the average
sum_of_nums = 0
for num in nums:
    sum_of_nums += float(num) 

avg = sum_of_nums / len(nums)

# Display the numbers & the average
print('\nYou entered:', *nums, end=' ')
print('\nThe average:', avg)
