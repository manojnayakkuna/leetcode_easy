# -*- coding: utf-8 -*-
"""
Created on Thu May 28 01:18:58 2020

@author: manoj
"""

def maxSum(arr,n):
    if n == 0:
        return 0
    if n <= 2:
        return max(arr[0],arr[1],arr[0]+arr[1])
    
    value1 = arr[0]
    #value2 = arr[1]
    for i in range(1,len(arr)):
        max_value = max(value1,arr[i],value1+arr[i])
        value1 = max_value
    return value1

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSum(arr,len(arr)))