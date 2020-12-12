# -*- coding: utf-8 -*-
"""
Created on Wed May 20 19:44:07 2020

@author: manoj
"""

def pascalTriangle(nums):
    result = []
    #first_row = []
    #first_row.append(1)
    #result.append(first_row)
    result.append([1])
    
    for i in range(1,nums):
        temp = []
        temp.append(1)
        for j in range(1,i):
            #prev_list = result[i-1]
            #temp.append(prev_list[j-1]+prev_list[j])
            temp.append(result[i-1][j-1]+result[i-1][j])
        temp.append(1)
        result.append(temp)
    return result

nums = 5
result = pascalTriangle(5)
print ('result:', result)
for i in range(len(result)):
    print((nums-i)*' ', result[i])