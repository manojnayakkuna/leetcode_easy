# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 01:35:08 2020

@author: manoj
"""

def runningSum(nums):
    prevVal = 0
    for i in range(len(nums)):
        nums[i] += prevVal
        prevVal = nums[i]
    return nums