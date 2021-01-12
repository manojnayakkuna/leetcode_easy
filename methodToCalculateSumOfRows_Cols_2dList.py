# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 23:52:06 2020

@author: manoj
"""

def numSpecial(mat):
    
    #mathod 1: Process to calculate sum of rows in a 2d matrix
    sum_rows = []
    for i in range(len(mat)):
        sum_rows.append(sum(mat[i]))
    # Process to calculate sum of cols in a 2d matrix
    sum_cols = []
    for c in range(len(mat)):
        tempSum = 0
        for r in range(len(mat[0])):
            tempSum += mat[r][c] 
        sum_cols.append(tempSum)
    
    #Method 2 using map and zip functions
    row_sums = list(map(sum, mat))
    col_sums = list(map(sum, zip(*mat)))