# -*- coding: utf-8 -*-
"""
Created on Fri May 22 00:17:59 2020

@author: manoj
"""

# headlessLinkedList:  
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        try:
            node.val = node.next.val # Assign Current Node value of next node as we need to override the values
            node.next = node.next.next
        except:
            return
        
        #node.val, node.next = node.next.val, node.next.next

head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)
sol = Solution()
sol.deleteNode(head.next)