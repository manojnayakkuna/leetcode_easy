# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 01:21:31 2020

@author: manoj
"""
"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
After doing so, return the array.
Example 1:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
"""
#In-Place but takes a lots of time to run - Bad performance
def replaceElementsInplace(arr):
    
    for i in range(len(arr)):
        if i == len(arr) - 1:
            arr[i] = -1
        else:
            arr[i] = max(arr[i+1:])
    return arr
    
#Extra Space - Good Performance but takes an additional O(N) space
def replaceElements(arr):
    lis = [-1]
    if len(arr) > 1:
        last_max = -1
        for index in range( len(arr) - 1, 0, -1):
            if arr[index] > last_max:
                lis.append(arr[index])
                last_max = arr[index]
            else:
                lis.append(last_max)
        lis.reverse()
        return lis
    else:
        return lis