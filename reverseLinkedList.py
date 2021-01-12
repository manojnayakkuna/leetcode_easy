# -*- coding: utf-8 -*-
"""
Created on Wed May 20 19:08:43 2020

@author: manoj
"""

class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None
        
class linkedList:
    def __init__(self):
        self.head = None
    
    def printLinkedList(self):
        temp = self.head
        print ('Linked List Value: ', end='')
        while (temp is not None):
            print (temp.data, end=' ')
            temp = temp.next
        print ()
        
    def reverseLinkedList(self):
        prevNode = None
        currNode = self.head
        while currNode is not None:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
            #currNode.next = prevNode
        self.head = prevNode
    
linkedList1 = linkedList()
linkedList1.head = Node(1)
nextNode2 = Node(2)
nextNode3 = Node(3)
nextNode4 = Node(4)
nextNode5 = Node(5)

linkedList1.head.next = nextNode2
nextNode2.next = nextNode3
nextNode3.next = nextNode4
nextNode4.next = nextNode5

print ('Display Newly Created Linked List')
linkedList1.printLinkedList()

print ('Display Reversed Linked List')
linkedList1.reverseLinkedList()
linkedList1.printLinkedList()