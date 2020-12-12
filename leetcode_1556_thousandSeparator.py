# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:57:33 2020

@author: manoj
"""

"""
Given an integer n, add a dot (".") as the thousands separator and return it in string format.
Example 1:
Input: n = 987
Output: "987"

Example 2:
Input: n = 1234
Output: "1.234"
"""

def thousandSeparator(self, n: int) -> str:
    
    if n == 0:
        return "0"
    
    s = str(n)
    if len(s) <= 3:
        return s
    else:
        s = s[::-1]
        s = [s[i:i+3] for i in range(0, len(s), 3)]
        s = '.'.join(s)
        return s[::-1]