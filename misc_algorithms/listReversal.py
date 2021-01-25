# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:32:58 2020

@author: manoj
"""

def listReversalUsingSplice(arr):
    return arr[::-1]

def listReversalUsingExtraSpace(arr):
    result = []
    for i in range(len(arr)-1,-1,-1):
        result.append(arr[i])
    return result

def listReversalInPlace(arr):
    n = len(arr) // 2
    for i in range(n):
        arr[i],arr[-i-1] = arr[-i-1],arr[i]
    return arr

arr = ['adc','aaa','manoj','kumar','nayak','using']
print ('listReversalUsingSplice    :',listReversalUsingSplice(arr))
print ('listReversalUsingExtraSpace:',listReversalUsingExtraSpace(arr))
print ('listReversalInPlace        :',listReversalInPlace(arr))