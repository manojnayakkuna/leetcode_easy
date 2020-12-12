# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 20:56:02 2020

@author: manoj
"""

class TreeNode:
    def __init__ (self,val=0,left=None,right=None):
        self.val = val
        self.left = None
        self.right = None

def insertBST(root,val):
    if root is None:
        root = TreeNode(val)
    elif val < root.val:
        root.left = insertBST(root.left,val)
    elif  val > root.val:
        root.right = insertBST(root.right,val)
    
    return root

def preOrderTraversal(nums,root):
    if root:
        nums.append(root.val)
        preOrderTraversal(nums,root.left)
        preOrderTraversal(nums,root.right)
    else:
        nums.append('null')
        
def inOrderTraversal(nums,root):
    if root:
        inOrderTraversal(nums,root.left)
        nums.append(root.val)
        inOrderTraversal(nums,root.right)
    else:
        nums.append('null')

#def searchBSTRecursively(self, root: TreeNode, val: int) -> TreeNode:
def searchBSTRecursively(root,val):
    if root is None:
        return None
    elif root.val == val:
        return root
    elif val < root.val:
        return searchBSTRecursively(root.left,val)
    elif val > root.val:
        return searchBSTRecursively(root.right,val)

def searchBSTIteratively(root,val):
    while root != None:
        if root.val == val:
            return root
        elif val < root.val:
            root = root.left
        elif val > root.val:
            root = root.right
    
    return None

treeNode = None
insertList = [49,79,46,41,45]
for item in insertList:
    treeNode = insertBST(treeNode,item)
    
nums = []
inOrderTraversal(nums,treeNode)
print ('nums:',nums)

nums = []
preOrderTraversal(nums,treeNode)
print ('nums:',nums)