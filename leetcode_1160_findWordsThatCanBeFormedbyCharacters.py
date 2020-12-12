# -*- coding: utf-8 -*-
"""
You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars (each character can only be used once).
Return the sum of lengths of all good strings in words.
Example 1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
"""
from collections import Counter
def countCharacters(words, chars):
    elementCharsCount = Counter(chars)
    totLen = 0
    for word in words:
        elementWordCount = Counter(word)
        addWord = 'Y'
        for key, value in elementWordCount.items():
            if key in elementCharsCount and value <= elementCharsCount[key]:
                continue
            else:
                addWord = 'N'
                break
        if addWord == 'Y':
            totLen += len(word)
    return totLen 

#Very Complex using List compression
def countCharacters1(words, chars):
    elementCharsCount = Counter(chars)
    totLen = 0
    for word in words:
        elementWordCount = Counter(word)
        if sum(list(elementWordCount[key] for key in elementWordCount if key in elementCharsCount and elementWordCount[key] <= elementCharsCount[key])) == len(word):
            totLen += len(word)
    return totLen