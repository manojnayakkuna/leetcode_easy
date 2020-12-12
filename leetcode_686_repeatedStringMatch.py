# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 17:25:36 2020

@author: manoj
"""

def repeatedStringMatch(A, B):
    if len(A) <= 0:
        return -1
    if len(B) <= 0:
        return -1
    
    #count = len(A)
    count = len(B)//len(A)+1
    mulVal = 1
    while mulVal <= count+2:
        if B in A*mulVal:
            return mulVal
        mulVal += 1
    return -1
"""    
    while len(A) < len(B):
        A = A + tempA
        mulVal = mulVal + 1
""" 

"""        
        for i in range(len(A)):
            if len(A[i:i+len(B)]) < len(B):
                break
            
            if A[i:i+len(B)] == B:
                return mulVal
        A = A + tempA
        mulVal += 1
"""

def internetMethod(A,B):
    b=len(B)//len(A)+1
    print ('b:',b)
    for i in range(1,b+2):
        if B in i*A:
            return i
    return -1

A = "abcd"
B = "cdabcdab"

A = "aa"
B = "a"

A = "abc"
B = "cabcabca"
print (repeatedStringMatch(A,B))