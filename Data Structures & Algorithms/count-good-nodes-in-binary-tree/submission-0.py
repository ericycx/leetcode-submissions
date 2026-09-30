# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None), get_overloads:
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def f(root, largest):
            if not root:
                return 0
            if root.val >= largest:
                count = 1 + f(root.left, root.val) + f(root.right, root.val)
            else:
                count = f(root.left, largest) + f(root.right, largest)
            return count
        return f(root, root.val)
            





        