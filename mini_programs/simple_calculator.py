### Created on 07-01-2019

# This function returns the result of the calculation of two numbers
def final_result(n, m):
    if user_choice == '+':
        result = n + m
    elif user_choice == '-':
        result = n - m
    elif user_choice == '*':
        result = n * m
    else:
        result = n / m
    return result


num1 = int(input('Enter a number: '))
while True:
    print('[operation]'.center(45))
    print('+ Add | - Subtract | * Multiply | / Divide')
    print('\nPlease enter you choice (+, -, *, /)\n[blank to quit]: ')
    user_choice = input()
    
    if user_choice in ['+', '-', '*', '/']:
        num2 = int(input('Enter another number: '))
        res = final_result(num1, num2)
        print(f'\nThe result is {res}\n')
        num1 = res
    elif user_choice == '':
        break
    else:
        print('Invalid operator.\n')
