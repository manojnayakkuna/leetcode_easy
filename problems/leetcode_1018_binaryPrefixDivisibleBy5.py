# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 00:59:22 2020

@author: manoj
"""

"""
Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i] interpreted as a binary number (from most-significant-bit to least-significant-bit.)
Return a list of booleans answer, where answer[i] is true if and only if N_i is divisible by 5.
Example 1:
Input: [0,1,1]
Output: [true,false,false]
Explanation: 
The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.  Only the first number is divisible by 5, so answer[0] is true.
"""

#Traditional approach of converting the binary to decimal and checking if its divisible by 5
def prefixesDivBy5(A):
    
    result = []
    subStr = ""
    for a in A:
        #n = ''.join([str(x) for x in A[:i+1]])
        subStr = subStr + str(a)
        if int(subStr,2) % 5 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
    
#Optimized Method
def prefixesDivBy5_Optimized(A):
    
    last = 0
    result = []
    for a in A:
        last <<= 1
        last = (last + a) % 10
        result.append(last == 0 or last == 5)
    return result