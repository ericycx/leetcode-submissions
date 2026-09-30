# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        lst = []
        lst.append(root.val)
        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)
        if len(right) >= len(left):
            lst.extend(right)
            return lst
        else:
            n = len(right)
            lst.extend(right)
            lst.extend(left[n:])
            return lst