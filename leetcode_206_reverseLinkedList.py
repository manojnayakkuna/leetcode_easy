# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 14:50:01 2020

@author: manoj
"""

class LinkedList:
    def __init__(self,val):
        self.val = val
        self.next = None

def reverseLinkedList(head):
    if head is None:
        return -1
    
    prevNode = None
    currNode = head
    nextNode = None
    while currNode is not None:
        nextNode = currNode.next
        currNode.next = prevNode
        prevNode = currNode
        currNode = nextNode
    print ('*******AFT prevNode:',prevNode.val,'currNode:',currNode,'nextNode:',nextNode)
    
    return prevNode

def printLinkedList(head):
    while head is not None:
        print (head.val,end=' ')
        head=head.next

Node1 = LinkedList(1)
Node2 = LinkedList(2)
Node1.next = Node2
Node3 = LinkedList(3)
Node2.next = Node3

printLinkedList(Node1)
Node1 = reverseLinkedList(Node1)
print ()
printLinkedList(Node1)