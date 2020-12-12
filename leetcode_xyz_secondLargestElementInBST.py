# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 21:17:56 2020

@author: manoj
"""

class bstNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def insertBST(root,val):
    if root is None:
        root = bstNode(val)
    elif val < root.val:
        root.left = insertBST(root.left, val)
    elif val > root.val:
        root.right = insertBST(root.right, val)
    
    return root

def inOrderTraversal(root,returnList):
    if root:
        inOrderTraversal(root.left,returnList)
        returnList.append(root.val)
        inOrderTraversal(root.right,returnList)

def secondLargerstElementBST(root, prevRoot = None):
    if prevRoot is None:
        if root.right is None:
            if root.left is not None:
                return root.left.val
            else:
                return False
    else:
        if root.right is None:
            if root.left is not None:
                return root.left
            else:
                print ('second largest using recursion:', prevRoot.val)
                return prevRoot
            
    secondLargerstElementBST(root.right, root)
    

arr = [10,5,2,1,3,7,6,9,20,15,25]
root = None
for num in arr:
    root = insertBST(root, num)

#Brute Force Method
returnList = []
inOrderTraversal(root,returnList)
print ('Second Largest Element In BST:', returnList[-2])

#Recursion Method
prevRoot = None
secondLargerstElementBST(root, prevRoot)
        