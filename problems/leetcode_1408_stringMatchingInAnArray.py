# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 01:04:42 2020

@author: manoj
"""
"""
Given an array of string words. Return all strings in words which is substring of another word in any order. 
String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].
Example 1:
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.
"""
def stringMatching(words):
    result = []
    for i in range(len(words)):
        for j in range(len(words)):
            if (i != j) and (len(words[i])<=len(words[j])) and (words[i] in words[j]) and words[i] not in result:
                result.append(words[i])
                break
    return result