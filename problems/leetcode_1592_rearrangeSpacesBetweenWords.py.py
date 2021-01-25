# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 13:50:50 2020

@author: manoj
"""

"""
You are given a string text of words that are placed among some number of spaces. Each word consists of one or more lowercase English letters and are separated by at least one space. It's guaranteed that text contains at least one word.
Rearrange the spaces so that there is an equal number of spaces between every pair of adjacent words and that number is maximized. If you cannot redistribute all the spaces equally, place the extra spaces at the end, meaning the returned string should be the same length as text.
Return the string after rearranging the spaces.

Example 1:
Input: text = "  this   is  a sentence "
Output: "this   is   a   sentence"
Explanation: There are a total of 9 spaces and 4 words. We can evenly divide the 9 spaces between the words: 9 / (4-1) = 3 spaces.
"""

def reorderSpaces(self, text: str) -> str:
    
    numOfSpaces = text.count(' ')
    if numOfSpaces <= 0:
        return text
    
    list1 = list(text.split())
    if len(list1) <= 1:
        return list1[0]+' '*numOfSpaces
    
    if numOfSpaces % (len(list1)-1) == 0:
        spacePerWord = numOfSpaces // (len(list1)-1)
        endSpace = 0
    else:
        spacePerWord = numOfSpaces // (len(list1)-1)
        endSpace = numOfSpaces % (len(list1)-1)
    
    string = ''
    for i in range(len(list1)):
        if i == len(list1) - 1:
            string += list1[i]
        else:
            string += list1[i] + ' '*spacePerWord
    
    string += ' '*endSpace
    
    return string

def reorderSpacesOptimized(self, text: str) -> str:
	s = text.count(' ')
	t = text.split() 
	return t[0]+' '*s if len(t) == 1 or s == 0 else (' '*(s//(len(t)-1))).join(t)+(' '*(s%(len(t)-1)))