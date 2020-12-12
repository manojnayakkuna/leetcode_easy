# -*- coding: utf-8 -*-
"""
Created on Fri May 22 20:31:56 2020

@author: manoj
"""
from itertools import product

def isValidSudoku(board):
    for (row,col) in product(range(0,9),repeat=2):
        if board[row][col] != 0:
            for num in range(1,10):
                if (isCorrect(board,row,col,board[row][col]) == False):
                    return False
    return True

def isCorrect(board,row,col,val):
    for r in range(0,9):
        if r != row and board[r][col] == val:
            return False
    for c in range(0,9):
        if c != col and board[row][c] == val:
            return False
    for (r, c) in product(range(0,3), repeat=2):
        rr = row-row%3+r
        cc = col-col%3+c
        if rr != row and cc!=col and board[rr][cc] == val:
            return False
    return True

sudoku = [[0, 8, 7, 6, 5, 4, 3, 2, 1], 
          [2, 0, 0, 0, 0, 0, 0, 0, 0],
          [3, 0, 0, 0, 0, 0, 0, 0, 0], 
          [4, 0, 0, 0, 0, 0, 0, 0, 0], 
          [5, 0, 0, 0, 0, 0, 0, 0, 0], 
          [6, 0, 0, 0, 0, 0, 0, 0, 0], 
          [7, 0, 0, 0, 0, 0, 0, 0, 0], 
          [8, 0, 0, 0, 0, 0, 0, 0, 0], 
          [9, 0, 0, 0, 0, 0, 0, 0, 0]] 

print (isValidSudoku(sudoku))