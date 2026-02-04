# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []

        start = root
        d = start
        while root:
            if root.left:
                if root.right:
                    stack.append(root.right)
                root.right = root.left
                root.left = None
                root = root.right
            elif root.right:
                root.left = None
                root = root.right 
            else:
                if stack:
                    root.right = stack.pop()
                    
                    
                root.left = None
                root = root.right
        return start