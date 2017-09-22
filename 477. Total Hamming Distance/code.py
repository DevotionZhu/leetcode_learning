class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bit1 = [0] * 32
        for num in nums:
            i = 0
            while num:
                if num & 1:
                    bit1[i] += 1
                num >>= 1
                i += 1
        n = len(nums)
        res = 0
        for v in bit1:
            res += v * (n - v)

        return res
