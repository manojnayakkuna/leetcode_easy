# -*- coding: utf-8 -*-
"""
Created on Sun May 31 01:54:58 2020

@author: manoj
"""
def closedIsland(grid):
    
    rows = len(grid)
    cols = len(grid[0])
    numIslands = 0
    
    def dfs(cr, cc):
        #check for bounds on the indices
        if cr<0 or cr>=rows or cc<0 or cc>=cols:                
            return False
        #if it is water then no need to explore further
        if (grid[cr][cc] == 1):   
            return True
        #if 0, change it to 1, to avoid visiting again
        grid[cr][cc] = 1
        if not dfs(cr+1, cc):
            #if the dfs gives False, reassign it to 0 to avoid considering it as wrong for other traversals
            grid[cr][cc] = 0
            return False
        if not dfs(cr-1, cc):
            grid[cr][cc] = 0
            return False
        if not dfs(cr, cc+1):  
            grid[cr][cc] = 0            
            return False    
        if not dfs(cr, cc-1):
            grid[cr][cc] = 0
            return False
        #if the exploration is successful, then change it to 1 and return True        
        grid[cr][cc] = 1
        return True

    def dfsNew(i,j):
        dir = [[1,0],[-1,0],[0,1],[0,-1]]        
        if rows <= i < 0 or cols <= j < 0:
            return False
        print ('i:',i,'j:',j)
        if grid[i][j] == 1:
            return True
        grid[i][j] = 1
        for d in dir:
            ni, nj = i + d[0], j + d[1]
            if (not dfsNew(ni,nj)):
                grid[i][j] = 0
                return False
        grid[i][j] = 1
        return True
    #since it is not possible to have an island on the corners iterate from 1 to rows-1 and 1 to cols-1
    for i in range(1,rows-1):
        for j in range(1,cols-1):
            if (grid[i][j] == 0):
                #if the dfs exploration is successful then increase the island count by 1
                if dfs(i,j):
                    numIslands+=1                   
    return numIslands

grid = [[0,0,1,1,0,1,0,0,1,0],
        [1,1,0,1,1,0,1,1,1,0],
        [1,0,1,1,1,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,0,1],
        [0,0,0,0,0,0,1,1,1,0],
        [0,1,0,1,0,1,0,1,1,1],
        [1,0,1,0,1,1,0,0,0,1],
        [1,1,1,1,1,1,0,0,0,0],
        [1,1,1,0,0,1,0,1,0,1],
        [1,1,1,0,1,1,0,1,1,0]]
print (closedIsland(grid))