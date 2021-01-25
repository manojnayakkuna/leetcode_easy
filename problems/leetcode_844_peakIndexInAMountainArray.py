# -*- coding: utf-8 -*-
"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
"""
# This approach dis not work for 2 test cases. The problem statement does not want to store all '#' in stack
def backspaceCompare(S, T):
    stack_s, stack_t = [], []
    for i in range(len(S)):
        if not stack_s:
            stack_s.append(S[i])
        elif S[i] == '#':
            if stack_s:
                stack_s.pop()
            else:
                stack_s.append(S[i])
        elif stack_s[-1] != '#':
            stack_s.append(S[i])
        else:
            stack_s.pop()
    for i in range(len(T)):
        if not stack_t:
            stack_t.append(T[i])
        elif T[i] == '#':
            if stack_t:
                stack_t.pop()
            else:
                stack_t.append(S[i])
        elif stack_t[-1] != '#':
            stack_t.append(T[i])
        else:
            stack_t.pop()
    return stack_s == stack_t

#Using stack approach, but does not store '#' in stack
def backspaceCompare1(S, T):
    if S is None:
        return False
    if T is None:
        return False
    res=[]
    res1=[]
    for i in S:
        if i!="#":
            res.append(i)
        else:
            if res:
                res.pop()
    for j in T:
        if j!="#":
            res1.append(j)
        else:
            if res1:
                res1.pop()
    print ('res:', res, 'res1:', res1)
    if "".join(res)=="".join(res1):
        return True
    else:
        return False