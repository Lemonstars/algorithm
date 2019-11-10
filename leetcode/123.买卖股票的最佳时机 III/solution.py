# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
# 示例 1:
# 输入: [3,3,5,0,0,3,1,4]
# 输出: 6
# 解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
#      随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
#
# 示例 2:
# 输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。  
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。  
#      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
#
# 示例 3:
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0 or n == 1:
            return 0

        left_max, right_max = [0], [0]
        cur_min_val_left, cur_max_val_right = prices[0], prices[n - 1]
        cur_res_left, cur_res_right = 0, 0

        for i in range(1, n):
            item_left, item_right = prices[i], prices[n - 1 - i]
            cur_res_left = max(cur_res_left, item_left - cur_min_val_left)
            left_max.append(cur_res_left)
            cur_res_right = max(cur_res_right, cur_max_val_right - item_right)
            right_max.append(cur_res_right)
            cur_min_val_left, cur_max_val_right = min(cur_min_val_left, item_left), max(cur_max_val_right, item_right)

        res = left_max[0] + right_max[n - 1]
        for i in range(1, n):
            res = max(res, left_max[i] + right_max[n - 1 - i])

        return res


s = Solution()
# p = [3, 3, 5, 0, 0, 3, 1, 4]
# p = [1, 2, 3, 4, 5]
# p = [7, 6, 4, 3, 1]
p = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
print(s.maxProfit(p))
