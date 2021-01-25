# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 01:56:49 2020

@author: manoj
"""

# To know if the node is balanced or not return the depth for that node, while returning up.
# To know if the node is at what depth not return the depth for that node, while going down.

class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
        
def inOrderTraversal(node,returnList):
    if node:
        inOrderTraversal(node.left,returnList)
        returnList.append(node.val)
        inOrderTraversal(node.right,returnList)

def preOrderTraversal(node,returnList):
    if node:
        returnList.append(node.val)
        preOrderTraversal(node.left,returnList)
        preOrderTraversal(node.right,returnList)

def isCousins(root, x, y):
    xreturnVals = [0,None]
    findDepth(root,x,0,None,xreturnVals)
    print ('xreturnVals:', xreturnVals)
    yreturnVals = [0,None]
    findDepth(root,y,0,None,yreturnVals)
    print ('yreturnVals:', yreturnVals)
    
    if xreturnVals[0] == yreturnVals[0] and xreturnVals[1] != yreturnVals[1]:
        return True
    else:
        return False
    
def findDepth(node,val,depth,parent,returnVals):
    if not node:
        return
    elif node.val == val:
        returnVals[0] = depth
        returnVals[1] = parent
    
    findDepth(node.left,val,depth+1,node,returnVals)
    findDepth(node.right,val,depth+1,node,returnVals)
    
#Internet Method 1: Iteratively
class Solution1:
    def isCousins_Method1(self, root: TreeNode, x: int, y: int) -> bool:
        d = deque([(root, None)])
        while d:
            foundOne, foundParent = None, None
            for i in range(len(d)):
                node, currentParent = d.popleft()
                if foundOne and (node.val == x or node.val == y) and foundParent != currentParent:
                    return True
                if node.val == x or node.val == y:
                    foundOne, foundParent = True, currentParent
                if node.left:
                    d.append((node.left, node))
                if node.right:
                    d.append((node.right, node))
			# early exit optimization. If you find one value and the second value is not present at this level. 
            if foundOne: 
                return False
        return False

#Internet Method 2: Recursion
class Solution2: 
    def isCousins_Method2(self, root, x, y):
        def dept(node, d, par):
            if not node: return 
			# if we find node with value x, then keep its depth and parent in a and aparent variables
            if node.val == x:
                self.a = d
                self.aparent= par
			# if we find node with value y, then keep its depth and parent in b and bparent variables
            elif node.val == y:
                self.b = d
                self.bparent= par
            dept(node.left, d+1, node)
            dept(node.right, d+1, node)
        dept(root, 0, None)
        # return True if a and b are equal and their parents are not same
        return self.a == self.b and self.aparent != self.bparent
    
    
btTree = None
btTree = TreeNode(1)
btTree.left = TreeNode(2)
btTree.right = TreeNode(3)
btTree.left.left = TreeNode(4)

printLst = []
preOrderTraversal(btTree,printLst)
#print ('preorder printLst:', printLst)

printLst = []
inOrderTraversal(btTree,printLst)
print ('inorder printLst:', printLst)

print (isCousins(btTree,4,3))
print (isCousins(btTree,2,3))

