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
    elif user_choice == '/':
        result = divide(n, m)
    else:
        result = 'Invalid operator.\n'
        
    return result

while True:
    num1 = int(input('Enter a number: '))
    
    while True:
        print('\t', 'Select operation: + Add | - Subtract | * Multiply | / Divide')
        print('\t', 'Please enter you choice (+, -, *, /): ', end=' ')
        user_choice = input()

        num2 = int(input('Enter another number: '))
        
        if user_choice == '+' or user_choice == '-' or user_choice == '*' or user_choice == '/':
            print('\n')
            print('The result is', final_result(num1, num2))
            num1 = final_result(num1, num2)
        else:
            print(final_result(num1, num2))
