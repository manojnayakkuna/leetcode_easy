# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 20:34:51 2020

@author: manoj
"""
from collections import Counter

#This method can handle all test cases
def mostCommonWord(paragraph, banned):
    #newPara = ''.join(map(lambda x: x if x.isalpha() else ' ', paragraph)).split()
    paragraphList = [word.lower() for word in ''.join(map(lambda x: x if x.isalpha() else ' ', paragraph)).split() if word.lower() not in banned]
    elementDictCount = Counter(paragraphList)
    maxVal = max(elementDictCount.values())
    for key,value in elementDictCount.items():
        if value == maxVal:
            return key

#This methof cannot handle single character word test case but can handle special character
def mostCommonWord1(paragraph, banned):
    paragraphList = (''.join([x for x in paragraph if x.isalpha() or x == ' '])).split()
    #paragraphList = paragraph.split()
    paragraphList = [word.lower() for word in paragraphList if word.lower() not in banned]
    elementDictCount = Counter(paragraphList)
    maxVal = max(elementDictCount.values())
    for key,value in elementDictCount.items():
        if value == maxVal:
            return key