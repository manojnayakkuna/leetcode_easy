# -*- coding: utf-8 -*-
"""
Created on Mon May 25 12:22:50 2020

@author: manoj
"""
#Time Complexity : O(n)
def findFirstAndLastElementSortedArray(arr,n,target):
    result = [-1,-1]
    if n <= 0:
        return result
    
    for i in range(len(arr)):
        if arr[i] == target:
            if result[0] == -1:
                result[0] = i
            else:
                result[1] = i
    return result

#Time Complexity : O(log n)
def logNTimeComplex(arr,left,right,result,target):
    print ('inside logNTimeComplex left:',left, 'right:',right)
    if left <= right:
        #pointer = left + (right-left) // 2
        pointer = (left+right) // 2
        print ('pointer:', pointer)
        if target == arr[pointer]:
            j = left
            while j <= right:
                if arr[j] == target:
                    if result[0] == -1:
                        result[0] = j
                        result[1] = j
                    else:
                        result[1] = j
                j += 1
     #       return result
        elif target > arr[pointer]:
            return logNTimeComplex(arr,pointer+1,right,result,target)
        else:
            return logNTimeComplex(arr,left,pointer-1,result,target)
    else:
        return result
            
def internetMethod(arr,n,target):
    result = [-1,-1]
    if n <= 0:
        return result
    
    logNTimeComplex(arr,0,len(arr)-1,result,target)
    return result

"""
def partition(arr,low,high,result,target):
    pi = (high - low) // 2
    if target == arr[pi]:
        if result[0] == -1:
            result[0] = pi
        else:
            result[1] = pi
    return pi
    
def usingQuickSort(arr,low,high,result,target):
    if low < high:
        pi = partition(arr,low,high,result,target)
        usingQuickSort(arr,low,pi-1,result,target)
        usingQuickSort(arr,pi+1,high,result,target)

"""



print ('******************************************')
nums = [5,7,7,8,8,8,10]
target = 8
print ('result 1 O(n)    :', findFirstAndLastElementSortedArray(nums,len(nums),target))
print ('result 1 O(log n):', internetMethod(nums,len(nums),target))
#result = [-1,-1]
#print ('result 1 O(log n):', usingQuickSort(nums,0,len(nums)-1,result,target))
print ('******************************************')

nums = [5,7,7,8,8,10]
target = 6
print ('result 2 O(n)    :', findFirstAndLastElementSortedArray(nums,len(nums),target))
print ('result 2 O(log n):', internetMethod(nums,len(nums),target))
#result = [-1,-1]
#print ('result 3 O(log n):', usingQuickSort(nums,0,len(nums)-1,result,target))
print ('******************************************')

nums = [5,7,7,8,10]
target = 8
print ('result 3 O(n)    :', findFirstAndLastElementSortedArray(nums,len(nums),target))
print ('result 3 O(log n):', internetMethod(nums,len(nums),target))
#result = [-1,-1]
#print ('result 3 O(log n):', usingQuickSort(nums,0,len(nums)-1,result,target))
print ('******************************************')


nums = [1]
target = 1
print ('result 4 O(log n):', internetMethod(nums,len(nums),target))