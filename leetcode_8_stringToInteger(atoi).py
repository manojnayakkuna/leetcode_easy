# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 23:42:06 2020

@author: manoj
"""

class Solution:
    def myAtoi(self, str: str) -> int:
        import math
        if len(str) <= 0:
            return 0
        INT_MAX = pow(2,31) - 1
        INT_MIN = -1 * pow(2,31)
        stripStr = str.strip()
        
        captureInt = ''
        for i in range(len(stripStr)):
            if i == 0:
                if stripStr[i] == '+' or stripStr[i] == '-':
                    captureInt = captureInt+stripStr[i]
                elif stripStr[i].isdigit():
                    captureInt = captureInt+stripStr[i]
                else:
                    return 0
            else:
                if stripStr[i].isdigit():
                    captureInt = captureInt+stripStr[i]
                else:
                    break
                    
        if len(captureInt) > 0:
            if len(captureInt) == 1 and (captureInt[0] == '+' or captureInt[0] == '-'):
                return 0
            else:
                captureInt = int(captureInt)
                if captureInt > INT_MAX:
                    return INT_MAX
                if captureInt <= INT_MIN:
                    return INT_MIN
                return captureInt
        else:
            return 0