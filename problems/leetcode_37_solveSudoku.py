# -*- coding: utf-8 -*-
"""
Created on Fri May  8 11:46:48 2020

@author: manoj
"""
from itertools import product

def solveSudoku(sudokuPuzzle):
    
    if len(sudokuPuzzle) == 0:
        return -1
    
    if len(sudokuPuzzle) != len(sudokuPuzzle[0]):
        return -1
    
    for (row,col) in product(range(0,9),repeat=2):
        #print ('row:',row,'col:',col)
        if sudokuPuzzle[row][col] == 0: #manipulate or fill only all unassigned positions
            for num in range(1,10):
                allowed = True
                for i in range(0,9):
                    if sudokuPuzzle[i][col] == num or sudokuPuzzle[row][i] == num:
                        allowed = False
                        break
                for (i, j) in product(range(0,3), repeat=2):
         #           print ('i:',i,'j:',j)
                    if sudokuPuzzle[row-row%3+i][col-col%3+j] == num:
                        allowed = False
                        break
                if allowed:
                    sudokuPuzzle[row][col] = num
                    trail = solveSudoku(sudokuPuzzle)
                    if trail == sudokuPuzzle:
                        return trail
                    else:
                        sudokuPuzzle[row][col] = 0
            return False
    return sudokuPuzzle

def printSudoku(puzzle):
    for row in range(0,9):
        for col in range(0,9):
            print (puzzle[row][col], '', end='')
        print ()

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

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
solveSudoku(puzzle)

printSudoku(puzzle)