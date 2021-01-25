# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 15:43:47 2020

@author: manoj
"""
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
            
    def printLinkedList(self):
        print ('Linked List Value:',end='')
        printNode = self.head
        while (printNode):
            print (printNode.val,end=' ')
            printNode = printNode.next
        print ()

def mergeTwoLinkedLists(firstLL,secondLL):
    firstLinkList = firstLL.head
    secondLinkList = secondLL.head
    refHead = None
    
    if firstLinkList == None:
        return secondLinkList
    
    if secondLinkList is None:
        firstLinkList
    
    if firstLinkList.val > secondLinkList.val:
        refHead = secondLinkList
    else:
        refHead = firstLinkList
    
    while firstLinkList != None and secondLinkList != None:
        if firstLinkList.val > secondLinkList.val:
            refHead.next = secondLinkList.next
            refHead = refHead.next
            secondLinkList = secondLinkList.next
        elif firstLinkList.val < secondLinkList.val:
            refHead.next = firstLinkList.next
            refHead = refHead.next
            firstLinkList = firstLinkList.next
        else:
            refHead.next = firstLinkList.next
            refHead = refHead.next
            refHead.next = secondLinkList.next
            refHead = refHead.next
    
    while firstLinkList != None:
        refHead.next = firstLinkList.next
        refHead = refHead.next
        firstLinkList = firstLinkList.next
    
    while secondLinkList != None:
        refHead.next = secondLinkList.next
        refHead = refHead.next
        secondLinkList = secondLinkList.next

# Definition for singly-linked list.
# l1: [1,2,4]
# l2: [1,3,4]
# output = [1,2,3,4,4]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoListsInternet(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        ptr = head
    
        while True:            
            if l1 is None and l2 is None:
                break
            elif l1 is None:
                ptr.next = l2
                break
            elif l2 is None:
                ptr.next = l1
                break
            else:
                smallValue = 0
                print ('l1:',l1)
                if l1.val < l2.val:
                    smallValue = l1.val
                    l1 = l1.next
                else:
                    smallValue = l2.val
                    l2 = l2.next

                newNode = ListNode(smallValue)
                ptr.next = newNode
                ptr = ptr.next
        
        #return head            ---- > Output = [0,1,1,2,3,4,4], as we have added 0 in default new LinkedList
        return head.next
    
firstNode1 = LinkedList()
firstNode1.head = Node(1)
firstNode2 = Node(2)
firstNode1.head.next = firstNode2
firstNode3 = Node(4)
firstNode2.next = firstNode3

firstNode1.printLinkedList()

secondNode1 = LinkedList()
secondNode1.head = Node(1)
secondNode2 = Node(3)
secondNode1.head.next = secondNode2
secondNode3 = Node(4)
secondNode2.next = secondNode3

secondNode1.printLinkedList()

refHead = mergeTwoLinkedLists(firstNode1,secondNode1)
refHead.printLinkedList()