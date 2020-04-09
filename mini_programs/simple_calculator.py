### Created on 07-01-2019

# This function adds two numbers
def add(n, m):
    return n + m

# This function subtracts two numbers
def subtract(n, m):
    return n - m

# This function multiplies two numbers
def multiply(n, m):
    return n * m

# This function divides two numbers
def divide(n, m):
    return n / m


# This function returns the result of the calculation of two numbers
def final_result(n, m):
    if user_choice == '+':
        result = add(n, m)
    elif user_choice == '-':
        result = subtract(n, m)
    elif user_choice == '*':
        result = multiply(n, m)
    else:
        result = divide(n, m)
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
