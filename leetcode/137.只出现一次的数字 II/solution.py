# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。


from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        two, one = 0, 0
        for item in nums:
            one = (one ^ item) & (~two)
            two = (two ^ item) & (~one)
        return one


data = [2, 3, 2, 2]
solution = Solution()
print(solution.singleNumber(data))

