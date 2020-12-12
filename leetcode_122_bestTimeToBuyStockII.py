# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 00:34:34 2020

@author: manoj
"""

def maxProfit(prices):
    maxReturnProfit = 0
    
    for i in range(1,len(prices)):
        if prices[i] - prices[i-1] > 0:
            maxReturnProfit = maxReturnProfit + prices[i] - prices[i-1]
        
    return maxReturnProfit

prices = [7,1,5,3,6,4]
print (maxProfit(prices))

prices = [1,2,3,4,5]
print (maxProfit(prices))