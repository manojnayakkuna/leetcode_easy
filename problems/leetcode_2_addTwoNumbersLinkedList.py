# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 15:55:46 2020

@author: manoj
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverseLL(linkedList):
    prevNode = None
    currNode = linkedList
    nextNode = None
    
    while (currNode is not None):
        nextNode = currNode.next
        currNode.next = prevNode
        prevNode = currNode
        currNode = nextNode
    
    return prevNode

def printLinkedList(node):
    print ('Linked List:',end=' ')
    while node is not None:
        print (node.val, end=' ')
        node = node.next
    print ()
    
def addTwoNumbersLinkedList(l1,l2):
    head = ListNode(0)
    ptr = head
    carry = 0
    
    #l1 = reverseLL(l1)
    printLinkedList(l1)
    #l2 = reverseLL(l2)
    printLinkedList(l2)
    
    while l1 is not None or l2 is not None:
        if l1 is not None:
            addVal1 = l1.val
            l1 = l1.next
        else:
            addVal1 = 0
        
        if l2 is not None:
            addVal2 = l2.val            
            l2 = l2.next
        else:
            addVal2 = 0
        
        print ('addVal1:',addVal1,'addVal2:',addVal2,'carry:',carry)
        sumVal = carry + addVal1 + addVal2
        print ('sumVal:', sumVal)
        
        if sumVal > 9:
            carry = sumVal // 10
            sumVal = sumVal % 10
        else:
            carry = 0
        print ('carry:',carry,'sumVal:',sumVal)
        
        newLL = ListNode(sumVal)
        head.next = newLL
        head = head.next
        
    if carry != 0:
        newLL = ListNode(carry)
        head.next = newLL
        head = head.next
        return ptr.next
    else:
        return ptr.next

firstNode3 = ListNode(3)
firstNode2 = ListNode(4,firstNode3)
firstNode1 = ListNode(2,firstNode2)
printLinkedList(firstNode1)

secondNode1 = ListNode(5)
secondNode2 = ListNode(6)
secondNode1.next = secondNode2
secondNode3 = ListNode(4)
secondNode2.next = secondNode3
printLinkedList(secondNode1)

newNode = addTwoNumbersLinkedList(firstNode1,secondNode1)
printLinkedList(newNode)