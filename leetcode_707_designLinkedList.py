# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 01:56:38 2020

@author: manoj
"""

class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        
    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        temp = self.head
        count = 0
        while temp is not None:
            if count == index:
                return temp.val
            temp = temp.next
            count = count + 1
        return -1
        
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if not self.head:
            self.head = Node(val)
        else:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode
        #print ('after head:',self.printLinkedList())
        
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if not self.head:
            self.head = Node(val)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            newNode = Node(val)
            temp.next = newNode
        #print ('after tail:',self.printLinkedList())

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        #print ('before addatIndex:',self.printLinkedList())
        if index == 0:
            self.addAtHead(val)
        else:
            temp = self.head
            newNode = Node(val)
            count = 1
            while temp is not None:
                if count == index:
                    newNode.next = temp.next
                    temp.next = newNode
                    break
                temp = temp.next
                count = count + 1
        #print ('after addatIndex:',self.printLinkedList())

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        #print ('before deleteatIndex:',self.printLinkedList())
        if index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            curr = self.head
            totalIndex = 0
            while curr is not None:
                totalIndex += 1
                curr = curr.next
            
            if index < totalIndex:
                count = 0
                while temp is not None:
                    if count == index - 1:
                        temp.next = temp.next.next
                        break
                    temp = temp.next
                    count = count + 1
        #print ('after deleteatIndex:',self.printLinkedList())
    
    def printLinkedList(self):
        temp = self.head
        while temp is not None:
            print (temp.val,end=' ')
            temp = temp.next
        print ()
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)