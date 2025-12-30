# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()


        q.append([root, 0])
        count = 1
        while q:
            l = len(q)
            
            for i in range(l):
                node, current = q.popleft()

                if node.left:
                    q.append([node.left, current *2 + 1])
                    count += 1
                if node.right:
                    q.append([node.right,current *2 + 2])
                    count += 1
            # if count < pow(2, level) and q:
            #     return False
            if current >= count:
                return False

        return True