# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        results = []
        to_delete = set(to_delete)
        
        def backtrack(parent, node, deleted = False):
            # print(node.val, results)
            if not node: # None
                return
            print(node.val, deleted)
            
            if node.val in to_delete:
                if parent is not None:
                    parent.left = None if node==parent.left else parent.left
                    parent.right = None if node==parent.right else parent.right
                
                print("DEL", node.val)
                print("left-d")
                backtrack(node, node.left, True)
                print("right-d")
                backtrack(node, node.right, True)
                return
            
            elif deleted:
                # print(node.val, node)
                results.append(node)
            print("NOT DEL", node.val)
            print("left-nd")
            backtrack(node, node.left)
            print("right-nd")
            backtrack(node, node.right)
        
        backtrack(None, root, True)
        
        print(results)
        return results
        
        