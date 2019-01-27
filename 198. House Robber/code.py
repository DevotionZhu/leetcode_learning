class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = [0]*(n+1)
        if n >= 1:
            total[1] = nums[0]
        for i in range(2, n+1):
            total[i] = max(total[i-2] + nums[i-1], total[i-1])
        return total[n]