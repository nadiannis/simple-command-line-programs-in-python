### Created on 07-01-2019
### @author: nad

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
def finalResult(n, m):
    if userChoice == '+':
        result = add(n, m)
        return result
    elif userChoice == '-':
        result = subtract(n, m)
        return result
    elif userChoice == '*':
        result = multiply(n, m)
        return result
    elif userChoice == '/':
        result = divide(n, m)
        return result

while True:
    num1 = int(input('Enter a number: '))

    result = 0
    while True:
        print('\t', 'Select operation: + Add | - Subtract | * Multiply | / Divide')
        print('\t', 'Please enter you choice (+, -, *, /): ', end=' ')
        userChoice = input()

        num2 = int(input('Enter another number: '))
        print('\n')
        print('The result is', finalResult(num1, num2))
        num1 = finalResult(num1, num2)
