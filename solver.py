# import numpy as np


# print ("Welcome to the equation solver. Please input ax + by = c for first equation.\n")
# a1 = int(input ("a: "))
# b1 = int(input ("b: "))
# c1 = int(input ("c: "))
# print(f'a: {a1}, b: {b1}, c: {c1}')
# print ("Please input ax + by = c for second equation")
# a2 = int(input ("a: "))
# b2 = int(input ("b: "))
# c2 = int(input ("c: "))
# print(f'a: {a2}, b: {b2}, c: {c2}')
# print("your linear equations are ")
# print(f'Equation 1: {a1}x + {b1}y = {c1}')
# print(f'Equation 2: {a2}x + {b2}y = {c2}')
# m = [[a1,b1,c1],[a2,b2,c2]]
# mA = [[a1,b1],[a2,b2]]
# mB = [c1,c2]
# mX = np.linalg.solve(mA,mB)
# print(f'x = {mX[0]}, y = {mX[1]}')

m = [[6,5,5,5,7,56],[67,8,1,1,9,10],[48,33,20,15,11,68],[23,44,12,5,16,87],[12,33,32,76,66,88]]

# python rowSwap given mxn matrix
def rowSwap(matrix, row1, row2):
    swap = matrix[row1]
    matrix[row1] = matrix[row2]
    matrix[row2] = swap
    return matrix

# print(rowSwap(m,0,1))

# Multiply every element in the row by factor, output: returns new row with multiplied elements
def rowMult(matrix, row, factor ):
    newRow = matrix[row][:]
    for i, val in enumerate(matrix[row]):
        # matrix[row][item] *= factor
        # item*=factor
        # print(item)
        newRow[i] = val*factor
        # print(newRow)
    return newRow

# print(rowMult(m,0,1/3))

# Add 2 rows together to create new row of same # of elements with i...n elements added
def rowAdd(row1, row2):
    newRow = []
    for i in range(len(row1)):
        # print(i)
        newRow.append(row1[i] + row2[i])
    return newRow

# print(rowAdd(m,0,1))

# m[0] = rowMult(m,0,1/m[0][0])
# factor = -(m[1][0])/(m[0][0])
# m[1] = rowAdd(rowMult(m,0,factor),m[1])
# print(m)
# m[1] = rowMult(m,1,1/m[1][1])
# print(m)
# factor = -(m[0][1])/(m[1][1])
# m[0] = rowAdd(rowMult(m,1,factor),m[0])
# print(m)

# print(len(m))
for i in range(0,len(m)):
    for j in range(i,len(m)):
        # print(f'[{j}][{i}]')
        if(i == j):
            # print(f'[{j}][{i}]')
            m[i] = rowMult(m,j,1/m[j][i])
            # print(m)
        else:
            # print(f'[{j}][{i}]')
            factor = -(m[j][i])/(m[i][i])
            m[j] = rowAdd(rowMult(m,i,factor),m[j])
            # print(m)

for k in range(1,len(m)):
    for l in range(0,k):
        # print(f'[{l}][{k}]')
        if(m[l][k] != 0):
            factor = -(m[l][k])
            m[l] = rowAdd(rowMult(m,k,factor),m[l])

for o in range(0, len(m[0])):
    for p in range(0,len(m)):
        if(o == len(m[0])-1):
            m[p][o] = round(m[p][o],2)
        else:
            m[p][o] = round(m[p][o])       


for n in range(0,len(m)):
    # print("Final Array")
    
    print(m[n])





