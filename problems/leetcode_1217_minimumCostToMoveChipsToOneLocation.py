# -*- coding: utf-8 -*-
"""
We have n chips, where the position of the ith chip is position[i].
We need to move all the chips to the same position. In one step, we can change the position of the ith chip from position[i] to:
position[i] + 2 or position[i] - 2 with cost = 0.
position[i] + 1 or position[i] - 1 with cost = 1.
Return the minimum cost needed to move all the chips to the same position.
Example 1:
Input: position = [1,2,3]
Output: 1
Explanation: First step: Move the chip at position 3 to position 1 with cost = 0.
Second step: Move the chip at position 2 to position 1 with cost = 1.
Total cost is 1.
Example 2:
Input: position = [2,2,2,3,3]
Output: 2
Explanation: We can move the two chips at position  3 to position 2. Each move has cost = 1. The total cost = 2.
Example 3:
Input: position = [1,1000000000]
Output: 1
"""

"""
Explanation: Collect every odd number on position 1 and every even number on position 2, 
Then find which length is lower than the other, in order to lower the cost.
(Since moving 1 position needs cost of 1.)
"""
def minCostToMoveChips(position):
    #captureAllOddChipsInPosition1 = [val for val in position if val%2 == 1]
    #captureAllEvenChipsInPosition1 = [val for val in position if val%2 == 0]
    
    #captureAllOddChipsInPosition1 = len([val for val in position if val%2 == 1])
    #captureAllEvenChipsInPosition2 = len(position) - captureAllOddChipsInPosition1
    #return min(captureAllOddChipsInPosition1, captureAllEvenChipsInPosition2)

    lenOfOddMoves = len([val for val in position if val%2 == 1])
    return min(lenOfOddMoves, len(position)-lenOfOddMoves)