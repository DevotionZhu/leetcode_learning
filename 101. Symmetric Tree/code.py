# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is None or root.right is None:
            return False
        left_todo = [root.left]
        right_todo = [root.right]
        while left_todo != [] or right_todo != []:
            left = left_todo.pop()
            right = right_todo.pop()
            if left.val != right.val:
                return False
            else:
                if left.left and right.right:
                    left_todo.append(left.left)
                    right_todo.append(right.right)
                if (left.left is None and right.right) or (left.left and right.right is None):
                    return False
                if left.right and right.left:
                    left_todo.append(left.right)
                    right_todo.append(right.left)
                if (left.right is None and right.left) or (left.right and right.left is None):
                    return False
        return True