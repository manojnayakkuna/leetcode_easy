# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 22:37:16 2020

@author: manoj
"""

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def inOrderTraversal(root):
    if root:
        inOrderTraversal(root.left)
        print(root.val, end=' ')
        inOrderTraversal(root.right)

def inOrderTraversalList(nums,root):
    if root:
        inOrderTraversalList(nums,root.left)
        nums.append(root.val)
        inOrderTraversalList(nums,root.right)

def preOrderTraversal(root):
    if root:
        print(root.val, end=' ')
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)

def postOrderTraversal(root):
    if root:
        postOrderTraversal(root.left)
        postOrderTraversal(root.right)
        print(root.val, end=' ')
    
def insertBST(root,val):
    if root is None:
        root = TreeNode(val)
    elif val < root.val:
        root.left = insertBST(root.left,val)
    elif  val > root.val:
        root.right = insertBST(root.right,val)
    
    return root

def levelOrderTraversal(root):
    if root is None:
        return
    
    queue = []
    result = []
    
    queue.append(root)
    while (queue):
        innerList = []
        for elements in queue:
            innerList.append(elements.val)
        if len(innerList) > 0:
            result.append(innerList)
        innerQueue = []
        for nodes in queue:
            if nodes.left is not None:
                innerQueue.append(nodes.left)
            if nodes.right is not None:
                innerQueue.append(nodes.right)
        queue = innerQueue
    
    return result

#Using Stack
def minDiffInBST(root):
    stack = []
    minimum = float('inf')
    previous = float('inf')
    
    while len(stack) != 0 or root!=None:
        while root != None:
            stack.append(root)
            print ('root val:', root.val)
            root = root.left
            print ('root left:', root)
        if root is None:
            node = stack.pop()
            print('node val:',node.val)
            print ('minimum:',minimum,'node.val:',node.val,'previous:',previous)
            minimum = min(minimum, abs(previous-node.val))
            print ('minimum:',minimum)
            previous = node.val
            print('previous val:',previous)
            root = node.right
            print ('root right:', root)
            
    return minimum

#Using inOrder Traversal
#def minDiffInBSTNew(self, root: TreeNode) -> int:
def minDiffInBSTNew(root):
    nums = []
    inOrderTraversalList(nums, root)
    print ('nums:',nums)
    minn = 1000000
    
    for i in range(len(nums) - 1):
        minn = min(nums[i+1]-nums[i], minn)
    
    return minn

def inorder(nums, root):
    if root is None:
        return
    inorder(nums, root.left)
    nums.append(root.val)
    inorder(nums, root.right)

treeNode = None
insertList = [4,2,6,1,3]
for item in insertList:
    treeNode = insertBST(treeNode,item)

print('inOrder  : ', end='')
inOrderTraversal(treeNode)
print ()
print('preOrder : ', end='')
preOrderTraversal(treeNode)
print ()
print('postOrder: ', end='')
postOrderTraversal(treeNode)

print ()
result = levelOrderTraversal(treeNode)
print('levelOrder: ', result)

print ()
result = minDiffInBST(treeNode)
print('levelOrder: ', result)

print ()
result = minDiffInBSTNew(treeNode)
print('levelOrder: ', result)