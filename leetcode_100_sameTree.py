# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 00:18:47 2020

@author: manoj
"""
class TreeNode:
    def __init__ (self,val=0,left=None,right=None):
        self.val = val
        self.left = None
        self.right = None

def preOrderTraversal(nums,root):
    if root:
        nums.append(root.val)
        preOrderTraversal(nums,root.left)
        preOrderTraversal(nums,root.right)
    else:
        nums.append('null')
    
def isSameTree(binaryTreeA,binaryTreeB):
    numsA = []
    preOrderTraversal(numsA,binaryTreeA)
    #print ('numsA:', numsA)
    
    numsB = []
    preOrderTraversal(numsB,binaryTreeB)
    #print ('numsB:', numsB)
    
    return numsA == numsB

#recursion
def isSameTreeRecursion(binaryTreeA,binaryTreeB):
    if not binaryTreeA and not binaryTreeB:
        return True
    
    if not binaryTreeA or not binaryTreeB or binaryTreeA.val != binaryTreeB.val:
        return False
    
    return isSameTreeRecursion(binaryTreeA.right, binaryTreeB.right) and isSameTreeRecursion(binaryTreeA.left, binaryTreeB.left)

#iterative
def isSameTreeIterative(p,q):
    stackp, stackq = [p], [q]
    while stackp:
        nodep, nodeq = stackp.pop(), stackq.pop()
        if not nodep and not nodeq:
            continue
        if not nodep or not nodeq or nodep.val != nodeq.val:
            return False
        stackp.append(nodep.left)
        stackq.append(nodeq.left)
        stackp.append(nodep.right)
        stackq.append(nodeq.right)
    return True

#Example 1
binaryTreeA = None
binaryTreeA = TreeNode(1)
binaryTreeA.left = TreeNode(2)
binaryTreeA.right = TreeNode(3)

binaryTreeB = None
binaryTreeB = TreeNode(1)
binaryTreeB.left = TreeNode(2)
binaryTreeB.right = TreeNode(3)

print ('1st Example:',isSameTree(binaryTreeA,binaryTreeB))

#Example 2
binaryTreeA = None
binaryTreeA = TreeNode(1)
binaryTreeA.left = TreeNode(2)

binaryTreeB = None
binaryTreeB = TreeNode(1)
binaryTreeB.right = TreeNode(2)

print ('2nd Example:',isSameTree(binaryTreeA,binaryTreeB))

#Example 3
binaryTreeA = None
binaryTreeA = TreeNode(1)
binaryTreeA.left = TreeNode(2)
binaryTreeA.right = TreeNode(1)

binaryTreeB = None
binaryTreeB = TreeNode(1)
binaryTreeB.left = TreeNode(1)
binaryTreeB.right = TreeNode(2)

print ('3rd Example:',isSameTree(binaryTreeA,binaryTreeB))