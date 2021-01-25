# -*- coding: utf-8 -*-
"""
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".
Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.
"""
#Most Optimized - 85%
def findRelativeRanks(nums):
    scores = sorted([(score, idx) for idx, score in enumerate(nums)], reverse=True)
    idx_to_rank = {t[1]: rank for rank, t in enumerate(scores)}        
    result = []
    for idx in range(len(nums)):
        rank = idx_to_rank[idx]
        if rank == 0:
            result.append("Gold Medal")
        elif rank == 1:
            result.append("Silver Medal")                
        elif rank == 2:
            result.append("Bronze Medal")
        else:
            result.append(str(rank+1))
    return result
    
# 10%
def findRelativeRanks1(nums):
    dic = {'0':"Gold Medal",'1':'Silver Medal','2':'Bronze Medal'}
    maxThree = sorted(nums, reverse=True)
    result = []
    for val in nums:
        if str(maxThree.index(val)) in dic:
            result.append(dic[str(maxThree.index(val))])
        else:
            result.append(str(maxThree.index(val)+1))
    return result

# 6%
def findRelativeRanks2(nums):
    maxThree = sorted(nums, reverse=True)
    result = []
    for val in nums:
        if maxThree.index(val) == 0:
            result.append('Gold Medal')
        elif maxThree.index(val) == 1:
            result.append('Silver Medal')
        elif maxThree.index(val) == 2:
            result.append('Bronze Medal')
        else:
            result.append(str(maxThree.index(val)+1))
    return result

