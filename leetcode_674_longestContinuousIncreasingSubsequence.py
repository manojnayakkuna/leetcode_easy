# -*- coding: utf-8 -*-
"""
Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.
A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].
Example 1:
Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.
Example 2:
Input: nums = [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
increasing.
"""
def findLengthOfLCIS(nums):
    if len(nums) <= 0:
        return 0
    count = 1
    maxCount = 0
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            count += 1
        else:
            maxCount = max(maxCount, count)
            count = 1
    maxCount = max(maxCount, count)
    return maxCount

#Using List and DP
def findLengthOfLCIS1(nums):
    if len(nums) < 1:
        return 0
    L = [1 for _ in range(len(nums))]
    maxlength = 1
    for i in range(1,len(nums)):
        if nums[i-1] < nums[i]:
            L[i] = L[i-1] + 1
        if L[i] > maxlength:
            maxlength = L[i]
    return maxlength