# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Dynamic Programming - 1 (Using For Loop)
def climStairsUsingForDP(n):
    a,b = 1,1
    for _ in range(n):
        a,b = b,a+b
    return a

#Dynamic Programming - 2 (Using Recursive)
def climStairsUsingRecursiveDP(n):
    if n == 0 or n == 1:
        return 1
    
    return climStairsUsingRecursiveDP(n-1) + climStairsUsingRecursiveDP(n-2)

#Dynamic Programming - 3 (Using O(n) Space - Memonizing List)
def climStairsUsingMemonizingListDP(n):
    List = [0 for _ in range(n+1)]
    List[0] = 1
    List[1] = 1
    
    for i in range(2,n+1):
        List[i] = List[i-1] + List[i-2]
    
    return List[n]

#Dynamic Programming - 3 (Using O(n) Space - Memonizing Dict)
def climStairsUsingMemonizingDictDP(n):
    pass
    
#For Steps = [1,2]
print('climStairsUsingForDP',climStairsUsingForDP(4))
print('climStairsUsingRecursiveDP:',climStairsUsingRecursiveDP(4))
print('climStairsUsingMemonizingListDP:',climStairsUsingMemonizingListDP(4))

#If Steps = [1,2,3]
