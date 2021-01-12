# -*- coding: utf-8 -*-
"""
Created on Tue May  5 02:08:28 2020

@author: manoj
"""

def is_palindrome(inputstr):
    if len(inputstr) < 2:
        return -1
    
    countLoop = len(inputstr) // 2
    
    for i in range(countLoop):
        if inputstr[i].lower() == inputstr[-i-1].lower():
            pass
        else:
            return False
    
    return True

import re

def is_palindrome1(inputstr):
    if len(inputstr) < 2:
        return -1
    
    forward = ''.join(re.findall(r'[a-z]+',inputstr.lower()))
    backward = forward[::-1]
    return forward == backward


str1 = 'Manoj'
print (is_palindrome1(str1))

str2 = 'NayaN'
print (is_palindrome1(str2))
        
        
            