# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 18:25:44 2020

@author: manoj
"""

"""
Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.
A substring is a contiguous sequence of characters within a string.
Example 1:

Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.
"""
def maxLengthBetweenEqualCharacters(self, s: str) -> int:
    d = {}
    for i in range(len(s)):
        if s[i] in d:
            d[s[i]].append(i)
        else:
            d[s[i]] = [i]
    maxDiff = -1
    for key, value in d.items():
        if len(value) > 1:
            maxDiff = max(maxDiff, (value[-1]-value[0]-1))
    return maxDiff