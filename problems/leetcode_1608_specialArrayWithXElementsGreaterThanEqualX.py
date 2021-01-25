# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 23:42:44 2020

@author: manoj
"""

"""
You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.
Notice that x does not have to be an element in nums.
Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.
Example 1:
Input: nums = [3,5]
Output: 2
Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.
"""
def specialArrayCorrect(nums):
    s = max(nums)
    for val in range(s+1):
        greaterCount = 0
        for item in nums:
            if item >= val:
                greaterCount += 1
            if greaterCount > val:
                break
        if greaterCount == val:
            return val
    return -1

#This below method checks of if each variable in nums is greater than equal to the length of nums
def specialArray(nums):
    
    nums = [x for x in nums if x > 0]
    if len(nums) <= 0:
        return -1
    countGreater = [x for x in nums if x >= len(nums)]
    if len(countGreater) == len(nums):
        return len(countGreater)
    else:
        return -1

#More Optimized Way - Using sorting and bisect technique
def specialArray(self, nums: List[int]) -> int:
    """
    if we sort [0, 0, 3, 4, 4]   ---> For any number in a sorted array, we can know how many numbers are less than with respect to the length of the array
    if no number fit == -1
    we begin with 1 and bisect left, if idx - length = idx return True if idx == length return -1 (idx > max)
    else we increment idx
    """

    nums.sort()
    i = 1
    while True:
        insertion_idx = bisect_left(nums, i)
        if len(nums) - insertion_idx == i:
            return i
        elif insertion_idx == len(nums):
            return -1
        i += 1