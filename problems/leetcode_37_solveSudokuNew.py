# -*- coding: utf-8 -*-
"""
Created on Mon May 11 19:09:03 2020

@author: manoj
"""
def locatePos(puzzle,List):
    for row in range(len(puzzle)):
        for col in range(len(puzzle[0])):
            if puzzle[row][col] == 0:
                List[0] = row
                List[1] = col
                return False
    return True

def used_in_rowcolumn(puzzle,row,col,num):
    for i in range(len(puzzle)):
        if puzzle[row][i] == num or puzzle[i][col] == num:
            return False
    return True

def used_in_box(puzzle,row,col,num):
    for i in range(3):
        for j in range(3):
            if puzzle[i+row][j+col] == num:
                return False
    return True

def check_location_is_safe(puzzle,row,col,num):
    #print ('row:',row,';col:',col,';row-row%3:',row-row%3,';col-col%3:',col-col%3)
    #return not used_in_rowcolumn(puzzle,row,col,num) and not used_in_box(puzzle,row-row%3,col-col%3,num)
    return used_in_rowcolumn(puzzle,row,col,num) and used_in_box(puzzle,row-row%3,col-col%3,num)

def solveSudoku(puzzle):
    l = [0,0]
    if (locatePos(puzzle,l)):
        return True
    row = l[0]
    col = l[1]
    for num in range(1,10):
        if (check_location_is_safe(puzzle,row,col,num)):
            puzzle[row][col] = num
            if solveSudoku(puzzle):
                return True
            puzzle[row][col] = 0
    return False

def printSudoku(puzzle):
    for row in range(len(puzzle)):
        for col in range(len(puzzle[0])):
            print (puzzle[row][col], '', end='')
        print ()

puzzle=[[3,0,6,5,0,8,4,0,0], 
        [5,2,0,0,0,0,0,0,0], 
        [0,8,7,0,0,0,0,3,1], 
        [0,0,3,0,1,0,0,8,0], 
        [9,0,0,8,6,3,0,0,5], 
        [0,5,0,0,9,0,6,0,0], 
        [1,3,0,0,0,0,2,5,0], 
        [0,0,0,0,0,0,0,7,4], 
        [0,0,5,2,0,6,3,0,0]]

puzzle=[[0,8,7,6,5,4,3,2,1],
        [2,0,0,0,0,0,0,0,0],
        [3,0,0,0,0,0,0,0,0],
        [4,0,0,0,0,0,0,0,0],
        [5,0,0,0,0,0,0,0,0],
        [6,0,0,0,0,0,0,0,0],
        [7,0,0,0,0,0,0,0,0],
        [8,0,0,0,0,0,0,0,0],
        [9,0,0,0,0,0,0,0,0]]

printSudoku(puzzle)
print('********************************')
if (solveSudoku(puzzle)):
    printSudoku(puzzle)
else:
    print ("No Solution Exists")