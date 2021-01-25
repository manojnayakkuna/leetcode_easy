# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 00:03:41 2020

@author: manoj
"""

def reverseVowels(inputString):
    if len(inputString) <= 0:
        return -1
    
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    
    inputStr = list(inputString)
    
    forwardPtr = 0
    backwardPtr = len(inputStr) - 1
    
    forwardInd = 'N'
    backwardInd = 'N'
    
    while (forwardPtr < backwardPtr):
        if inputStr[forwardPtr] in vowels:
            forwardInd = 'Y'
        if inputStr[backwardPtr] in vowels:
            backwardInd = 'Y'
        
        if forwardInd == 'N' and backwardInd == 'N':
            forwardPtr += 1
            backwardPtr -= 1
        elif forwardInd == 'Y' and backwardInd == 'N':
            backwardPtr -= 1
        elif forwardInd == 'N' and backwardInd == 'Y':
            forwardPtr += 1
        elif forwardInd == 'Y' and backwardInd == 'Y':
            inputStr[forwardPtr], inputStr[backwardPtr] = inputStr[backwardPtr], inputStr[forwardPtr]
            forwardPtr += 1
            backwardPtr -= 1
            forwardInd = 'N'
            backwardInd = 'N'
    
    return ''.join(inputStr)
        
input1 = 'hello'
result = reverseVowels(input1)
print ('result:', result)

input1 = 'leetcode'
result = reverseVowels(input1)
print ('result:', result)
    
    