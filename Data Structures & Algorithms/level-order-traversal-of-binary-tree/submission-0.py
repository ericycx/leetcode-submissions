# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        lst = [[root.val]]
        left_order = self.levelOrder(root.left)
        right_order = self.levelOrder(root.right)
        n = min(len(left_order),len(right_order))
        for i in range(n):
            lst.append(left_order[i] + right_order[i])
        if n == len(left_order):
            lst.extend(right_order[n:])
        if n == len(right_order):
            lst.extend(left_order[n:])
        return lst
