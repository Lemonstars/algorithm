# 给定n个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为1 。
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
# 给定的高度为[2, 1, 5, 6, 2, 3]。
# 最大矩形面积为10个单位。
#
# 示例:
# 输入: [2, 1, 5, 6, 2, 3]
# 输出: 10
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


s = Solution()
print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
