import numpy as np
import time
import random as r

filename = "sudoku-task1.txt"

with open(filename, "r") as f:
    """Opens the text file and converts it to a numpy integer matrix. Prints puzzle."""
    values = list(f.read().replace(" ", "").replace("\n", ""))
    values = map(int, values)                       # maps all values to integers
    matrix = np.reshape(values, (9, 9))             # turns it into matrix
    print matrix

numbers = range(1, 10)
size = range(0, 9)
squs = [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]

def fill(matrix):
    """Replaces all zeros with all possible values (1 - 9)"""
    for x in size:
        for y in size:
            if matrix[x][y] == 0:
                matrix[x][y] = 123456789            # all possible initial values
    return matrix

def checkrow(matrix, i, j):
    """Removes all numbers that are already occupied in the row"""
    for y in size:
        if len(str(matrix[i][y])) == 1:             # ignores cells with more than one number
            try:
                a = list(str(matrix[i][j]))         # removes occupied values in row
                a.remove(str(matrix[i][y]))
                matrix[i][j] = int("".join(a))
            except ValueError:
                pass
    return matrix

def checkcol(matrix, i, j):
    """Removes all numbers that are already occupied in the column"""
    for x in size:
        if len(str(matrix[x][j])) == 1:
            try:
                a = list(str(matrix[i][j]))         # removes occupied values in column
                a.remove(str(matrix[x][j]))
                matrix[i][j] = int("".join(a))
            except ValueError:
                pass
    return matrix

def checksqu(matrix, i, j):
    """Removes all numbers that are already occupied in the square"""
    csx, csy = 3 * (i / 3), 3 * (j / 3)
    for x in range(csx, csx + 3):
        for y in range(csy, csy + 3):
            if len(str(matrix[x][y])) == 1:
                try:
                    a = list(str(matrix[i][j]))     # removes occupied values in square
                    a.remove(str(matrix[x][y]))
                    matrix[i][j] = int("".join(a))
                except ValueError:                  # catches exception in case of ValueError
                    pass
    return matrix

def length(matrix, l):
    """Returns False if all cells contain only one number (sudoku is solved)"""
    for x in size:
        for y in size:
            if len(str(matrix[x][y])) > l:
                return True
    return False

def pick(matrix, l):
    """If it encounters the case where there is nothing left to remove,
    it will pick the first of two possible values and continue."""
    for x in size:
        for y in size:
            if len(str(matrix[x][y])) > l:
                #matrix[x][y] = str(matrix[x][y])[r.randint(0, l)]
                matrix[x][y] = str(matrix[x][y])[0] # picks first branch
                break
    return matrix

def square(matrix, i):
    c = []
    for x in range(squs[i][0], squs[i][0] + 3):
        for y in range(squs[i][1], squs[i][1] + 3):
            c.append(matrix[x][y])
    return c

def count(matrix):
    counter = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in size:
        for y in size:
            if matrix[x][y] in numbers:
                a = matrix[x][y]-1
                counter[a] = counter[a]+1
    print counter
    if counter == [9, 9, 9, 9, 9, 9, 9, 9, 9]:
        return False

def control(matrix):
    for x in size:
        for y in size:
            for i in size:
                if matrix[:x].tolist().count(matrix[x][y]) != 1:
                    return True
                elif matrix[y:].tolist().count(matrix[x][y]) != 1:
                    return True
                elif square(matrix, i).count(matrix[x][y]) != 1:
                    return True
                else:
                    return False

def solve(matrix):
    """Fills matrix with possible values and iteratively removes all occupied numbers.
    Finishes if all cells contain only one number. Prints solution."""
    while True:
        fill(matrix)
        matrix2 = matrix
        matrix_backup = matrix

        while length(matrix, 1):
            print matrix
            print
            for x in size:
                for y in size:
                    checkrow(matrix, x, y)
                    checkcol(matrix, x, y)
                    checksqu(matrix, x, y)
            if np.array_equal(matrix2, matrix):
                pick(matrix, 1)
            matrix2 = matrix
        if not (control(matrix) and count(matrix)):
            break
    return matrix

start = time.time()                                 # measures execution time
solve(matrix)
end = time.time()
print (end - start)