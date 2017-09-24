# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        res = []
        parent = []
        if root:
            parent.append(root)

        while True:
            tmp = []
            child = []
            flag = True
            for node in parent:
                if node is None:
                    tmp.append("")
                else:
                    tmp.append(str(node.val))
                tmp.append("")

                if node:
                    flag = False
                    if node.left:
                        child.append(node.left)
                    else:
                        child.append(None)

                    if node.right:
                        child.append(node.right)
                    else:
                        child.append(None)
                else:
                    child.append(None)
                    child.append(None)
            if flag:
                break

            n = len(res)
            for i in range(n):
                t = []
                for v in res[i]:
                    t.append("")
                    t.append(v)
                t.append("")
                res[i] = t
            res.append(tmp[:-1])

            parent = child

        return res