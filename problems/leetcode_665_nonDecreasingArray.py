# -*- coding: utf-8 -*-
"""
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).
Example 1:
Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.
"""

def checkPossibility(nums):
    if len(nums) == 1:
        return True
    count = 0
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            if count > 0:
                return False
            if i+1 < len(nums)-1 and i > 0:
                if nums[i] > nums[i+2] and nums[i-1] > nums[i+1]:
                    return False
            count += 1
    return True

#Method 2: Using 2 array brute force
def check_non_dec(arr):
    print("new arr - ", arr)
    for i in range(len(arr)-1):
        if arr[i] <= arr[i+1]:
            continue
        else:
            return False
    return True
	
def checkPossibility1(nums):
    new_arr1 = nums[:]
    new_arr2 = nums[:]
    for i in range(len(nums)-1):
        if nums[i] <= nums[i+1]:
            continue
        else:
            if i == 0:
                new_arr1[i] = nums[i+1]
                new_arr2[i+1] = nums[i]
            else:
                new_arr1[i+1] = nums[i]
                new_arr2[i] = nums[i+1]
            print(new_arr1, new_arr2)
            return (self.check_non_dec(new_arr1) or self.check_non_dec(new_arr2))
    return True