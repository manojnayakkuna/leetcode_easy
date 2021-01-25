# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 23:56:18 2020

@author: manoj
"""
"""
"""

#This method does not work if we have dups in s & t
def isSubsequence(self, s: str, t: str) -> bool:
    prevIndex = None
    for char in s:
        if char in t:
            currIndex = t.index(char)
            if prevIndex is None:
                prevIndex = currIndex
            elif currIndex < prevIndex:
                return False
            else:
                prevIndex = currIndex
        else:
            return False
    return True

#Method which can handle dups in s & t
def isSubsequence1(s,t) -> bool:    
    prevIndex = -1
    for i in range(len(s)):
        if s[i] in t[prevIndex+1:]:
            currIndex = t.index(s[i], prevIndex+1)
            if currIndex < prevIndex:
                return False
            else:
                prevIndex = currIndex
        else:
            return False
        print ('prevIndex:', prevIndex)
    return True