# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
#
# 示例:
#
# 输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
from typing import List


class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:

        def add(cur: List[int], start_pos: int):
            if len(cur) == k:
                res.append(cur.copy())
                return

            for j in range(start_pos, n - (k - len(cur)) + 2):
                add(cur + [j], j + 1)

        res = []
        add([], 1)
        return res


s = Solution()
print(s.combine(4, 2))