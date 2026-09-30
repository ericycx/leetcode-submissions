# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None), get_overloads:
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def f(node, largest):
            if not node:
                return 0
            if node.val >= largest:
                count = 1 + f(node.left, node.val) + f(node.right, node.val)
            else:
                count = f(node.left, largest) + f(node.right, largest)
            return count
        return f(root, root.val)
            





        