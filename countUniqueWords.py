# -*- coding: utf-8 -*-
"""
Created on Thu May  7 11:51:32 2020

@author: manoj
"""

import collections

def countUniqueWords(string,num):
    if len(string) <= 0:
        return -1
    
    wordsList = string.split()
    
    word_counts = collections.Counter()
    for word in wordsList:
        word_counts[word] += 1
    
    print ('word_counts:',word_counts, 'len(word_counts):', len(word_counts))
    results = []
    for word in word_counts.most_common(num):
        print ('word:', word)
        results.append(word)
    
    return results

stringInput = """This is my first use of collection Counter function. Collections in python has many features like orderedict, deque, etc. Have used
deque in past and am aware of orderedict but not Counter. This function has few good cool features and I am using one of the feature most_common, which
helps return most common keys in the dict based on value"""

print ('results',countUniqueWords(stringInput, 10))