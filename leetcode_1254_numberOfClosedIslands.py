# -*- coding: utf-8 -*-
"""
Created on Sat May 30 00:42:34 2020

@author: manoj
"""

"""
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally 
connected group of 0s and a closed island is an island totally (all left, top, right, bottom) 
surrounded by 1s.

Return the number of closed islands.
"""

#Base Code: Not Working
"""
def closedIsland(self, grid: List[List[int]]) -> int:
    countIsland = 0
    if len(grid) > 0:
        visited = []        
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                if grid[i][j] == 0 and [i,j] not in visited:
                    visited.append([i,j])
                    if (self.dfs(i,j,grid,visited)):
                        countIsland += 1                
    return countIsland

def dfs(self,i,j,grid,visited):
    dir = [[1,0],[-1,0],[0,1],[0,-1]]
    n = len(grid)
    m = len(grid[0])
    for d in dir:
        ni, nj = i + d[0], j + d[1]
        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] != 1 and [ni,nj] not in visited:
            visited.append([ni,nj])
            if (not self.dfs(ni,nj,grid,visited)):
                return False
    return True
"""
    
def isOnBoundary(i,j,rows,cols):
    return i == 0 or j == 0 or i == rows - 1 or j == cols - 1
    
def dfs(i,j,grid,rows,cols):
    #if grid[i][j] == 1 or [i,j] in visited:
    #if grid[i][j] == 1:
    if grid[i][j] == 1 or grid[i][j] == -1:
        return True
    
    if isOnBoundary(i,j,rows,cols):
        return False
    
    grid[i][j] = -1
    #grid[i][j] = 1

    left = dfs(i,j-1,grid,rows,cols)
    right = dfs(i,j+1,grid,rows,cols)
    up = dfs(i-1,j,grid,rows,cols)
    down = dfs(i+1,j,grid,rows,cols)
    
    return left and right and up and down

def numOfIslands(grid):
    if len(grid) == 0 or len(grid[0]) == 0:
        return 0
    
    countIsland = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(1,len(grid)-1):
        for j in range(1,len(grid[0])-1):
            if grid[i][j] == 0:
                if (dfs(i,j,grid,rows,cols)):
                    #print ('visited:',visited)
                    countIsland += 1  
    return countIsland

def dfsNew(i,j,grid):
    dir = [[1,0],[-1,0],[0,1],[0,-1]]
    n = len(grid) - 1
    m = len(grid[0]) - 1
    
    #if n < i < 0 or m < j < 0:
    if not 0 <= i < n and 0 <= j < m:
        return False
    
    if grid[i][j] == 1:
        return True
    
    grid[i][j] = 1
    for d in dir:
        ni, nj = i + d[0], j + d[1]
        if (not dfsNew(ni,nj,grid)):
            grid[i][j] = 0
            return False
    
    grid[i][j] = 1
    return True

def numOfIslandsWithoutVisited(grid):
    countIsland = 0
    #if len(grid) > 0:   
    for i in range(1,len(grid)-1):
        for j in range(1,len(grid[0])-1):
            if grid[i][j] == 0:
                if (dfsNew(i,j,grid)):
                    countIsland += 1        
    return countIsland


grid = [[1,1,1,1,1,1,1,0],
        [1,0,0,0,0,1,1,0],
        [1,0,1,0,1,1,1,0],
        [1,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,0]]
print ('using recursive result:',numOfIslands(grid))

grid = [[0,0,1,0,0],
        [0,1,0,1,0],
        [0,1,1,1,0]]
print ('using recursive result:',numOfIslands(grid))

grid = [[1]]
print ('using recursive result:',numOfIslands(grid))

grid = [[1,1,1,1,0],
        [1,0,0,0,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1]]
print ('using recursive result:',numOfIslands(grid))

grid = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1],
        [1,0,1,1,1,0,1],
        [1,0,1,0,1,0,1],
        [1,0,1,1,1,0,1],
        [1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1]]
print ('using recursive result:',numOfIslands(grid))

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
print ('using recursive result:',numOfIslands(grid))









