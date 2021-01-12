# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 13:36:49 2020

@author: manoj
"""

def minCostClimbingStairs(cost):
    if len(cost) <= 2:
        return cost[0]
    
    dp = [0 for _ in range(len(cost))]
    dp[0] = cost[0]
    dp[1] = cost[1]
    
    for i in range(2,len(cost)):
        #dp[i] = min(cost[i]+dp[i-1],cost[i]+dp[i-2])
        dp[i] = cost[i] + min(dp[i-1],dp[i-2])
    
    print ('cost:', cost)
    print ('dp  :',dp)
    
    print ('min(dp[len(cost)-1],dp[len(cost)-2]:',min(dp[len(cost)-1],dp[len(cost)-2]))
    print ('min(dp[len(dp)-1],dp[len(dp)-2]:',min(dp[len(dp)-1],dp[len(dp)-2]))

cost = [10, 15, 20]
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print (minCostClimbingStairs(cost))