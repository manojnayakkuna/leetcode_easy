# -*- coding: utf-8 -*-
"""
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.
Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.
Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"
Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"
Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"
"""
#Using dict
def nextGreatestLetter(letters, target):
    charDict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,
                'y':25,'z':26}
    targetVal = charDict[target]
    if targetVal >= charDict[letters[-1]]:
        return letters[0]
    for char in letters:
        if targetVal >= charDict[char]:
            continue
        else:
            return char

#Using ord()
def nextGreatestLetter1(letters, target):
    s = ord(target)
    for i in letters:
        if ord(i) > s:
            return i
    return letters[0]

#Using binary Search
def nextGreatestLetter2(letters, target):
    if target >= letters[-1]:
        return letters[0]
    l = 0
    r = len(letters) - 1        
    while l <= r:
        mid = (l + r) // 2
        if letters[mid] <= target:
            l = mid + 1
        else:
            r = mid - 1        
    return letters[l]