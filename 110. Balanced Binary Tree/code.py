# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        lh = self.height(root.left)
        rh = self.height(root.right)
        if abs(lh-rh) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False


    def height(self, node):
        """
        :param node: TreeNode
        :return: bool
        """
        if node is None:
            return 0

        return (max(self.height(node.left), self.height(node.right)) + 1)