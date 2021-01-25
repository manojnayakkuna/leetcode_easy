# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 02:02:19 2020

@author: manoj
"""
def combinationsStr(arr):
    if len(arr) == 0:
        return [[]]
    combinations = []
    for c in combinationsStr(arr[1:]):
        combinations += [c, c+[arr[0]]]
    return combinations

import copy
def combinations(target,data):
    for i in range(len(data)):
         new_target = copy.copy(target)
         new_data = copy.copy(data)
         new_target.append(data[i])
         new_data = data[i+1:]
         combinations(new_target,new_data)

#arr = list('1234')
arr = [1,2,3,4]
combs = combinationsStr(arr)
print(combs)