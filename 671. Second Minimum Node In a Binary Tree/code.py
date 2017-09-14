# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return -1
        if root.left:
            if root.val == root.left.val and root.val == root.right.val:
                if self.findSecondMinimumValue(root.left) == -1 and self.findSecondMinimumValue(root.right) == -1:
                    return -1
                elif self.findSecondMinimumValue(root.left) == -1:
                    return self.findSecondMinimumValue(root.right)
                elif self.findSecondMinimumValue(root.right) == -1:
                    return self.findSecondMinimumValue(root.left)
                else:
                    return min(self.findSecondMinimumValue(root.left), self.findSecondMinimumValue(root.right))
            elif root.val == root.left.val:
                if self.findSecondMinimumValue(root.left) == -1:
                    return root.right.val
                return min(self.findSecondMinimumValue(root.left), root.right.val)
            elif root.val == root.right.val:
                if self.findSecondMinimumValue(root.right) == -1:
                    return root.left.val
                return min(self.findSecondMinimumValue(root.right), root.left.val)
            else:
                return min(root.left.val, root.right.val)
        else:
            return -1
