# -*- coding: utf-8 -*-
"""
Created on Sun May 17 16:42:55 2020

@author: manoj
"""

import collections

def stringAnagram(inputStr, searchStr):
    inLen = len(inputStr)
    searchLen = len(searchStr)
    
    if inLen < searchLen:
        return []
    
    indexList = []
    word_count = collections.Counter()
    for char in searchStr:
        word_count[char] += 1
    
    in_count = collections.Counter()
    for i in range(inLen):
        in_count[inputStr[i]] += 1
        if i >= searchLen:
            #print ('i:',i,'searchLen;',searchLen)
            if in_count[inputStr[i-searchLen]] == 1:
                del in_count[inputStr[i-searchLen]]
            else:
                in_count[inputStr[i-searchLen]] -= 1
        #print ('in_count:', in_count)
        if word_count == in_count:
            indexList.append(i - searchLen + 1)
        
    return indexList

inputStr = "cbaebabacd"
searchStr = 'abc'

print ('result:', stringAnagram(inputStr,searchStr))