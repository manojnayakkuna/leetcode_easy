# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 02:01:10 2020

@author: manoj
"""

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def insertBST(root,val):
    if root is None:
        root = TreeNode(val)
    elif val < root.val:
        root.left = insertBST(root.left,val)
    elif val > root.val:
        root.right = insertBST(root.right,val)
    return root
    
def inOrderTraversal(printList,root):
    if root is None:
        return
    inOrderTraversal(printList,root.left)
    printList.append(root.val)
    inOrderTraversal(printList,root.right)

#Using recursion
def minDepthBST(root):
    if root is None:
        return 0
    if not root.left and not root.right:
        return 1
    lmin = 0
    rmin = 0
    if root.left:
        lmin = minDepthBST(root.left) + 1
    if root.right:
        rmin = minDepthBST(root.right) + 1
    if lmin and rmin:
        return min(lmin,rmin)
    else:
        return lmin if lmin else rmin
        #if lmin:
        #    return lmin
        #else:
        #    return rmin

#Using Recursion - Alternate Method
def minDepthBSTAlt(root):
    if not root:
        return 0
    
    l = minDepthBSTAlt(root.left)
    r = minDepthBSTAlt(root.right)
    
    # special case, ensure result not impacted by empty branches
    if l == 0 or r == 0:
        return max(l, r) + 1
    
    return min(l, r) + 1

#Using recursion
def maxDepthBST(root):
    if root is None:
        return 0
    if not root.left and not root.right:
        return 1
    lmax = 0
    rmax = 0
    if root.left:
        lmax = minDepthBST(root.left) + 1
    if root.right:
        rmax = minDepthBST(root.right) + 1
    if lmax and rmax:
        return max(lmax,rmax)
    else:
        if lmax:
            return lmax
        else:
            return rmax

#Using iteratively
def minDepBST(root):
    if not root:
            return 0
    depth = 1
    nodes = [root]
    while True:
        for node in nodes:
            if not node.left and not node.right:
                return depth
        depth += 1
        nodes = [node.left for node in nodes if node.left] \
            + [node.right for node in nodes if node.right]

#Example 1
bstTree = None
treeValues = [10,6,12,4,7,11,13,3,12,15]
for value in treeValues:
    bstTree = insertBST(bstTree,value)
    
printList = []
inOrderTraversal(printList,bstTree)
print ('printList:',printList)
print ('minDepthValue:',minDepthBST(bstTree))

#Example 2
bstTree = None
treeValues = [3,9,20,15,7]
for value in treeValues:
    bstTree = insertBST(bstTree,value)
    
printList = []
inOrderTraversal(printList,bstTree)
print ('printList:',printList)
print ('minDepthValue:',minDepthBST(bstTree))

#Example 3 (binaryTree)
binaryTree = None
binaryTree = TreeNode(3)
binaryTree.left = TreeNode(9)
binaryTree.right = TreeNode(20)
binaryTree.right.left = TreeNode(15)
binaryTree.right.right = TreeNode(7)

printList = []
inOrderTraversal(printList,binaryTree)
print ('printList:',printList)
print ('minDepthValue:',minDepthBST(binaryTree))