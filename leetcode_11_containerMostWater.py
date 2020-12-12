# -*- coding: utf-8 -*-
"""
Created on Mon May 25 00:30:40 2020

@author: manoj
"""

def containerMostWater(arr,n):
    if n <= 0:
        return 0
    
    result = 0
    for i in range(len(arr)):
        length = 0
        tempresult = 0
        for j in range(i,len(arr)):
            Area = min(arr[i],arr[j]) * length
            if tempresult < Area:
                tempresult = Area
            length +=  1
        if result < tempresult:
            result = tempresult
        
    return result

def twoPointerApproach(height,n):
    if len(height) <= 0:
        return 0

    result = 0
    max_water = float("-inf")
    left = 0
    right = len(height) - 1
    while left < right:
        length = (right - left)
        result = max(result, length * min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return result

arr = [1,8,6,2,5,4,8,3,7]
print ('result:',containerMostWater(arr,len(arr)))

height = [1,8,6,2,5,4,8,3,7]
print ('result:',twoPointerApproach(arr,len(height)))