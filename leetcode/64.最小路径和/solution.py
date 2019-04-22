# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 说明：每次只能向下或者向右移动一步。
#
# 示例:
# 输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        cost = [[0 for _ in range(n)] for _ in range(m)]

        cost[0][0] = grid[0][0]
        for i in range(1, m):
            cost[i][0] = cost[i-1][0] + grid[i][0]

        for j in range(1, n):
            cost[0][j] = cost[0][j-1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                cost[i][j] = min(cost[i-1][j], cost[i][j-1]) + grid[i][j]

        return cost[m-1][n-1]


s = Solution()
print(s.minPathSum([[1, 2, 5], [3, 2, 1]]))
