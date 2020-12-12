# -*- coding: utf-8 -*-
"""
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
"""

# To know if the node is balanced or not return the depth for that node, while returning up (bottom-up approach)
# To know if the node is at what depth return the depth for that node, while going down (top down approach)

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

# 1D List
def levelOrderTraversal(node,lst):
    d = deque()
    d.append(node)
    while d:
        tempNode = d.popleft()
        lst.append(tempNode.val)
        if tempNode.left is not None:
            d.append(tempNode.left)
        if tempNode.right is not None:
            d.append(tempNode.right)
    return lst

#2D List
def levelOrderTraversal2D(node):
    d = deque()
    lst = []
    if node is None:
        return lst
    d.append(node)
    while d:
        innerList = []
        innerQueue = []
        for nodes in d:        #capture all values
            innerList.append(nodes.val)
        for nodes in d:        #capture all nodes
            if nodes.left is not None:
                innerQueue.append(nodes.left)
            if nodes.right is not None:
                innerQueue.append(nodes.right)
        if len(innerList) > 0:          #add the innerList values to outer return final List
            lst.append(innerList)
        d = innerQueue  #add newly build queues
    return lst[::-1]

def isBalancedBST(node):
    if not node:
        return 0
    #ldepth = isBalancedBST(node.left) + 1
    #rdepth = isBalancedBST(node.right) + 1
    ldepth = isBalancedBST(node.left)
    rdepth = isBalancedBST(node.right)
    if ldepth == -1 or rdepth == -1:
        return -1
    elif abs(ldepth - rdepth) > 1:
        return -1
    else:
        #return max(ldepth,rdepth)
        return max(ldepth,rdepth) + 1

#Internet Method 1:
class Solution:
    def isBalanced1(self, root: TreeNode) -> bool:
        def depth(root: TreeNode) -> int:
            if not root:
                return 0
            ldepth = depth(root.left)
            rdepth = depth(root.right)
            if ldepth == -1 or rdepth == -1 or abs(ldepth - rdepth) > 1:
                return -1
            return max(ldepth, rdepth) + 1

        return depth(root) != -1

#Internet Method 2: Recursive Vs Iteratuve
class Solution2:
    def isBalanced2(self, root: TreeNode) -> bool:
        '''
        # Recursive
        def dfs(cur):
            if not cur: return True, 0
            ret_l, ret_r = dfs(cur.left), dfs(cur.right)
            return ret_l[0] and ret_r[0] and (abs(ret_l[1]-ret_r[1])<=1), max(ret_l[1], ret_r[1])+1
        return dfs(root)[0]
        '''
        # Non-recursive
        ret = []
        stack, cur = [], ((root, []), ret)
        while cur[0][0] or stack:
            while cur[0][0]:
                stack.append(cur)
                if cur[0][0].left: 
                    cur = ((cur[0][0].left, []), cur[0][1])
                else: 
                    cur = ((cur[0][0].right, []), cur[0][1])
            (node, state), p_state = stack.pop()
            
            ret_l = state[:2] if state else (True, 0)
            ret_r = state[2:] if len(state) > 2 else (True, 0)
            ret_state = (ret_l[0] and ret_r[0] and (abs(ret_l[1]-ret_r[1])<=1), max(ret_l[1], ret_r[1])+1)
            p_state.extend(ret_state)
            if stack and stack[-1][0][0].left == node:
                cur = ((stack[-1][0][0].right, []), stack[-1][0][1])
            else:
                cur = ((None, None), None)    
        return ret[0] if ret else True
    
btTree = None
btTree = TreeNode(3)
btTree.left = TreeNode(9)
btTree.right = TreeNode(20)
btTree.right.left = TreeNode(15)
btTree.right.right = TreeNode(7)

printLst = []
inOrderTraversal(btTree,printLst)
print ('Inorder Binary Tree:',printLst)

items = [9,3,15,20,7]
bstTree = None
for item in items:
    bstTree = insertNodeBST(bstTree,item)
    
printLst = []
inOrderTraversal(bstTree,printLst)
print ('Inorder Binary Search Tree:',printLst)

if isBalancedBST(btTree) != -1:
    print ('True')
else:
    print ('False')
    
lst = []
levelOrderTraversal(btTree,lst)
print ('levelOrderTraversal:', lst)

lst1 = levelOrderTraversal2D(btTree)
print ('levelOrderTraversal:', lst1)
