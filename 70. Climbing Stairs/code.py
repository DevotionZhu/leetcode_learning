class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0]*(n+2)
        nums[1] = 1
        nums[2] = 2
        for i in xrange(3,n+1):
            nums[i] = nums[i-1] + nums[i-2]
        return nums[n]