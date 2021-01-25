# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 23:22:35 2020

@author: manoj
"""
"""
Given an integer array arr, return the mean of the remaining integers after removing the smallest 5% and the largest 5% of the elements.
Answers within 10-5 of the actual answer will be considered accepted.
Example 1:
Input: arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
Output: 2.00000
Explanation: After erasing the minimum and the maximum values of this array, all elements are equal to 2, so the mean is 2.
"""
def trimMean(arr):
    if len(arr) < 20 or len(arr) > 1000:
        return 0.0    
    arr.sort()
    removeCount = int(.05 * len(arr))    
    return (sum(arr[removeCount:-removeCount])/len(arr[removeCount:-removeCount]))