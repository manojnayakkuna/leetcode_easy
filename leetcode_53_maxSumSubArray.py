# -*- coding: utf-8 -*-
"""
Created on Thu May 28 02:03:26 2020

@author: manoj
"""

def maxSumSubArray(arr,n):
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    
    max_value = 0
    max_sofar = 0
    
    for i in range(len(arr)):
        if i == 0:
            max_value = arr[0]
            max_sofar = arr[0]
        else:
            max_value = max(max_value+arr[i],arr[i])
            if max_value > max_sofar:
                max_sofar = max_value
    return max_sofar

arr = [-2,1,-3,4,-1,2,1,-5,4]
print ('maxSumSubArray:',maxSumSubArray(arr,len(arr)))