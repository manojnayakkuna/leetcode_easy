# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 00:43:11 2020

@author: manoj
"""

def lengthOfLastWord(s):
    strList = s.split()
    #strList = list(s.split())
    if len(strList) == 0:
        return 0
    else:
        return len(strList[-1])