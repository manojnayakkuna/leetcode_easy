# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 20:27:50 2020

@author: manoj
"""

def strStr(haystack,needle):
        
        if len(needle) <= 0:
            return 0

        if len(haystack) <= 0:
            return -1

        if len(haystack) < len(needle):
            return -1
        elif len(haystack) == len(needle):
            if haystack == needle:
                return 0
            else:
                return -1
        elif len(haystack) > len(needle):
            for i in range(0,len(haystack) - len(needle)+1):
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1
    
haystack = "hello"
needle = "ll"

haystack = "a"
needle = "a"

print (strStr(haystack,needle))