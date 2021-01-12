# -*- coding: utf-8 -*-
"""
Created on Sat May 23 00:02:01 2020

@author: manoj
"""

def removeElement(arr,val):
    j = 0
    print ('len(arr):',len(arr))
    for i in range(len(arr)):
        if arr[i] != val:
            arr[j],arr[i] = arr[i],arr[j]
            j = j + 1
    print ('arr:', arr)
    return j
    
arr = [0,1,2,2,3,0,4,2]
val = 2
print (removeElement(arr,val))

arr = [3,2,2,3]
val = 3
print (removeElement(arr,val))