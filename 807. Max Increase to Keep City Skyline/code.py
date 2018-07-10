class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        length = len(grid)
        topBottom = []
        leftRight = []
        for i in range(length):
            topBottom.append(max([row[i] for row in grid]))
            leftRight.append(max(grid[i]))
        increase = 0
        for i in range(length):
            for j in range(length):
                value = min(topBottom[j], leftRight[i])
                if grid[i][j] < value :
                    increase += value - grid[i][j]
        return increase