class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # k=9, and add no duplicate nums 1-9
        if n > 45 or n < 1:
            return []

        return self.mySum(k, n, [i+1 for i in range(9)])

    def mySum(self, k, n, nums):
        if n < 1 or nums == []:
            return []
        if k == 1:
            if n in nums:
                return [n]

        resTotal = self.mySum(k-1, n-nums[-1],nums[:-1])
        resSub = self.mySum(k,n,nums[:-1])

        resList = []
        for v in resTotal:
            if isinstance(v, int):
                resList.append([v,nums[-1]])
            else:
                resList.append(v[:] + [nums[-1]])
        return resList + resSub