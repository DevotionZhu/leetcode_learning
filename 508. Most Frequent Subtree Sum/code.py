# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        table = {}
        sum_class = self.TreeSum(root)

        for v in sum_class:
            if v in table:
                table[v] += 1
            else:
                table[v] = 1
        times = sorted(table.iteritems(), key=lambda x:x[1], reverse=True)
        res = []
        n = len(times)
        if times:
            res.append(times[0][0])
        for i in range(n-1):
            if times[i][1] > times[i+1][1]:
                break
            res.append(times[i+1][0])
        return res


    def TreeSum(self, root):
        if root is None:
            return []
        res = []
        tmp = root.val
        if root.left:
            left = self.TreeSum(root.left)
            res.extend(left)
            tmp += left[0]
        if root.right:
            right = self.TreeSum(root.right)
            res.extend(right)
            tmp += right[0]
        res = [tmp] + res

        return res