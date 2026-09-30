# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(root:Optional[TreeNode]) -> int:
            if not root:
                return 0
            else:
                total = max(depth(root.left),depth(root.right))
                return 1 + total
        if not root:
            return True
        elif not -1 <= depth(root.left) - depth(root.right) <= 1:
            print(depth(root.left), depth(root.right))
            return False
        else: 
            return self.isBalanced(root.left) and self.isBalanced(root.right)