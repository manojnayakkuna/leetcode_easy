# -*- coding: utf-8 -*-
"""
Created on Fri May 29 23:58:59 2020

@author: manoj
"""

def dfs(i,j,grid,visited):
    dir = [[1,0],[-1,0],[0,1],[0,-1],[-1,-1],[-1,1],[1,-1],[1,1]]
    n = len(grid)
    m = len(grid[0])
    for d in dir:
        ni, nj = i + d[0], j + d[1]
        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1 and [ni,nj] not in visited:
            visited.append([ni,nj])
            dfs(ni,nj,grid,visited)
    
def numOfIslands8Ways(grid):
    countIsland = 0
    if len(grid) > 0:
        visited = []        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and [i,j] not in visited:
                    visited.append([i,j])
                    dfs(i,j,grid,visited)
                    print ('visited:',visited)
                    countIsland += 1
                
    return countIsland

grid = [[1,1,1,1,1,1,1,0],
        [1,0,0,0,0,1,1,0],
        [1,0,1,0,1,1,1,0],
        [1,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,0]]
print ('using recursive result:',numOfIslands8Ways(grid))

grid = [[0,0,1,0,0],
        [0,1,0,1,0],
        [0,1,1,1,0]]
print ('using recursive result:',numOfIslands8Ways(grid))

grid = [[1]]
print ('using recursive result:',numOfIslands8Ways(grid))

grid = [[1,1,1,1,0],
        [1,0,0,0,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1]]
print ('using recursive result:',numOfIslands8Ways(grid))