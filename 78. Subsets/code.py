class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        subList = self.subsets(nums[:-1])
        t = nums[-1]
        totalList = []
        for v in subList:
            totalList.append(v + [t])
        totalList.extend(subList)
        return totalList