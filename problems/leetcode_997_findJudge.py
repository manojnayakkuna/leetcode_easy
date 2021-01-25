# -*- coding: utf-8 -*-
"""
Created on Sat May 23 01:16:37 2020

@author: manoj
"""

def findJudge(N, trust):
    indexCount = [0 for _ in range(N)]
    for i in range(len(trust)):
        indexCount[trust[i][0]-1] = indexCount[trust[i][0]-1] - 1
        indexCount[trust[i][1]-1] = indexCount[trust[i][1]-1] + 1
    
    maxVal = max(indexCount)
    if maxVal == (N-1):
        for i in range(N):
            if indexCount[i] == maxVal:
                return i + 1
    else:
        return -1

trust = [[1,2]]
N = 2
print ('example 1:', findJudge(N,trust))

N = 3
trust = [[1,3],[2,3]]
print ('example 2:', findJudge(N,trust))

N = 3
trust = [[1,3],[2,3],[3,1]]
print ('example 3:', findJudge(N,trust))

N = 3
trust = [[1,2],[2,3]]
print ('example 4:', findJudge(N,trust))

N = 4
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
print ('example 5:', findJudge(N,trust))