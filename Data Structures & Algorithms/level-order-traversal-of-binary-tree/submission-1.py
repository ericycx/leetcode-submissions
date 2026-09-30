# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root])

        while q:
            qlen = len(q)
            layer = []

            for i in range(qlen):
                node = q.popleft()
                if node:
                    layer.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if layer:
                res.append(layer)
        return res
                

