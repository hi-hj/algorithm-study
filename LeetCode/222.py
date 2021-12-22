from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = 0
        queue = deque()
        if root:
            queue.append(root)
            count+=1
        
        while queue:
            node = queue.popleft()
            if node.left:
                count+=1
                queue.append(node.left)
            if node.right:
                count+=1
                queue.append(node.right)
        
        return count