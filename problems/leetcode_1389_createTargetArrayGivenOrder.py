# -*- coding: utf-8 -*-
"""
Given two arrays of integers nums and index. Your task is to create target array under the following rules:
Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array. It is guaranteed that the insertion operations will be valid.
Example 1: Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]
"""
#Using zip method as the len(index) == len(nums) - 6%
def createTargetArray(nums, index):
    target = []
    for x,y in zip(nums,index):
        target.insert(y,x)
    return target

#Using List - 34%
def createTargetArray1(nums, index):
    target = []
    for i in range(len(index)):
        if i == 0:
            target.append(nums[i])
        else:
            target.insert(index[i], nums[i])
    return target

#Using While - 44%
def createTargetArray2(nums, index):
    target = []
    i = 0
    while i < len(index):
        target.insert(index[i], nums[i])
        i += 1
    return target

#If index array does not start from 0 and starts from random value other than 0th index
def createTargetArray3(nums, index):
    result = []
    n= len(nums)
    for i in range(n):
        if i==0 and index[0]==0:
            result.append(nums[0])
        elif i==0 and index[0]>0:
            result = [0]*index[0]
            result[index[0]]=nums[0]
        else:   
            result=result[:index[i]]+[nums[i]]+result[index[i]:]    
    return result

#Using Linked List
class Solution: 
    def createTargetArray(self, nums, index):
        head = Node(nums[0])  # We always start at nums[0].
        ll = LL(head)  # Initialise our linked list.
        for i in range(1, len(index)):  # We set our head node already. Skip.
            ll.insert(nums[i], index[i])  # Very simple insertion!
        return ll.toArray()  # Only non-standard linked list operation.

class Node:  # Separate classes for neatness.
    def __init__(self, val=None, ref=None):
        self.val = val
        self.ref = ref  # I dislike stepping on Python's "next" keyword.

class LL:
    def __init__(self, head=Node()):
        self.head = head
        
    def insert(self, val, pos):
        if pos == 0:
            new_node = Node(val, self.head)
            self.head = new_node
            return
        curr = self.head
        while curr and pos-1:
            curr = curr.ref
            pos -= 1
        new_node = Node(val, curr.ref)
        curr.ref = new_node
        
    def toArray(self):
        arr = []
        curr = self.head
        while curr:
            arr.append(curr.val)
            curr = curr.ref
        return arr