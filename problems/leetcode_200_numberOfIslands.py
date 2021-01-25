# -*- coding: utf-8 -*-
"""
Created on Tue May 12 01:48:55 2020

@author: manoj
"""
def dfs(i,j,grid,visited):
    dir = [[1,0],[-1,0],[0,1],[0,-1]]
    n = len(grid)
    m = len(grid[0])
    for d in dir:
        ni, nj = i + d[0], j + d[1]
        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1 and [ni,nj] not in visited:
            visited.append([ni,nj])
            dfs(ni,nj,grid,visited)
    
def numOfIslands(grid):
    countIsland = 0
    if len(grid) > 0:
        visited = []        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and [i,j] not in visited:
                    visited.append([i,j])
                    dfs(i,j,grid,visited)
                    print ('visited:', visited)
                    countIsland += 1
                
    return countIsland

def numOfIslandsStack(grid):
    rows_count = len(grid)
    cols_count = len(grid[0]) if grid else 0
    num_islands = 0
    stack = []
    for i in range(rows_count):
        for j in range(cols_count):
            if grid[i][j] == 1:
                num_islands += 1
                stack.append((i, j))
                while stack:
                    ci, cj = stack.pop()
                    grid[ci][cj] = 0
                    dir = [[1,0],[-1,0],[0,1],[0,-1]]
                    for d in dir:
                        nr, nc = ci + d[0], cj + d[1]
                        if 0 <= nr < rows_count and 0 <= nc < cols_count and grid[nr][nc] == 1:
                            stack.append((nr, nc))
                '''
                    if ci > 0 and grid[ci - 1][cj] == 1:
                        stack.append((ci - 1, cj))

                    if ci < rows_count - 1 and grid[ci + 1][cj] == 1:
                        stack.append((ci + 1, cj))

                    if cj > 0 and grid[ci][cj - 1] == 1:
                        stack.append((ci, cj - 1))

                    if cj < cols_count - 1 and grid[ci][cj + 1] == 1:
                        stack.append((ci, cj + 1))
                '''
    return num_islands

grid = [[1,1,1,1,0],
        [1,1,0,1,0],
        [1,1,0,0,0],
        [0,0,0,0,0]]
print ('using recursive result:',numOfIslands(grid))
print ('using stack result    :',numOfIslandsStack(grid))

grid = [[1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,1]]
print ('using recursive result:',numOfIslands(grid))
print ('using stack result    :',numOfIslandsStack(grid))

grid = [[1]]
print ('using recursive result:',numOfIslands(grid))
print ('using stack result    :',numOfIslandsStack(grid))

grid = []
print ('using recursive result:',numOfIslands(grid))
print ('using stack result    :',numOfIslandsStack(grid))

grid = [[1,1]]
print ('using recursive result:',numOfIslands(grid))
print ('using stack result    :',numOfIslandsStack(grid))

grid = [[1,1,1,1,1,1,1,0],
        [1,0,0,0,0,1,1,0],
        [1,0,1,0,1,1,1,0],
        [1,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,0]]
print ('using recursive result:',numOfIslands(grid))
print ('using stack result    :',numOfIslandsStack(grid))

grid = [[0,0,1,0,0],
        [0,1,0,1,0],
        [0,1,1,1,0]]
print ('using recursive result:',numOfIslands(grid))
print ('using stack result    :',numOfIslandsStack(grid))





