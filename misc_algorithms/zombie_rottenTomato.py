# -*- coding: utf-8 -*-
"""
Created on Thu May 14 18:39:52 2020

@author: manoj
"""

def zombieSolutions(grid):
    if len(grid) <= 0:
        return -1
    
    m = len(grid)
    n = len(grid[0]) if grid else 0
    
    queue = [[i,j] for i in range(m) for j in range(n) if grid[i][j] == 1]
    dir = [[1,0],[-1,0],[0,1],[0,-1]]
    count = 0
    
    while len(queue) > 0:
        new_queue = []
        for q in queue:
            i = q[0]
            j = q[1]
            if grid[i][j] == 1:
                for d in dir:
                    ni, nj = i+d[0], j+d[1]
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 0:
                        grid[ni][nj] = 1
                        new_queue.append([ni,nj])
        count = count + 1
        queue = new_queue
    
    return count

grid = [[0, 1, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0]]
print ('result 1:',zombieSolutions(grid))

grid = [[1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1]]
print ('result 2:',zombieSolutions(grid))
    