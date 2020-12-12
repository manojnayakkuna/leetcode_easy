# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 00:09:01 2020

@author: manoj
"""
"""
Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1, return the number of special positions in mat.
A position (i,j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
Example 1:
Input: mat = [[1,0,0],
              [0,0,1],
              [1,0,0]]
Output: 1
Explanation: (1,2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
Example 2:
Input: mat = [[1,0,0],
              [0,1,0],
              [0,0,1]]
Output: 3
Explanation: (0,0), (1,1) and (2,2) are special positions. 
"""
def numSpecial(mat):
    
    """
    sum_rows = []
    for i in range(len(mat)):
        sum_rows.append(sum(mat[i]))
    sum_cols = []
    for c in range(len(mat)):
        tempSum = 0
        for r in range(len(mat[0])):
            tempSum += mat[r][c] 
        sum_cols.append(tempSum)
    """
    row_sums = list(map(sum, mat))
    col_sums = list(map(sum, zip(*mat)))
    print('row_sums:', row_sums, '\ncol_sums:', col_sums)
    
    count = 0
    for r, row in enumerate(mat):
        print ('row   :', row, '\nmat[r]:', mat[r])
        for c, n in enumerate(mat[r]):
            print ('r:', r, 'c:', c, 'n:', n,'row_sums[r]:',row_sums[r],'col_sums[c]:',col_sums[c])
            if n and row_sums[r] == col_sums[c] == 1:
                count += 1
                print (count)
                
    return count

mat = [[1,0,0],
       [0,0,1],
       [1,0,0]]
print(numSpecial(mat))