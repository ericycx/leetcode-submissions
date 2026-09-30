# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        longest_path = self.maxDepth(root.left) + self.maxDepth(root.right)

        return max(longest_path, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        if not root:
            return 0
        count += max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        return count
