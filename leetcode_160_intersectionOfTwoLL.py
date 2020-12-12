# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 01:19:55 2020

@author: manoj
"""
"""
Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:
begin to intersect at node c1.
Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
"""

#Method using List
def getIntersectionNode(headA, headB):
    L1,L2 = 0,0
    temp = headA
    while temp:
        L1 += 1
        temp = temp.next
    temp = headB
    while temp:
        L2 += 1
        temp = temp.next
    
    if L1>L2:
        headA,headB = headB,headA
        L1,L2 = L2,L1
    for _ in range(L2-L1):
        headB = headB.next
    while headA:
        if headA == headB: return headB
        headA = headA.next
        headB = headB.next
    return None

#Method using set
def getIntersectionNodeSet(headA, headB):
    
    h = set()
    while headA:
        h.add(headA)
        headA = headA.next
    
    while headB:
        if headB in h:
            return headB
        else:
            headB = headB.next
            
    return None

#Method using 2 pointer
def getIntersectionNode(headA, headB):
    tempA, tempB, ptr_exchange = headA, headB, 0
    if tempA == None or tempB == None: 
        return 
    while ptr_exchange < 3:
        if tempA == tempB: 
            return tempA
        if tempA.next != None: 
            tempA = tempA.next
        else: 
            tempA = headB 
            ptr_exchange += 1
        if tempB.next != None: 
            tempB = tempB.next
        else: 
            tempB = headA
            ptr_exchange += 1