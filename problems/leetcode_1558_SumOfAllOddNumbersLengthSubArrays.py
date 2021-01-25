# -*- coding: utf-8 -*-
"""
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.
A subarray is a contiguous subsequence of the array.
Return the sum of all odd-length subarrays of arr.
Example 1:
Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
"""

#Using while loop
def sumOddLengthSubarrays(arr):
    i = 0
    sumVal = 0
    while i <= len(arr):
        if i % 2 != 0:
            for j in range(len(arr)-i+1):
                sumVal += sum(arr[j:j+i])
        i += 1
    return sumVal

#Using List compression
def sumOddLengthSubarrays1(arr):
    i = 0
    sumVal = 0
    while i <= len(arr):
        if i % 2 != 0:
            sumVal += sum([sum(arr[j:j+i]) for j in range(len(arr)-i+1)])
        i += 1
    return sumVal