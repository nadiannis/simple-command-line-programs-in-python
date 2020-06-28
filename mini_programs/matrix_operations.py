### Created on 25-05-2019

def input_matrix(matrix, row, col):
    for i in range(row):      # Loop for row entries
        r = []
        for j in range(col):  # Loop for column entries
            r.append(int(input('Entry in row ' + str(i+1) + ' col ' + str(j+1) + ': ')))
        matrix.append(r)

def add_matrix(matrix1, matrix2, result):
    for i in range(len(matrix1)):
        r = []
        for j in range(len(matrix1[0])):
            r.append(matrix1[i][j] + matrix2[i][j])
        result.append(r)

def sub_matrix(matrix1, matrix2, result):
    for i in range(len(matrix1)):
        r = []
        for j in range(len(matrix1[0])):
            r.append(matrix1[i][j] - matrix2[i][j])
        result.append(r)

def display_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end='  ')
        print('')


def main():
    matrix1 = []
    matrix2 = []
    result = []
    
    print('====================================')
    print('    Operation: + Add | - Subtract   ')
    print('====================================')
    
    row1 = int(input('\nEnter number of rows of matrix 1: '))
    col1 = int(input('Enter number of columns of matrix 1: '))
    
    row2 = int(input('\nEnter number of rows of matrix 2: '))
    col2 = int(input('Enter number of columns of matrix 2: '))
    
    if (row1 != row2) or (col1 != col2):
        print('\nBoth matrices must be of the same size.')
    else:
        print('\n###  Matrix 1  ###')
        input_matrix(matrix1, row1, col1)
        
        print('\n###  Matrix 2  ###')
        input_matrix(matrix2, row2, col2)
        
        op = input('\nSelect operation (+, -): ')
        if op == '+':
            add_matrix(matrix1, matrix2, result)
            print('\nThe addition of the matrices:')
            display_matrix(result)
        elif op == '-':
            sub_matrix(matrix1, matrix2, result)
            print('\nThe subtraction of the matrices:')
            display_matrix(result)
        else:
            print('Invalid choice\n')


if __name__ == '__main__':
    main()
