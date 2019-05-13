# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 说明：解集不能包含重复的子集。
#
# 示例:
# 输入: [1,2,2]
# 输出:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        nums.sort()
        length = len(nums)
        cur = 0
        res = [[]]

        while cur < length:
            k = len(res)

            if cur != length - 1:
                if nums[cur] != nums[cur+1]:
                    for i in range(k):
                        res.append(res[i] + [nums[cur]])
                    cur += 1
                else:
                    cnt = 2
                    while cur + cnt < length and nums[cur + cnt] == nums[cur]:
                        cnt += 1

                    for i in range(k):
                        for j in range(cnt):
                            res.append(res[i] + [nums[cur] for _ in range(j+1)])
                    cur += cnt
            else:
                for i in range(k):
                    res.append(res[i] + [nums[cur]])
                cur += 1

        return res


s = Solution()
print(s.subsetsWithDup([9, 0, 3, 5, 7]))
