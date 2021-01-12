# -*- coding: utf-8 -*-
"""
Created on Sat May 23 02:37:38 2020

@author: manoj
"""
import math

def reverseInteger(x):
    
    x = list(str(x).strip('0'))
    print ('x:',x)
    if len(x) == 0:
        return 0
    
    if len(x) == 1:
        return ''.join(x)
        
    addInd = 'N'
    if x[0] == '-':
        addInd = 'Y'
        x = x[1:]
    
    print ('x:', x)
    #j = 0
    #for i in range(len(x)):
    #    if x[i] != '0':
    #        x[j], x[i] = x[i], x[j]
    #        j = j + 1
    #print ('j:',j)
    #x = x[:j]
    x = x[::-1]
    if addInd == 'Y':
        x.insert(0,'-')
    
    x = int(''.join(x))
    print ('math.pow(2,16):', int(math.pow(2,31)))
    if x > (int(math.pow(2,31)) - 1):
        return 0
    if x < -1*int(math.pow(2,31)):
        return 0
    
    return x

x = 123
print ('result 123:', reverseInteger(x))

x = -123
print ('result -123:', reverseInteger(x))

x = 120
print ('result 120:', reverseInteger(x))

x = 0
print ('result 0:', reverseInteger(x))