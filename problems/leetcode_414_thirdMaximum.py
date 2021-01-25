# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 23:17:10 2020

@author: manoj
"""

# Using traditional method of going through all elements
def thirdMax(nums):
    if len(nums) < 3:
        return max(nums)
    minArray = []
    for i in range(len(nums)):
        if len(minArray) < 3 and nums[i] not in minArray:
            minArray.append(nums[i])
        else:
            if nums[i] not in minArray and nums[i] > min(minArray):
                minArray.remove(min(minArray))
                minArray.append(nums[i])    
    if len(minArray) < 3:
        return max(minArray)
    else:
        return min(minArray)
    
#Usng heap sort
# 1. Create a minHeap of size k (here it is 3)
# 2. Add a number to heap if not found, then run heapify everytime for new element and pop
#    the 4th element from the heap
# 3. Return the 1st element from the heap, as it's minHeap the first element will hold the
#    the 3rd highest value.

def runHeapify(heap, num):
    