# #coding=utf-8
# # 本题为考试单行多行输入输出规范示例，无需提交，不计分。
# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))
# 本题为考试多行输入输出规范示例，无需提交，不计分。

import sys
import copy


if __name__ == "__main__":
    matrix = list()
    for line in sys.stdin:
        values = list(map(int, line.split()))
        matrix.append(values)

    n = len(matrix)
    m = len(matrix[0])

    def check(r, c):
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 1:
                    return False
        return True

    def can_continue(r, c):
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 2:
                    if i - 1 >= 0 and matrix[i - 1][j] == 1:
                        return True

                    if i + 1 < r and matrix[i + 1][j] == 1:
                        return True

                    if j - 1 >= 0 and matrix[i][j - 1] == 1:
                        return True

                    if j + 1 < c and matrix[i][j + 1] == 1:
                        return True
        return False

    num = 0
    while can_continue(n, m):
        matrix_copy = copy.deepcopy(matrix)

        for i in range(n):
            for j in range(m):
                if matrix_copy[i][j] == 2:
                    if i - 1 >= 0 and matrix_copy[i - 1][j] == 1:
                        matrix[i-1][j] = 2

                    if i + 1 < n and matrix_copy[i + 1][j] == 1:
                        matrix[i+1][j] = 2

                    if j - 1 >= 0 and matrix_copy[i][j - 1] == 1:
                        matrix[i][j-1] = 2

                    if j + 1 < m and matrix_copy[i][j + 1] == 1:
                        matrix[i][j+1] = 2

        num += 1

    if check(n, m):
        print(num)
    else:
        print(-1)





