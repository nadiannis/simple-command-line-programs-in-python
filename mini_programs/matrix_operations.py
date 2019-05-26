### Created on 25-05-2019
### @author: annadineyl

def inputMatrix(matrix, row, col):
    for i in range(row):      # Loop for row entries
        r = []
        for j in range(col):  # Loop for column entries
            r.append(int(input('Entry in row ' + str(i+1) + ' col ' + str(j+1) + ': ')))
        matrix.append(r)

def addMatrix(matrix1, matrix2, row, col, result):
    for i in range(row):
        r = []
        for j in range(col):
            r.append(matrix1[i][j] + matrix2[i][j])
        result.append(r)

def displayMatrix(matrix, row, col):
    for i in range(row):
        for j in range(col):
            print(matrix[i][j], end='  ')
        print('')


matrix1 = []
matrix2 = []
result = []

row1 = int(input('Enter number of rows of matrix 1: '))
col1 = int(input('Enter number of columns of matrix 1: '))

row2 = int(input('\nEnter number of rows of matrix 2: '))
col2 = int(input('Enter number of columns of matrix 2: '))

if (row1 != row2) or (col1 != col2):
    print('\n\tMatrices can\'t be added each other.')
    print('\tBoth matrices must be of the same size.')
else:
    print('\n###  Matrix 1  ###')
    inputMatrix(matrix1, row1, col1)

    print('\n###  Matrix 2  ###')
    inputMatrix(matrix2, row2, col2)
    
    # Add the matrices
    addMatrix(matrix1, matrix2, row1, col1, result)

    print('\nThe addition of the matrices:')
    displayMatrix(result, row1, col1)
