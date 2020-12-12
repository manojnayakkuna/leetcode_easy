# -*- coding: utf-8 -*-
"""
Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.
A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.
Return the number of good triplets.
Example 1:
Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4
Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
Example 2:
Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
Output: 0
Explanation: No triplet satisfies all conditions.
"""
#Time Complexity: O(N*N*N)
def countGoodTriplets(arr, a, b, c):
    count=0 
    for i in range(0,len(arr)-2):
        for j in range (i+1,len(arr)-1):
            if(abs(arr[i]-arr[j]) <=a):
                for k in range (j+1,len(arr)):
                    if(abs(arr[j] - arr[k]) <= b and abs(arr[i]-arr[k]) <= c):
                            count += 1
    return count

def countGoodTriplets1(arr,a,b,c):
    i = 0
    j = 1
    k = 2
    res = 0
    while True:
        val1 = Abs(arr[i] - arr[j])
        val2 = Abs(arr[j] - arr[k])
        val3 = Abs(arr[i] - arr[k])
        if val1 <= a and val2 <= b and val3 <= c:
            res += 1
        if i == len(arr)-3:
            break
        k += 1
        if k == len(arr):
            j += 1
            k = j + 1
        if j == len(arr)-1:
            i += 1
            j = i + 1
            k = j + 1
    return res

def Abs(v):
    if v < 0:
        return -v
    return v

print(countGoodTriplets1([3,0,1,1,9,7],7,2,3))