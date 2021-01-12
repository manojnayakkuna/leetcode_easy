# -*- coding: utf-8 -*-
"""
Created on Tue May  5 02:28:06 2020

@author: manoj
"""

# input = 'apple ORANGE banana'
# expected output = 'apple banana ORANGE'

def sortString(inputstr):
    if len(inputstr) <= 0:
        return -1
    
    strList = inputstr.split(' ')
    #strList.sort() : ['ORANGE', 'apple', 'banana']
    #strList.sort(reverse=True) : ['banana', 'apple', 'ORANGE']
    for i in range(len(strList)):
        strList[i] = strList[i].lower() + strList[i]
    strList.sort()
    
    for i in range(len(strList)):
        strList[i] = strList[i][(len(strList[i])//2):]
    
    return strList

str1 = 'apple ORANGE banana'
print (sortString(str1))
    