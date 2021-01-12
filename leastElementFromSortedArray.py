# -*- coding: utf-8 -*-
"""
Created on Sun May 17 00:09:27 2020

@author: manoj
"""
def partition(arr,startLen,endLen):
    pivot = arr[endLen]
    i = startLen
    for j in range(startLen,endLen):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[i],arr[endLen] = arr[endLen], arr[i]
    return i

def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)
    return arr
    
def leastElementFromSortedArray(arr):
    quickSort(arr,0,len(arr)-1)
    #countArr = [0 for _ in range(len(arr))]
    holdCnt = 9999
    
    prevVal = None
    currCnt = 0
    currVal = None
    
    for i in range(len(arr)):
        if currVal == None:
            prevVal = arr[i]
            currVal = arr[i]
            currCnt += 1
        else:
            if currVal == arr[i]:
                currCnt += 1
            else:
                if currCnt < holdCnt:
                    prevVal = currVal
                    holdCnt = currCnt
                currVal = arr[i]
                currCnt = 1        
    return prevVal, holdCnt

arr = [1,9,3,3,3,5,1,1,5,4,5,4,7,6,1,2,2,4,5,2,9,7,7]
leastVal,leastCnt = leastElementFromSortedArray(arr)
print ('sorted arr:', arr)
print ('leastVal:',leastVal,'; leastCnt:',leastCnt)