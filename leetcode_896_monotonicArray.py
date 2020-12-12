# -*- coding: utf-8 -*-
"""
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
Return true if and only if the given array A is monotonic.
Example 1:
Input: [1,2,2,3]
Output: true
Example 2:
Input: [6,5,4,4]
Output: true
"""
#Using increase and decrease indicator, fails when values are equal.
def isMonotonic(A):    
    decreaseInd = 'N'
    increaseInd = 'N'
    if A[0] > A[1]:
        decreaseInd = 'Y'
    else:
        increaseInd = 'Y'
    for i in range(1,len(A)-1):
        if A[i+1] >= A[i]:
            increaseInd = 'Y'
        else:
            decreaseInd = 'Y'
    
    if increaseInd=='Y' and decreaseInd =='Y':
        return False
    else:
        return True

#Using sorted function
def isMonotonic1(A):
    if A == sorted(A) or A == sorted(A, reverse=True):
        return True
    return False

#Using increase/decrease indicator
def isMonotonicUsingInd(A):
    lastType = "N"
    if len(A) == 1 or len(A) == 2:
        return True
    if A[1] > A[0]:
        lastType = "I"
    elif A[1] < A[0]:
        lastType = "D"
        
    for i in range(2,len(A)):
        if A[i] == A[i-1]:
            continue
        elif A[i] > A[i-1] and lastType == "D":
            return False
        elif A[i] < A[i-1] and lastType == "I":
                return False
        if lastType == "N":
            if A[i] > A[i-1]:
                lastType = "I"
            elif A[i] < A[i-1]:
                lastType = "D"
    return True