# -*- coding: utf-8 -*-
"""
Given an integer, return its base 7 string representation.
Example 1: Input: 100
Output: "202"
Example 2: Input: -7
Output: "-10"
"""
# Time - 53% using str
def convertToBase7(num):
    if not num:
        return str(num)
    base7val = ''
    sign = '-' if num < 0 else ''
    num = abs(num)
    while num:
        lastBit = num % 7
        num = num // 7
        base7val = str(lastBit) + base7val
    return sign + base7val

#Time - 15% using list
def convertToBase7_alt(num):
    if not num:
        return str(num)
    base7val = []
    sign = '-' if num < 0 else ''
    num = abs(num)
    while num:
        lastBit = num % 7
        num = num // 7
        base7val.append(str(lastBit))
    base7val.append(sign)
    return ''.join(base7val[::-1])

# Single Liner - 90%
def convertToBase7_alt1(n):
    return["", "-"][n < 0] + str(sum(10 ** d * (abs(n) // 7 ** d % 7) for d in range(9)))

# Single Liner Approach With Description - 81.5%
def convertToBase7_alt2(num):
    targetBase = 7
    inputRangeExponent = 9 # corresponds to input range: -1e7 - 1e7
    runningSum = 0
    tempVal = 0
    for power in range(inputRangeExponent):
        tempVal = abs(num) // (targetBase ** power)
        if tempVal == 0:
            break
        else:
            targetBaseDigit = tempVal % targetBase
            runningSum += (10 ** power) *  targetBaseDigit
    return ["", "-"][num < 0] + str(runningSum)