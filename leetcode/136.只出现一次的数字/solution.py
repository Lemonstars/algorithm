# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。


from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res ^ i
        return res


input = [4, 2, 1, 4, 1]
s = Solution()
print(s.singleNumber(input))