# -*- coding: utf-8 -*-
"""
Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.
Example 1: Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2: Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
"""
# Time - 77%
def findComplement(num):
    new_string = ''
    for char in str(bin(num)).split('b')[1]:
        new_string += '0' if char == '1' else '1'
    return int(new_string, 2)

# Time - 75% (Without using defaukt functions)
def findComplement1(num):
    new_string = ''
    for char in decimalToBinary(num):
        new_string += '0' if char == '1' else '1'
    return binaryToDecimal(int(new_string))

def decimalToBinary(decimalVal):
    binaryVal = ''
    while decimalVal:
        lastBit = decimalVal % 2
        decimalVal = decimalVal // 2
        binaryVal = str(lastBit) + binaryVal
    return binaryVal
    
def binaryToDecimal(binaryVal):
    decimalVal = 0
    base = 1
    while binaryVal:
        lastBit = binaryVal % 10
        binaryVal = binaryVal // 10
        decimalVal += lastBit * base
        base = base*2
    return decimalVal