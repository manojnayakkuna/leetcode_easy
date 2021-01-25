# -*- coding: utf-8 -*-
"""
Created on Thu May 21 00:22:54 2020

@author: manoj
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
    
    def reverseLinkedList(self):
        prevNode = None
        currNode = self.head
        nextNode = None
        while (currNode is not None):
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        self.head = prevNode
        
    def printLinkedList(self):
        result = []
        tempNode = self.head
        while tempNode is not None:
            result.append(tempNode.data)
            tempNode = tempNode.next
        return result
    
def checkPalindromeInternet(self):
    pass
    
linkList = linkedList()
linkList.head = Node(1)

linkList2 = Node(2)
linkList3 = Node(3)
linkList4 = Node(4)
linkList4A = Node(4)
linkList3A = Node(3)
linkList2A = Node(2)
linkList1A = Node(1)

linkList.head.next = linkList2
linkList2.next = linkList3
linkList3.next = linkList4
linkList4.next = linkList4A
linkList4A.next = linkList3A
linkList3A.next = linkList2A
linkList2A.next = linkList1A

result = linkList.printLinkedList()
linkList.reverseLinkedList()
reverse = linkList.printLinkedList()

if result == reverse:
    print (True)
else:
    print (False)