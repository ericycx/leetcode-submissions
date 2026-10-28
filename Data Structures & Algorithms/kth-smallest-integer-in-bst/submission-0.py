# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(root):
            res = []
            if not root:
                return res
            left = helper(root.left)
            left.append(root.val)
            right = helper(root.right)
            left.extend(right)
            return left
        in_order = helper(root)
        return in_order[k-1]