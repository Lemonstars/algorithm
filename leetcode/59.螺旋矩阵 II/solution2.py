# 给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
#
# 示例:
# 输入: 3
# 输出:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(n)] for _ in range(n)]
        i, j = 0, 0
        di, dj = 0, 1
        for m in range(n**2):
            res[i][j] = m + 1
            if res[(i+di) % n][(j+dj) % n] > 0:
                di, dj = dj, -di
            i += di
            j += dj
        return res


s = Solution()
print(s.generateMatrix(3))
