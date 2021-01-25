# -*- coding: utf-8 -*-
"""
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
Example 1:
Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:
Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
"""
#Brute Force Method
def threeConsecutiveOdds(arr):
    for i in range(len(arr)-2):
        if arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i+2] % 2 == 1:
            return True
    return False

#DP Solution
def threeConsecutiveOdds1(arr):
    counter = 0
    for num in arr:
        if num % 2 == 0:
            counter = 0
        else:
            counter += 1
            if counter == 3:
                return True
    return False