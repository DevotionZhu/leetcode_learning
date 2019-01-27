class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        multiply_left = [1]
        multiply_right = [1]
        tmp_left = 1
        tmp_right = 1
        for i in xrange(n-1):
            tmp_left *= nums[i]
            multiply_left.append(tmp_left)
            tmp_right *= nums[n-1-i]
            multiply_right.append(tmp_right)

        res = []
        for i in xrange(n):
            res.append(multiply_left[i]*multiply_right[n-i-1])
        return res