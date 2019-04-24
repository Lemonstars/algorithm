# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
#
# 示例 1:
# 输入:
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# 输出:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
#
# 示例 2:
# 输入:
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# 输出:
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
#
# 进阶:
# 一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个常数空间的解决方案吗？


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        first_row_zero = False
        first_col_zero = False

        for i in range(m):
            if matrix[0][i] == 0:
                first_row_zero = True
                break

        for j in range(n):
            if matrix[j][0] == 0:
                first_col_zero = True
                break

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, n):
            if matrix[i][0] == 0:
                for j in range(1, m):
                    matrix[i][j] = 0

        for j in range(1, m):
            if matrix[0][j] == 0:
                for i in range(1, n):
                    matrix[i][j] = 0

        if first_row_zero:
            for i in range(m):
                matrix[0][i] = 0

        if first_col_zero:
            for j in range(n):
                matrix[j][0] = 0



