# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 23:56:57 2020

@author: manoj
"""
#Using 2 dictionaries

class Solution:
    def romanToInt(self, s: str) -> int:
        sym = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        specialCase = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        
        total = 0
        ignoreIndex = []
        for i in range(len(s)):
            if i < len(s) -1 and (s[i]+s[i+1]) in specialCase:
                ignoreIndex.append(i+1)
                total = total + specialCase[s[i]+s[i+1]]
            else:
                if i not in ignoreIndex:
                    total = total + sym[s[i]]
        return total

#Using 1 dictionaries
#In a normal roman number the number preceding them should be greater if not then it is a special case like IV, IX,...
class Solution1:
    def romanToInt(self, s: str) -> int:        
        romans  = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        prev = None
        result = 0
        for c in s:
            val = romans[c]
            if prev and val > prev:
                result -= 2 * prev
            else:
                prev = val
            result += val
                
        return result