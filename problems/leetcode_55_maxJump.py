# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 00:08:06 2020

@author: manoj
"""

def maxJump(nums):
    if len(nums) == 1:
        return True
    
    if len(nums) > 1:
        if nums[0] == 0:
            return False
    print ('passed base check')
    maxJump = 0
    for i in range(len(nums)):
        if i > maxJump:
            return False
        print ('bef maxJump:',maxJump)
        maxJump = max(maxJump,i + nums[i])
        print ('aft maxJump:',maxJump)

    return True
    
nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
print (maxJump(nums))