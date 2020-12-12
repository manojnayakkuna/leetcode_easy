# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 23:45:06 2020

@author: manoj
"""
#Time Complexity: O(n)
def validPalindrome(s):
    if len(s) <= 0:
        return False
    
    for i in range(len(s)):
        newStr = s[:i] + s[i+1:]
        midpoint = len(newStr) // 2
        flag = 'Y'
        for j in range(midpoint):
            if newStr[j] != newStr[-j-1]:
                flag = 'F'
                break
        if (flag == 'Y'):
            return True
            break

#Time Complexity: O(n)
def validPalindromeAlt(s):
    if len(s) <= 0:
        return False
    
    for i in range(len(s)):
        newStr = s[:i] + s[i+1:]
        flag = 'Y'
        if newStr != newStr [::-1]:
            flag = 'N'
            
        if (flag == 'Y'):
            return True
            break

#Time Complexity: O(n/2)
def validPalindromeOptimum(s):
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                temp_1 = s[:start]+s[start+1:]
                temp_2 = s[:end]+s[end+1:]
                return temp_1 == temp_1[::-1] or temp_2 == temp_2[::-1]
            start += 1
            end -= 1
        return True

s = "aba"
#s = "abcb"
print (validPalindromeOptimum(s))