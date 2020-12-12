# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 23:01:28 2020

@author: manoj
"""

def isPalindrome(s):
    if len(s) <= 0:
        return True
    
    newStr = ''
    for char in s:
        if char.isalnum():
            newStr += char.lower()
    
    newStrList = list(newStr)
    i = 0
    j = len(newStrList) - 1 
    
    while i <= j:
        if newStrList[i] != newStrList[j]:
            return False
        i = i + 1
        j = j - 1
        
    return True