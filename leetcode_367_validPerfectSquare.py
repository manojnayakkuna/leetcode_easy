# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 01:44:50 2020

@author: manoj
"""
#This below approach works only for perfect square of 2's
def isPerfectSquare(num):
    
    c = 0
    while num>0:
        if num&1 == 1:
            c += 1
        num >>= 1
    
    if c > 1:
        return False
    else:
        return True

#Optimized method: using binary search

def isPerfectSquare1(num):
    
    left = 0
    right = num
    
    while left < right:
        mid = left + (right - left)//2
        if mid * mid == num:
            return True
        elif mid * mid > num:
            right = mid
        else:
            left = mid
        
    return False
