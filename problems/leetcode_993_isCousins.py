# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 14:41:48 2020

@author: manoj
"""
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
def printTreeNode(root):
    if root:
        printTreeNode(root.left)
        print (root.val)
        printTreeNode(root.right)
    
def isCousins(root, x, y, returnVals):
    parent = root
    depth = 0
    xreturnVals = findNodeParent(root, x, depth, parent, [0,None])
    yreturnVals = findNodeParent(root, y, depth, parent, [0,None])
    
    if xreturnVals[0] == x and yreturnVals[0] == 1 and xreturnVals[1] != yreturnVals[1]:
        return True
    else:
        return False
    
def findNodeParent(root, value, depth, parent, returnVals):
    if root is None:
        return
    if root.val == value:
        returnVals[0] = depth
        returnVals[1] = parent
    findNodeParent(root.left, x, depth+1, root, returnVals)
    findNodeParent(root.right, x, depth+1, root, returnVals)

