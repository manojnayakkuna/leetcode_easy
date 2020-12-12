# -*- coding: utf-8 -*-
"""
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].
Note: If a tree has more than one mode, you can return them in any order.
"""

from collections import Counter
def findMode(root):
    treeValues = []
    inOrderTraversal(root, treeValues)
    elementMapValues = Counter(treeValues)
    if len(treeValues) > 0:
        maxVal = max(elementMapValues.values())
        return [key for key,values in elementMapValues.items() if values == maxVal]
    else:
        return treeValues

def inOrderTraversal(root, treeValues):
    if root:
        inOrderTraversal(root.left, treeValues)
        treeValues.append(root.val)
        inOrderTraversal(root.right, treeValues)