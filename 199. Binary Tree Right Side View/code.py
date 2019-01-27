# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        view = []
        pre = [root]
        while pre:
            view.append(pre[-1].val)            
            now = []
            for node in pre:
                if node.left:
                    now.append(node.left)
                if node.right:
                    now.append(node.right)
            pre = now
        return view