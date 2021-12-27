from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def DFS(node):
            nonlocal diameter
            if not node:
                return 0
            left_length = DFS(node.left)
            right_length = DFS(node.right)
            
            diameter = max(diameter, left_length + right_length)
            
            return max(left_length, right_length)+1
        
        DFS(root)
        
        return diameter
