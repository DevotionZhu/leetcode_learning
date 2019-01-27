class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k < 0:
            return
        n = len(nums)
        k = k%n

        tmp = nums[n-k:]
        i = n-k
        while i:
            nums[i-1+k] = nums[i-1]
            i -= 1
        for i in xrange(k):
            nums[i] = tmp[i]