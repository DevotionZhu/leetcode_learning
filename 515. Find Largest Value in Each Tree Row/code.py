# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        current = []
        res = []
        if root:
            current.append(root)
        while current:
            child = []
            num = -2147483648
            for node in current:
                if num < node.val:
                    num = node.val
                if node.left:
                    child.append(node.left)
                if node.right:
                    child.append(node.right)
            res.append(num)
            current = child
        return res