# -*- coding: utf-8 -*-
"""
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.
Given the string command, return the Goal Parser's interpretation of command.
Example 1: Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
Example 2: Input: command = "G()()()()(al)"
Output: "Gooooal"
"""
# 75%
def interpret(command):
    string = ''
    i = 0
    while i < len(command):
        if command[i] == 'G':
            string += 'G'
            i += 1
        elif ((i+2) <= len(command)) and (command[i:i+2] == '()'):
            string += 'o'
            i += 2
        elif ((i+4) <= len(command)) and (command[i:i+4] == '(al)'):
            string += 'al'
            i += 4
    return string

#Using dict
def interpret1(s):
        d = {"(al)":"al", "()":"o","G":"G"}
        tmp= ""
        res=""
        for i in range(len(s)):
            c = s[i]
            tmp+=c
            if(tmp in d):
                res+=d[tmp]
                tmp=""
        return res