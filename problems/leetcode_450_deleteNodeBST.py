# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 01:44:36 2020

@author: manoj
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#class Solution:
    #def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
def deleteNode(root,key):
    #Base Case
    if root is None:
        return root
    # If the key to be deleted is smaller than the root's 
    # key then it lies in  left subtree 
    elif key < root.val:
        root.left = deleteNode(root.left,key)
    # If the kye to be delete is greater than the root's key 
    # then it lies in right subtree 
    elif key > root.val:
        root.right = deleteNode(root.left,key)
    # Key is equal to a Node
    elif key == root.val:
        # Node has no child 
        if root.left is None and root.right is None:
            return None
        # Node with only one child in right
        elif root.left is None and root.right is not None:
            root = root.right
        # Node with only one child or in left
        elif root.left is not None and root.right is None:
            root = root.left
        # Node with has both left ad right child
        # locate the lowest value from right node child
        elif root.left is not None and root.right is not None:
            # Node with two children: Get the inorder successor 
            # (smallest in the right subtree) 
            curr = root.right
            while curr.left is not None:
            #while curr is not None:
                curr = curr.left
            
            # Copy the inorder successor's content to this node 
            root.val = curr.val
            
            # Delete the inorder successor 
            root.right = deleteNode(root.right,curr.val)
            
    return root