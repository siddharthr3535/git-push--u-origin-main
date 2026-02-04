# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        result = 0
        def solve(root, dir, current):
            nonlocal result
            if not root:
                return 
            result = max(result, current)
            if dir == 0:
                solve(root.left, 0, 1)
            else:
                solve(root.left, 0, current + 1)
            
            if dir == 1:
                solve(root.right, 1, 1)
            else:
                solve(root.right, 1, current + 1)
        
       
        
        solve(root,0,0)
        solve(root, 1, 0)
        return result