class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums) + 1
        num_exist = [0]*n
        result = []

        for v in nums:
            if num_exist[v]:
                result.append(v)
            else:
                num_exist[v] = 1

        for i in range(1,n):
            if num_exist[i] == 0:
                result.append(i)
                break
        return result