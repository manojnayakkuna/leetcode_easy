# -*- coding: utf-8 -*-
"""
Created on Wed May 20 19:37:52 2020

@author: manoj
"""

def hasDuplicate(arr):
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            return True
    return False

def hasDuplicateMap(arr):
    dataDict = {}
    for i in range(len(arr)):
        if arr[i] not in dataDict:
            dataDict[arr[i]] = 1
        else:
            return True
    return False
        
arr = [1,2,3,4,5,6]
print ('result using array:', hasDuplicate(arr))

arr = [1,2,2,3,4,5,6]
print ('result using dataDict:', hasDuplicateMap(arr))