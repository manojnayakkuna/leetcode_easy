# -*- coding: utf-8 -*-
"""
Created on Thu May 28 02:28:13 2020

@author: manoj
"""

def needsAdjustment(digits):
    for i in range(len(digits)-1,-1,-1):
        if digits[i] == 9:
            digits[i] = 0
            if i == 0:
                digits.insert(0,1)
        else:
            digits[i] += 1
            break
    
    return digits

inputs = [1,2,3]
inputs = [4,3,2,1]
inputs = [1,2,9]
inputs = [1,9,9]
inputs = [9,9,9]
inputs = [2,4,9,3,9]
print (needsAdjustment(inputs))
