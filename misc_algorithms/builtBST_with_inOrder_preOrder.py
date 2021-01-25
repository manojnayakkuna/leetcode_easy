# -*- coding: utf-8 -*-
"""
Created on Fri May 15 10:00:20 2020

@author: manoj
"""

class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
    
def insertNode(root,key):
    if root == None:
        root = Node(key)
    elif key < root.key:
        root.left = insertNode(root.left,key)
    elif key > root.key:
        root.right = insertNode(root.right,key)
    return root

def inOrderTraversal(root,listBST):
    if root:
        inOrderTraversal(root.left,listBST)
        listBST.append(root.key)
        inOrderTraversal(root.right,listBST)
    #return listBST
    
def preOrderTraversal(root,listBST):
    if root:
        listBST.append(root.key)
        preOrderTraversal(root.left,listBST)
        preOrderTraversal(root.right,listBST)
    #return listBST

def postOrderTraversal(root,listBST):
    if root:
        postOrderTraversal(root.left,listBST)
        postOrderTraversal(root.right,listBST)
        listBST.append(root.key)
    return listBST

def readBST(preOrder,inOrder):
    if len(preOrder) <= 0 or len(inOrder) <= 0:
        return None
    
    print ('preorder:', preOrder)
    print ('inOrder:', inOrder)
    
    root = Node(preOrder[0])
    print ('root.key:', root.key)
    
    for i in range(len(inOrder)):
        if root.key == inOrder[i]:
            indexVal = i

    print ('indexVal:', indexVal)
    
    root.left = readBST(preOrder[1:indexVal+1], inOrder[:indexVal])
    root.right = readBST(preOrder[indexVal+1:], inOrder[indexVal+1:])
    
    return root

arr = [9,33,3,5,2,11,45,76,23,56]
bstTree = None
for i in range(len(arr)):
    if i == 0:
        bstTree = insertNode(bstTree,arr[i])
    else:
        insertNode(bstTree,arr[i])

inOrder, preOrder, postOrder = [], [] , []

inOrderTraversal(bstTree,inOrder)
print ('inOrder:',inOrder)
preOrderTraversal(bstTree,preOrder)
print ('preOrder:',preOrder)
postOrderTraversal(bstTree,postOrder)
print ('postOrder:',postOrder)

print ('****************************************************************')
bstTree1 = None
bstTree1 = readBST(preOrder, inOrder)
secondinorderlist = []
inOrderTraversal(bstTree1,secondinorderlist)
print ('Second Time inOrder:',secondinorderlist)

print ('****************************************************************')
inOrder = ['D', 'B', 'E', 'A', 'F', 'C'] 
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
bstTree2 = None
#bstTree2 = readBST(preOrder, inOrder)
secondinorderlist = []
#inOrderTraversal(bstTree2,secondinorderlist)
#print ('Second Time inOrder:',secondinorderlist)