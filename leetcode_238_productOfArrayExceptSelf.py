# -*- coding: utf-8 -*-
"""
Created on Thu May 21 23:07:25 2020

@author: manoj
"""

def productArray(arr):
    if len(arr) <= 1:
        return []
    
    output = []
    output.append(1)
    for i in range(1,len(arr)):
        output.append(output[i-1]*arr[i-1])
    
    print ('output:',output)
    R = 1
    for i in range(len(arr)-1,-1,-1):
        print ('i:',i,'R:',R,'output[i]:',output[i],'arr[i]:',arr[i])
        output[i] = R * output[i]
        R = R * arr[i]
    
    return output
    
inputArr = [1,2,3,4]
print ('result:',productArray(inputArr))