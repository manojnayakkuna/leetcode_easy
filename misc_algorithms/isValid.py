# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:58:21 2020

@author: manoj
"""

def isValid(s):
    openBracketQueue = []
    openSquareQueue = []
    openCurlyQueue = []
    
    for i in range(len(s)):
        print ('len(s):', len(s),'i:',i,'s[i]:',s[i])
        print ('openBracketQueue:', openBracketQueue)
        print ('openSquareQueue:', openSquareQueue)
        print ('openCurlyQueue:', openCurlyQueue)
        if s[i] == '(':
            openBracketQueue.append(i)
        elif s[i] == ')':
            if len(openBracketQueue) > 0:
                if len(openSquareQueue) > 0 or len(openCurlyQueue) > 0:
                    return False
                openBracketQueue.pop()
            else:
                return False

        if s[i] == '[':
            openSquareQueue.append(i)
        elif s[i] == ']':
            if len(openSquareQueue) > 0:
                if len(openBracketQueue) > 0 or len(openCurlyQueue) > 0:
                    return False
                openSquareQueue.pop()
            else:
                return False
        
        if s[i] == '{':
            openCurlyQueue.append(i)
        elif s[i] == '}':
            if len(openCurlyQueue) > 0:
                if len(openBracketQueue) > 0 or len(openSquareQueue) > 0:
                    return False
                openCurlyQueue.pop()
            else:
                return False
            
    if len(openBracketQueue) == 0 and len(openSquareQueue) == 0 and len(openCurlyQueue) == 0:
        return True
    else:
        return False

def isValidSingleStack(s):
    stack = [] 
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            stack.append(s[i])
        elif s[i] == ')':
            if len(stack) > 0:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            else:
                return False
        elif s[i] == ']':
            if len(stack) > 0:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            else:
                return False
        elif s[i] == '}':
            if len(stack) > 0:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            else:
                return False            
    
    if len(stack) == 0:
        return True
    else:
        return False
        
s = '()'
s = "()[]{}"
s ="(]"
s = "([)]"
s = "{[]}"
s = "(])"
s = "[])"
print (isValidSingleStack(s))

