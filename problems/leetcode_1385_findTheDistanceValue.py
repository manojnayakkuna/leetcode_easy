# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 12:38:25 2020

@author: manoj
"""

def findTheDistanceValue(arr1,arr2,d):
    counter = 0
    for i in range(len(arr1)):
        print ('i:',i)
        flag = True
        for j in range(len(arr2)):
            if abs(arr1[i]-arr2[j]) <= d:
                flag = False
                break
        print ('counter:', counter)
        if (flag):
            counter += 1
    
    return counter

arr1 = [4,5,8,3]
arr2 = [10,9,1,8]
d = 2
print (findTheDistanceValue(arr1,arr2,d))