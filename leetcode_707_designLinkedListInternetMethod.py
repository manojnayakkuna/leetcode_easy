# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 01:58:00 2020

@author: manoj
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def get(self,index: int) -> int:
        current = self.head
        if index < self.size:
            for _ in range(index):
                current = current.next
            return current.val
        return -1
    
    def addAtHead(self,val: int) -> None:
        if not self.head:
            self.head = Node(val)
        else:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode
        self.size += 1
    
    def addAtTail(self,val: int) -> None:
        if not self.head:
            self.head = Node(val)
        else:
            current = self.head
            for _ in range(self.size - 1):
                current = current.next 
            current.next = Node(val)
        self.size += 1
    
    def addAtIndex(self,index: int,val: int) -> None:
        if index == self.size:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            if index < self.size:
                current = self.head
                for _ in range(index - 1):
                    current = current.next 
                newNode = Node(val)
                newNode.next = current.next 
                current.next = newNode
                current.next = newNode
                self.size += 1
    def deleteAtIndex(self,index: int) -> None:
        if index < self.size:
            current = self.head
            if index == 0:
                self.head = current.next 
            else:
                for _ in range(index - 1):
                    curent = current.next 
                current.next = current.next.next 
                self.size -= 1