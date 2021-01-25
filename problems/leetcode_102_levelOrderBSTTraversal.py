# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 00:29:44 2020

@author: manoj
"""

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def insertBST(root,val):
    if root == None:
        root = TreeNode(val)
        #print ('value inserted:',val)
    elif val < root.val:
        #print ('value inserted left side:', val)
        insertBST(root.left,val)
    elif val > root.val:
        #print ('value inserted right side:', val)
        insertBST(root.right,val)
    return root

def preOrderTraversal(root):
    if root:
        print (root.val, end=' ')
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)
    return root

#output result = result: [[3], [9, 20], [15, 7]]
def levelOrderBSTTraversal(root):
    queue = []
    result = []
    if root is None:
        return
    queue.append(root)
    while (queue):
        innerResult = []
        innerQueue = []
        for nodes in queue:
            if nodes.left is not None:
                innerQueue.append(nodes.left)
            if nodes.right is not None:
                innerQueue.append(nodes.right)    
        for elements in queue:
            innerResult.append(elements.val)    
        if len(innerResult) > 0:
            result.append(innerResult)        
        queue = innerQueue
        
    return result

# result: result: [3, 9, 20, 15, 7]
def levelOrderBSTTraversalAsList(root):
    queue = []
    if root is None:
        return
    queue.append(root)
    while (queue):
        print (queue[0].val, end=' ')
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)    

def levelOrderBSTTraversalNew(root):
    result = []
    result.append([root.val])
    result.append([root.left.val,root.right.val])
    result.append([root.right.left.val,root.right.right.val])
    
    return result
        
binarysearchTreeNode = None
bTree = [3,9,20,15,7]
for item in bTree:
    binarysearchTreeNode = insertBST(binarysearchTreeNode,item)

#bTree = [3,9,20,15,7]
binaryTreeNode = TreeNode(3)
binaryTreeNode.left = TreeNode(9)
binaryTreeNode.right = TreeNode(20)
binaryTreeNode.right.left = TreeNode(15)
binaryTreeNode.right.right = TreeNode(7)

#print ('binaryTreeNode:',binaryTreeNode)
inOrderTraversal(binaryTreeNode)

print()
#resultAlt = levelOrderBSTTraversalNew(binaryTreeNode)
#print ('resultAlt:',resultAlt)

result = levelOrderBSTTraversal(binaryTreeNode)
print ('result using 2D List:',result)

print ('Using 1D List:',end='')
levelOrderBSTTraversalAsList(binaryTreeNode)
