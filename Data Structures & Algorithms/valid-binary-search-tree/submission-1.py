# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(root, local_min, local_max):
            if not root:
                return True
            if not local_min < root.val < local_max:
                return False
            return helper(root.left, local_min, root.val) and helper(root.right, root.val, local_max)
        return helper(root, -99999999999, 99999999999)