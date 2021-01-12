# -*- coding: utf-8 -*-
"""
Created on Mon May 25 16:05:40 2020

@author: manoj
"""

def validParenthesisString(string):
    if len(string) <= 0:
        return False
    
    openStack = []
    starStack = []
    
    for i in range(len(string)):
        print ('string[i]:', string[i])
        if string[i] == '(':
            openStack.append(i)
            print ('append openStack:', openStack)
        elif string[i] == ')':
            if len(openStack) > 0:
                openStack.pop()
                print ('pop openStack:', openStack)    
            else:
                if len(starStack) > 0:
                    starStack.pop()
                    print ('pop starStack:', starStack)
                else:
                    return False
        elif string[i] == '*':
            starStack.append(i)
            print ('append starStack:', starStack)
    
    print ('outside openStack:', openStack, 'starStack:', starStack)
    while len(openStack) > 0:
        print ('inside for loop: i', i)
        if len(starStack) > 0:
            if starStack[-1] > openStack[-1]:
                    starStack.pop()
                    openStack.pop()
            else:
                return False
        else:
            return False
    
    if len(openStack) > 0:
        return False
    else:
        return True

inputStr = "()"
inputStr = "(*)"
inputStr = "(*))"
inputStr = ")*())"
inputStr = "*())"
inputStr = "**())"
inputStr = "*(()*))"
inputStr = ")*()"
inputStr = "(*(**)"
inputStr = "***(()"
inputStr = "(*()"
inputStr = "((()))()(())(*()()())**(())()()()()((*()*))((*()*)"
#inputStr = "()*()(()(*()(((())()()())*))()*()(*)(((*))(())(())((*()*(()(())()*(((*(**))((())*)(((()()))(())()))"
#inputStr = "*()(())*()(()()((()(()()*)(*(())((((((((()*)(()(*)"
print('result 12:', validParenthesisString(inputStr))