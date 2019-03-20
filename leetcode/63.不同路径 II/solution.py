# 一个机器人位于一个 m x n 网格的左上角
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
#
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
# 说明：m 和 n 的值均不超过 100。
#
# 示例 1:
# 输入:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]

        dp[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, n):
            if dp[i-1][0] == 0 or obstacleGrid[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = 1

        for j in range(1, m):
            if dp[0][j-1] == 0 or obstacleGrid[0][j] == 1:
                dp[0][j] = 0
            else:
                dp[0][j] = 1

        for i in range(1, n):
            for j in range(1, m):
                    dp[i][j] = dp[i-1][j] + dp[i][j-1] if obstacleGrid[i][j] == 0 else 0

        return dp[n-1][m-1]


s = Solution()
print(s.uniquePathsWithObstacles([[1, 0]]))