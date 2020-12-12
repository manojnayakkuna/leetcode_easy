# -*- coding: utf-8 -*-
"""
Balanced strings are those who have equal quantity of 'L' and 'R' characters.
Given a balanced string s split it in the maximum amount of balanced strings.
Return the maximum amount of splitted balanced strings.
Example 1: Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2: Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
"""
# Time - 99.90%
def balancedStringSplit(s):
    l,r =0,0
    cnt = 0
    for char in s:
        if char == 'L':
            l += 1
        else:
            r += 1
        if l == r:
            cnt += 1
            l = 0
            r = 0
    return cnt