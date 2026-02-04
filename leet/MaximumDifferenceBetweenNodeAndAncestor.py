# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def solve(root, currentmax, currentmin):
            if not root:
                return currentmax - currentmin
            
            currentmax = max(currentmax, root.val)
            currentmin = min(currentmin, root.val)

            left = solve(root.left, currentmax, currentmin)
            right = solve(root.right, currentmax, currentmin)

            return max(left, right)

        return solve(root, root.val, root.val)
        