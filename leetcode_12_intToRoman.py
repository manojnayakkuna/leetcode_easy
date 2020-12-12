# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 01:13:10 2020

@author: manoj
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        
        #sym = {1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        sym = [("M",1000),("CM",900),("D",500),("CD",400),("C",100),("XC",90),("L",50),("XL",1000),("X",10),("IX",9),("V",5),("IV",4),("I",1)]
        
        romanStr = ''
        
        for roman, value in sym:
            while num >= value:
                romanStr = romanStr + roman
                num = num - value
        return romanStr
    
#Using Divisor
class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [1000, 500, 100, 50, 10, 5, 1 ]
        roms = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        ans = ''
        i=0
        
        while num>0:
            divisor = nums[i]
            while num != num%divisor:
                ans += roms[i]*(num//divisor)  
                num %= divisor
                
            if (divisor == 5 or divisor == 10) and num>= divisor-1:
                ans += 'I'+roms[i]
                num -= divisor-1
            elif (divisor == 50 or divisor == 100) and num>= divisor-10:
                ans += 'X'+roms[i]
                num -= divisor -10
            elif (divisor == 500 or divisor == 1000) and num>= divisor-100:
                ans += 'C'+roms[i]
                num -= divisor - 100
            
        
            i+=1
            
        return ans