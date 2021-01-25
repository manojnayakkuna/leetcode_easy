# -*- coding: utf-8 -*-
"""
Given an array of integers arr, replace each element with its rank.
The rank represents how large the element is. The rank has the following rules:
Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
Example 1: Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.
"""
#Time - 88%
def arrayRankTransform(arr):
    copy = sorted(arr)
    d = {}
    counter = 1
    prevVal = None
    for val in copy:
        if prevVal != val:
            d[val] = counter
            counter += 1
            prevVal = val
    return [d[num] for num in arr]

#This approach does not work for the duplicate values scenario: [40,10,20,30,30,50]
def arrayRankTransformUniqueValues(arr):
    copy = sorted(arr)
    result = [copy.index(num)+1 for num in arr]
    return result