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
        bound = [n-1, n-1, 0, 1]
        direction = 0
        i, j = 0, 0
        for m in range(1, n*n+1):
            res[i][j] = m

            if direction == 0:
                if j == bound[0]:
                    direction = 1
                    bound[0] -= 1
                    i += 1
                else:
                    j += 1
            elif direction == 1:
                if i == bound[1]:
                    direction = 2
                    bound[1] -= 1
                    j -= 1
                else:
                    i += 1
            elif direction == 2:
                if j == bound[2]:
                    direction = 3
                    bound[2] += 1
                    i -= 1
                else:
                    j -= 1
            else:
                if i == bound[3]:
                    direction = 0
                    bound[3] += 1
                    j += 1
                else:
                    i -= 1

        return res


s = Solution()
print(s.generateMatrix(3))
