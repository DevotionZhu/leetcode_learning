class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        i = 0
        longest_num = 1
        tmp_num = 1
        while i < n-1:
            if nums[i] < nums[i+1]:
                tmp_num += 1
            else:
                tmp_num = 1
            if longest_num < tmp_num:
                longest_num = tmp_num
            i += 1
        return longest_num