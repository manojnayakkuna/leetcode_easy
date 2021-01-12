# -*- coding: utf-8 -*-
"""
Created on Tue May 19 00:38:19 2020

@author: manoj
"""

def permutationsStr(arr):
    if len(arr) < 0:
        return -1
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return arr
    else:
        permutations = []
        for i in range(len(arr)):
            x = arr[i]
            xs = arr[:i] + arr[i+1:]
            for p in permutationsStr(xs):
                permutations.append([x] + list(p))
        return permutations

arr = list('abc')
#permutations = permutationsStr(arr)
#print(permutations)
for p in permutationsStr(arr):
    print (p)