# -*- coding: utf-8 -*-
"""
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.
Return the number of consistent strings in the array words.
Example 1: Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2: Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.
Example 3: Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
"""
from collections import Counter

# Time - 75%
def countConsistentStrings(allowed, words):
    count = 0
    for word in words:
        count += 1
        word = set(word)
        for char in word:
            if char not in allowed:
                count -= 1
                break
    return count
    
# Time - 25%
def countConsistentStrings1(allowed, words):
    elementCounterAllowed = Counter(allowed)
    count = 0
    for word in words:
        elementCounterWord = Counter(word)
        add = 'Y'
        for key in elementCounterWord.keys():
            if key in elementCounterAllowed:
                continue
            else:
                add = 'N'
                break
        if add == 'Y':
            count += 1
    return count

# Another variation of approach 2 - 25%
def countConsistentStrings2(allowed, words):
    allowed = set(allowed)
    count = 0
    for word in words:
        add = 'Y'
        word = set(word)
        if len(word) > len(allowed):
            add = 'N'
        else:
            for char in word:
                if char in allowed:
                    continue
                else:
                    add = 'N'
                    break
        if add == 'Y':
            count += 1
    return count