class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        return self.mycount([i+1 for i in range(N)])

    def mycount(self, nums):
        n = len(nums)
        if n == 1:
            return 1
        times = 0
        for i in range(n):
            if nums[i]%n == 0 or n%nums[i] == 0:
                tmp = nums[:i] + nums[i+1:]
                times += self.mycount(tmp)
        return times