# -*- coding: utf-8 -*-
"""
Created on Tue May 26 00:48:48 2020

@author: manoj
"""

def generateParenthesisUtil(openings , closings , stack , result):
    
    print ('openings:',openings,'closings:',closings,'stack:',stack,'result:',result)
    
    if openings == 0 and closings == 0:
        result.append("".join(stack))
        return
    
    if closings < openings or (openings < 0 or closings < 0):
        return
    
    stack.append('(')
    generateParenthesisUtil(openings-1,closings,stack,result)
    stack.pop()
    
    if openings < closings:
        stack.append(')')
        generateParenthesisUtil(openings,closings-1,stack,result)
        stack.pop()
        
def generateParenthesis(n):
    result = []
    generateParenthesisUtil(n,n,[],result)
    return result

def generateParenthesisRecursive(n):
    result = []
    helper(0,0,n,'',result)
    return result
    
def helper(openlen,closelen,size,string,result):
    if openlen == size and closelen == size:
    #if len(string) == 2*size:
        #print ('openlen:', openlen, 'closelen:',closelen,'string:', string)
        result.append(string)
        return
        #return string
    if openlen < size:
        #string = string+"("
        #print ('inside openlen string:', string)
        helper(openlen+1,closelen,size,string+'(',result)
    if closelen < openlen:
        #string = string+")"
        #print ('inside closelen string:', string)
        helper(openlen,closelen+1,size,string+')',result)

import collections
def generateParenthesisIterative(n):
    queue = collections.deque([('',n,n)])
    print ('queue:',queue)
    while True:
        curr_str, left, right = queue.popleft()
        print ('curr_str:', curr_str,'left:',left,'right:',right)
        if left == 0 and right == 0:
            print ('inside return queue:', queue, 'curr_str:',curr_str)
            return [itm[0] for itm in queue] + [curr_str]
        if left>0:
            print ('inside left queue:', queue, 'curr_str:',curr_str)
            queue.append((curr_str+'(',left-1,right))
        if right > left:
            print ('inside right queue:', queue, 'curr_str:',curr_str)
            queue.append((curr_str+')',left,right-1))

#print (generateParenthesis(3))
print (generateParenthesisRecursive(2))
print (generateParenthesisIterative(2))