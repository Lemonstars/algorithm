# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1:
# 输入: 123
# 输出: 321
#
# 示例 2:
# 输入: -123
# 输出: -321
#
# 示例 3:
# 输入: 120
# 输出: 21
#
# 注意:
# 假设我们的环境只能存储得下 32 位的有符号整数，请根据这个假设，如果反转后整数溢出那么就返回 0。


class Solution:
    def reverse(self, x):
        is_positive = True
        if x < 0:
            is_positive = False
            x = -x

        res = 0
        while x != 0:
            remainder = x % 10
            res = res * 10 + remainder
            x = x // 10

        if not is_positive:
            res = -res

        min_int = -pow(2, 31)
        max_int = 0x7fffffff
        if res <= min_int or res > max_int:
            return 0

        return res


s = Solution()
print(s.reverse(321))
