from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
          1(3)
         /     \
        2(2)   3(1)
       /    \
      4(1)   5(1) 
      
      nodeHeight = max(leftHeight,rightHeight) + 1
      
      mapping ={height: [node1, node2,..]}
        """
        self.mapping = defaultdict(list)
        self.dfs(root)
        
        return self.mapping.values()
    def dfs(self,root):
        if root == None:
            return 0
        else:
            leftHeight = self.dfs(root.left)
            rightHeight = self.dfs(root.right)
            nodeHeight = max(leftHeight,rightHeight) + 1
            
            self.mapping[nodeHeight].append(root.val)
            return nodeHeight

Solution().findLeaves([1,2,3,4,5])