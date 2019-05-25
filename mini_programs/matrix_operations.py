### Created on 25-05-2019
### @author: annadineyl

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
    for i in range(row1):      # Loop for row entries
        r = []
        for j in range(col1):  # Loop for column entries
            r.append(int(input('Entry in row ' + str(i+1) + ' col ' + str(j+1) + ': ')))
        matrix1.append(r)

    print('\n###  Matrix 2  ###')
    for i in range(row2):      # Loop for row entries
        r = []
        for j in range(col2):  # Loop for column entries
            r.append(int(input('Entry in row ' + str(i+1) + ' col ' + str(j+1) + ': ')))
        matrix2.append(r)
    
    # Add the matrices
    for i in range(row1):
        r = []
        for j in range(col1):
            r.append(matrix1[i][j] + matrix2[i][j])
        result.append(r)

    print('\nThe addition of the matrices:')
    for i in range(row1):
        for j in range(col1):
            print(result[i][j], end='  ')
        print('')

