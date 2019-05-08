# 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
#
# 示例:
# 输入:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# 输出: 6
from typing import List


class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        n = len(heights)
        max_area = 0
        stack = list()

        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                top = stack.pop()
                this_area = heights[top] * (i - stack[-1] - 1 if stack else i)

                if this_area > max_area:
                    max_area = this_area

            stack.append(i)

        return max_area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0

        n, m = len(matrix), len(matrix[0])
        heights = [0 for _ in range(m)]
        res = 0

        for i in range(n):
            for j in range(m):
                heights[j] = heights[i] + 1 if matrix[i][j] == '1' else 0

            res = max(res, self.largestRectangleArea(heights))

        return res


s = Solution()
print(s.maximalRectangle([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
                          ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
