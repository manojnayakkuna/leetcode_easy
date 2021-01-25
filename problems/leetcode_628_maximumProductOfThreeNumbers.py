# -*- coding: utf-8 -*-
"""
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
Example 1:
Input: nums = [1,2,3]
Output: 6
Example 2:
Input: nums = [1,2,3,4]
Output: 24
Example 3:
Input: nums = [-1,-2,-3]
Output: -6
"""

def maximumProduct(nums):
    
    if len(nums) <= 3:
        return nums[0]*nums[1]*nums[2]
    
    nums.sort()
    if nums[0] >= 0:
        return nums[-1]*nums[-2]*nums[-3]
    else:
        return max(nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[-3])
        #return nums[-1]*max(nums[0]*nums[1],nums[-3]*nums[-2])
    
    #return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])