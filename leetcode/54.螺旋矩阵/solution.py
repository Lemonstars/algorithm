# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
#
# 示例 1:
#
# 输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
# 示例 2:
#
# 输入:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]


class Solution(object):
    def spiralOrder(self, matrix):
        r = len(matrix)
        if r == 0:
            return []

        c = len(matrix[0])
        if c == 0:
            return []

        num = r * c

        direction = 0
        edge = [c-1, r-1, 0, 1]
        i, j = 0, 0

        res = list()
        while num > 0:
            res.append(matrix[i][j])
            if direction == 0:
                if j == edge[0]:
                    direction = 1
                    edge[0] -= 1
                    i += 1
                else:
                    j += 1
            elif direction == 1:
                if i == edge[1]:
                    direction = 2
                    edge[1] -= 1
                    j -= 1
                else:
                    i += 1
            elif direction == 2:
                if j == edge[2]:
                    direction = 3
                    edge[2] += 1
                    i -= 1
                else:
                    j -= 1
            else:
                if i == edge[3]:
                    direction = 0
                    edge[3] += 1
                    j += 1
                else:
                    i -= 1

            num -= 1

        return res


s = Solution()
print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))

