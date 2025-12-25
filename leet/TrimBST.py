# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, left, right):
        if not root:
            return None
        if root.val< left:
            return self.solve(root.right, left, right)
        if root.val > right:
            return self.solve(root.left, left, right)
        else:
            root.left = self.solve(root.left, left, right)
            root.right = self.solve(root.right, left, right)
            return root
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        return self.solve(root, low, high)
