class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        t = 0
        for i in xrange(n-1):
            if nums[i] > nums[i+1]:
                if i-1 < 0 or i+2 > n-1:
                    t += 1
                elif nums[i-1] <= nums[i+1]:
                    t += 1
                elif nums[i+2] >= nums[i]:
                    t += 1
                else:
                    return False

        return True if t <= 1 else False        
