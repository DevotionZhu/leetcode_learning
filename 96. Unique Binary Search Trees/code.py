class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return
        nums = [0]*(n+1)
        nums[0] = 1
        nums[1] = 1
        i = 1
        while i < n:
            for j in range(i+1):
                nums[i+1] += nums[j]*nums[i-j]
            i += 1

        return nums[n]