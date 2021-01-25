# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def listPrimeFactors(num):
    factorsList = []
    divisor = 2
    
    while(divisor <= num):
        if num % divisor == 0:
            factorsList.append(divisor)
            num = num / divisor
        else:
            divisor = divisor + 1
    
    print ('factorsList:', factorsList)
    return factorsList

num1 = 630
result = listPrimeFactors(630)
print ('result', result)
                
            
