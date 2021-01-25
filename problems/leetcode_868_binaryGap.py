# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 11:05:37 2020

@author: manoj
"""
"""
Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. If there are no two adjacent 1's, return 0.
Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute difference between their bit positions. For example, the two 1's in "1001" have a distance of 3.
Example 1:
Input: n = 22
Output: 2
Explanation: 22 in binary is "10110".
The first adjacent pair of 1's is "10110" with a distance of 2.
The second adjacent pair of 1's is "10110" with a distance of 1.
The answer is the largest of these two distances, which is 2.
Note that "10110" is not a valid pair since there is a 1 separating the two 1's underlined.
"""
#Optimzed Approach - 80%
def binaryGap(n):
    string = ''
    while n:
        if (n&1 == 0):
            string = '0' + string
        else:
            string = '1' + string
        n >>= 1
    binaryVal = list(int(x) for x in string)
    maxIndexDiff = 0
    prevIndex = None
    for i in range(len(binaryVal)):
        if binaryVal[i] == 1:
            if prevIndex is None:
                prevIndex = i
            else:
                maxIndexDiff = max(maxIndexDiff,i-prevIndex)
                prevIndex = i
    return maxIndexDiff

#Using Lambda
def binaryGapLambda(n):
    return(lambda h:h(h))(lambda g:lambda n,b,c:g(g)(*((n>>1,[b,c][c>b],1)if n&1else(n>>1,b,c+1)))if n else b)(n//(n&-n),0,0)

#Using Recursion
def binaryGapRecursion(n, b=0, c=0):
    return binaryGap(*(lambda n:((n>>1,b,c+1),(n>>1,(b,c)[c>b],1))[n&1])(n//(n&-n,1)[c>0]))if n else b

#Optimized Way
def binaryGapOptWay(n):
    n = n // (n & -n)  #Strip 0s from the right side of n
    best = gap = 0
    while n > 0:
        if n & 1:
            best = max(best, gap)
            gap = 1
        else:
            gap += 1
        n >>= 1
    return best

print(binaryGapOptWay(22))