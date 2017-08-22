# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.mySubtree(s, t, True)

    def mySubtree(self, s, t, root):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        if s.val != t.val:
            if root:
                return self.mySubtree(s.left, t, True) or self.mySubtree(s.right, t, True)
            else:
                return False
        else:
            if self.mySubtree(s.left, t.left, False) and self.mySubtree(s.right, t.right, False):
                return True
            else:
                return self.mySubtree(s.left, t, True) or self.mySubtree(s.right, t, True)