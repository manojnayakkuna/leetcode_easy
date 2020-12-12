# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 02:17:26 2020

@author: manoj
"""

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

def pathSum(root,sumVal,compareVal):
    if not root:
        return
    
    
    

btTree = None
btTree = TreeNode(5)
btTree.left = TreeNode(4)
btTree.left.left = TreeNode(11)
btTree.left.left.left = TreeNode(7)
btTree.left.left.right = TreeNode(2)
btTree.right = TreeNode(8)
btTree.right.left = TreeNode(13)
btTree.right.right = TreeNode(4)
btTree.right.right.right = TreeNode(1)

printLst = []
printLst = inOrderTraversal(btTree,printLst)
print ('Inorder Binary Tree:',printLst)

lst1 = pathSum(btTree)
print ('levelOrderTraversal:', lst1)