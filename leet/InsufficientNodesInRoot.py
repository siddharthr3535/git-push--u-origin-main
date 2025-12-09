
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def solve(root, current, limit):
            if root.left == None and root.right == None:
                if current + root.val < limit:
                    # print("saab")
                    return False
                return True
            current += root.val
            left = False
            right = False
            
            if root.left:
                left = solve(root.left, current, limit)
            if root.right:
                right = solve(root.right, current, limit)

            if left is False:
                root.left = None
            if right is False:
                root.right = None
            

            return left or right
        
        result = solve(root, 0, limit)
        if result == False:
            return None
        return root
