# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 说明：解集不能包含重复的子集。
#
# 示例:
# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = list()
        res.append([])

        i = 0
        while i < len(nums):
            k = len(res)
            for j in range(k):
                res.append(res[j] + [nums[i]])
            i += 1

        return res


s = Solution()
print(s.subsets([1, 2, 3]))