# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:25:42 2020

@author: manoj
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def printLinkedList(node):
    print ('Linked List:',end=' ')
    while node is not None:
        print (node.val, end=' ')
        node = node.next
    print ()

def oddEvenLinkedList(llist):
    head = llist
    prevNode = None
    currNode = llist
    end = llist
    
    while end is not None:
        end = end.next
    
    cnt = 1
    while currNode is not None:
        if cnt % 2 == 0:
            prevNode.next = currNode.next
            end.next = currNode
            end = end.next
        currNode = currNode.next
        prevNode = currNode
    
    return head

def oddEvenLinkedListUsingNewNodes(node):    
    cnt = 1
    while node is not None:
        if cnt % 2 == 0:
            

firstNode5 = ListNode(5)
firstNode4 = ListNode(4,firstNode5)
firstNode3 = ListNode(3,firstNode4)
firstNode2 = ListNode(2,firstNode3)
firstNode1 = ListNode(1,firstNode2)
printLinkedList(firstNode1)

result = oddEvenLinkedList(firstNode1)
printLinkedList(result)