# -*- coding: utf-8 -*-
"""
On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.
You can move according to the next rules:
In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
You have to visit the points in the same order as they appear in the array.
Example 1:
Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds
"""

""" Mathematical Geometric Logic:
# A = [x,y], B = [x1,y1]
# distance/time to reach from A to B will be [x1-x, y1-y]
# to make it optimum we need to cover max distance diagonaly
# so get diff betn [x1-x, y1-y] and  the extra distance in any of the 2 elements will be 
    the dist which shall be
# covered linearly
"""
def minTimeToVisitAllPoints(points):
    xCurrPos, yCurrPos = points[0][0], points[0][1]
    tot = 0
    for i in range(1,len(points)):
        tot += max(abs(points[i][0]-xCurrPos), abs(points[i][1]-yCurrPos))
        xCurrPos, yCurrPos=points[i][0], points[i][1]
    return tot