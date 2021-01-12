# -*- coding: utf-8 -*-
"""
Created on Wed May 20 01:36:42 2020

@author: manoj
"""
#Time Complexity : O(n*n)/O(n^2), can handle negative values too
def twoSum(nums,target):
    returnList = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                returnList.append(i)
                returnList.append(j)
    return returnList

#Time Complexity : O(n), Cannot handle negative values
def twoSumCustom(nums,target):
    returnList = []
    i = 0
    j = len(nums) - 1
    while j > 0 and i < len(nums):
        sumVal = nums[i] + nums[j]
        #print ('sumVal:',sumVal, 'target:', target)
        if sumVal > target:
            j -= 1
        elif sumVal < target:
            i += 1
        else:
            returnList.append(i)
            returnList.append(j)
            return returnList 
    return returnList

def twoSumUsingDict(nums,target):
    dataDict = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in dataDict:
            return [dataDict[diff],i]
        dataDict[nums[i]] = i
    return []

def twoSumIndex(arr,target):
    result = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] +arr[j] == target:
                result.append(i+1)
                result.append(j+1)
                return result
        
nums = [2,7,11,15]
print ('result twoSum         :', twoSum(nums,9))
print ('result twoSumCustom   :', twoSumCustom(nums,9))
print ('result twoSumUsingDict:', twoSumUsingDict(nums,9))
print ()

nums = [-1,-2,-3,-4,-5]
print ('result twoSum         :', twoSum(nums,-8))
print ('result twoSumCustom   :', twoSumCustom(nums,-8))
print ('result twoSumUsingDict:', twoSumUsingDict(nums,-8))
print ()

nums = [3,2,4]
print ('result twoSum         :', twoSum(nums,6))
print ('result twoSumCustom   :', twoSumCustom(nums,6))
print ('result twoSumUsingDict:', twoSumUsingDict(nums,6))