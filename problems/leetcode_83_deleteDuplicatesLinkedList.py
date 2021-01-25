# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 10:37:40 2020

@author: manoj
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def deleteDuplicates(self):
        currNode = self.head
        
        while (currNode != None):
            if currNode.val == currNode.next.val:
                currNode.next = currNode.next.next
            currNode = currNode.next
    
    def deleteDuplicatesInternet(self):
        currNode = self.head
        prevNode = self.head
        
        while (currNode != None):
            if currNode.val != prevNode.val:
                prevNode.next = currNode
                prevNode = currNode
            currNode = currNode.next
        prevNode.next = None
        
        return self.head
            
    def printLinkedList(self):
        print ('Linked List Value:',end='')
        printNode = self.head
        while (printNode):
            print (printNode.val,end=' ')
            printNode = printNode.next
        print ()

node1 = LinkedList()
node1.head = Node(1)

node2 = Node(1)
node1.head.next = node2

node3 = Node(2)
node2.next = node3

node4 = Node(3)
node3.next = node4

node5 = Node(3)
node4.next = node5

node6 = Node(4)

node1.printLinkedList()
#node1.deleteDuplicates()
node1.deleteDuplicatesInternet()
node1.printLinkedList()

