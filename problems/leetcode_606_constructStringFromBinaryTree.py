# -*- coding: utf-8 -*-
"""
You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.
The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.
Example 1: Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"
Explanation: Originallay it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)".
Example 2: Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 
Output: "1(2()(4))(3)"
Explanation: Almost the same as the first example, 
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#Optmized my approach
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        return self.helper(t)
    
    def helper(self,root):
        ans = ''
        if root is None:
            return ''
        ans = str(root.val)
        if root.left is not None and root.right is not None:
            left = self.helper(root.left)
            right = self.helper(root.right)
            ans += '('+left+')'+'('+right+')'
        elif root.left is not None and root.right is None:
            left = self.helper(root.left)
            ans += '('+left+')'
        elif root.left is None and root.right is not None:
            right = self.helper(root.right)
            ans += '()('+right+')'

        return ans

#Need to understand approach
def tree2str1(self, t: TreeNode) -> str:
    if not t: return ""
    
    left, right = "", ""
    if t.left or t.right:
        left = f"({self.tree2str(t.left)})"
    if t.right:
        right = f"({self.tree2str(t.right)})"
    
    return f"{t.val}{left}{right}"

#Need to understand approach
"""The base case will be when the tree is empty and we return "".If not, we declare a dummy string and pass it to our function.
The function takes a treenode and a string as arguments. If the treenode is not none, we replace the first character of our string with the value of treenode.
Then we check whether both left and right children are present: we recursively call our function with left child and dummy string as parameters and assign it to a variable,
similarly call the function for right child add the results to our string Similarly we check if node has left child only:recursively call the function add the results to our string Similarly we check if the node has right child only: recursively call the function add the results to our string
"""
# Definition for a binary tree node.

def tree2str2(self, t: TreeNode) -> str:
    if not t:
        return ""
    string = "x"
    def some(node, string):
        if node:
            string = string.replace(string[0], str(node.val))
            if node.left and node.right:
                left = some(node.left, "x")
                right = some(node.right, "x")
                string += "({})({})".format(left, right)
            elif node.left:
                temp = some(node.left, "x")
                string += "({})".format(temp)
            elif node.right:
                temp = some(node.right, "x")
                string += "()({})".format(temp)
        return string
    return some(t, string)