# -*- coding: utf-8 -*-
"""
Created on Fri May 29 00:26:29 2020

@author: manoj
"""
import math
def binaryAdd(a,b):
    
    lenA = len(a) - 1
    lenB = len(b) - 1
    carry = 0
    stack = []
    
    while lenA >= 0 or lenB >= 0:
        print ('loop')
        valueA = a[lenA] if lenA >=0 else "0"
        valueB = b[lenB] if lenB >=0 else "0"
        if valueB == "1" and valueA == "1":
            if carry == 0:
                stack.append("0")
                carry = 1
            else:
                stack.append("1")
                #carry = 1
        elif (valueB == "1" and valueA == "0") or (valueB == "0" and valueA == "1"):
            if carry == 1:
                stack.append("0")
                carry = 1
            else:
                stack.append("1")
                carry = 0
        elif valueB == "0" and valueA == "0":
            if carry == 0:
                stack.append("0")
            else:
                stack.append("1")
            carry = 0
        
        lenA -= 1
        lenB -= 1
    print ('stack:',stack, 'carry:',carry)    
    if carry == 1:
        stack.append("1")
    
    return ''.join(stack[::-1])

a = "11"
b = "1"

print ('result:',binaryAdd(a,b))

print (int(math.sqrt(8)))
print ('*********************')
x = 20
n=len(str(x))//2
print ('n:',n)
ans=0
while n>=0:
    while (ans+10**n)**2 <= x:
        print ('(ans+10**n)**2:',(ans+10**n)**2,'   x:', x)
        print ('10**n:',10**n, 'n:',n)
        print ('bef ans:', ans)
        ans+=10**n
        print ('aft ans:', ans)
    n-=1
print ('ans:',ans)