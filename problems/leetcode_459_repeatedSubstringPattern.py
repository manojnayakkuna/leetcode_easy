# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 00:14:14 2020

@author: manoj
"""

def repeatedSubstringPattern(s):
    if len(s) <= 1:
        return False
    
    if len(s) % 2 == 0:
        midpoint = len(s) // 2
    else:
        midpoint = (len(s) // 2) + 1
    print ('midpoint:',midpoint)
    
    compareLen = 1
    secodPointer = 0
    for i in range(midpoint):
        print ('i:',i,'s[:i+1]:', s[:i+1],'s[i+1:i+3]:',s[i+1:2*(i+1)])
        if s[:i+1] == s[i+1:2*(i+1)]:
            compareLen = i+1
            secodPointer = max(compareLen,secodPointer)
    
    print ('compareLen:',compareLen, 'secodPointer:',secodPointer)
    #for i in range(0,len(s)-compareLen,compareLen):
    for i in range(1,midpoint+1):
        print ('i:',i,'i+compareLen:',i+compareLen,'i+2*compareLen:',i+2*compareLen)
        #if s[0:compareLen] != s[i+compareLen:i+2*compareLen]:
        #    return False
        if s[:i] * int(len(s)/i) == s:
            return True
    
    return False

def internetMethod(s):
    if len(s) == 1: return False
    
    i, l= 1, len(s)
    while i < l/2 + 1:
        print ('int(l/i):',int(l/i))
        print ('i:',i,';s[:i]:',s[:i],';s[:i] * int(l/i):', s[:i] * int(l/i))
        if s[:i] * int(l/i) == s:
            return True
        i += 1
    return False

Input1 = "abab"
Input2 = "aba"
Input3 = "abcabcabcabc"
Input4 = "ababab"
Input4 = "abaaba"
Input5 = "abaababaab"
Input6 = "ababababab"
print (repeatedSubstringPattern(Input1))