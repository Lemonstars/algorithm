# 给定一个未排序的整数数组，找出最长连续序列的长度。
# 要求算法的时间复杂度为 O(n)。
#
# 示例:
# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num2res = dict()
        for num in nums:
            if num2res.__contains__(num):
                continue
            else:
                leftNum = 0 if not num2res.__contains__(num-1) else num2res[num-1]
                rightNum = 0 if not num2res.__contains__(num+1) else num2res[num+1]
                num2res[num] = leftNum + rightNum + 1
                num2res[num - leftNum] = num2res[num]
                num2res[num + rightNum] = num2res[num]

                if num2res[num] > res:
                    res = num2res[num]

        return res


data = [100, 4, 200, 1, 3, 2]
solution = Solution()
print(solution.longestConsecutive(data))