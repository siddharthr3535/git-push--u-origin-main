# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        def solve(root, currentMax):
            nonlocal result
            if not root:
                return 
            if currentMax <= root.val:
                result += 1
                currentMax = root.val
            solve(root.left, currentMax)
            solve(root.right , currentMax)
        
        solve(root, float('-inf'))
        return result