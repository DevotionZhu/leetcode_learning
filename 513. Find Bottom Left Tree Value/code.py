# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        current = []
        res = 0

        if root:
            current.append(root)
        while current:
            res = current[0].val
            next = []
            for node in current:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            current = next
        return res