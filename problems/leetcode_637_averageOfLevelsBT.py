# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 01:42:50 2020

@author: manoj
"""

from collections import deque

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def insertNodeBST(node,val):
    if node is None:
        node = TreeNode(val)
    elif val < node.val:
        node.left = insertNodeBST(node.left,val)
    elif val > node.val:
        node.right = insertNodeBST(node.right,val)
    
    return node

def inOrderTraversal(node,lst):
    if node:
        inOrderTraversal(node.left,lst)
        lst.append(node.val)
        inOrderTraversal(node.right,lst)

#2D List
def levelOrderTraversal2D(node):
    d = deque()
    lst = []
    if node is None:
        return lst
    
    d.append(node)
    while d:
        innerQueue = []
        #capture all values
        sumVal = 0
        counter = 0
        for nodes in d:
            sumVal = sumVal + nodes.val
            counter = counter + 1
        avgVal = sumVal / counter
        #capture all nodes
        for nodes in d:
            if nodes.left is not None:
                innerQueue.append(nodes.left)
            if nodes.right is not None:
                innerQueue.append(nodes.right)
        #add the innerList values to outer return final List
        lst.append(avgVal)
        #add newly build queues
        d = innerQueue
    
    return lst

btTree = None
btTree = TreeNode(3)
btTree.left = TreeNode(9)
btTree.right = TreeNode(20)
btTree.right.left = TreeNode(15)
btTree.right.right = TreeNode(7)

printLst = []
printLst = inOrderTraversal(btTree,printLst)
print ('Inorder Binary Tree:',printLst)

lst1 = levelOrderTraversal2D(btTree)
print ('levelOrderTraversal:', lst1)