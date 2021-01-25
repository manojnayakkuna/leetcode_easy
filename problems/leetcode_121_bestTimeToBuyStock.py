# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 02:04:44 2020

@author: manoj
"""

def maxProfit(prices):
    if len(prices) < 2:
        return 0
    
    if len(prices) == 2:
        if prices[0] < prices[1]:
            return prices[1] - prices[0]
        else:
            return 0

    curr_max_profit = 0
    curr_min = float('inf')
    
    for curr_price in prices:
        print ('curr_price:', curr_price)
        print ('bef curr_min:', curr_min)
        print ('bef curr_max_profit:', curr_max_profit)
        curr_min = min(curr_min, curr_price)
        curr_max_profit = max(curr_max_profit, curr_price - curr_min)
        print ('aft curr_min:', curr_min)
        print ('aft curr_max_profit:', curr_max_profit)
    
    return curr_max_profit

print (maxProfit([7,2,15,1,3,6,4]))
#print (maxProfit([7,6,4,3,1]))
#print (maxProfit([6,1]))