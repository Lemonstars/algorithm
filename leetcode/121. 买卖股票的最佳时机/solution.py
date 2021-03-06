# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
#
# 注意你不能在买入股票前卖出股票。
#
# 示例 1:
#
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
# 示例 2:
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0

from typing import List


class Solution:

    def divide(self, prices: List[int], lo: int, hi: int):
        if lo >= hi:
            return 0

        mi = (lo + hi) // 2
        low_val, high_val = prices[lo], prices[mi+1]

        for item in prices[lo: mi+1]:
            if item < low_val:
                low_val = item

        for item in prices[mi+1: hi+1]:
            if item > high_val:
                high_val = item

        return high_val - low_val if high_val - low_val > 0 else 0

    def solve(self, prices: List[int], lo: int, hi: int):
        if lo >= hi:
            return 0

        mi = (lo + hi) // 2
        val1 = self.solve(prices, lo, mi)
        val2 = self.solve(prices, mi+1, hi)
        val3 = self.divide(prices, lo, hi)

        return max(val1, val2, val3)

    def maxProfit(self, prices: List[int]) -> int:
        return self.solve(prices, 0, len(prices) - 1)


s = Solution()
data = [2, 1, 2, 1, 0, 1, 2]
print(s.maxProfit(data))