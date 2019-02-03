# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
# 返回被除数 dividend 除以除数 divisor 得到的商。
#
# 示例 1:
# 输入: dividend = 10, divisor = 3
# 输出: 3
#
# 示例 2:
# 输入: dividend = 7, divisor = -3
# 输出: -2
#
# 说明:
# 被除数和除数均为 32 位有符号整数。
# 除数不为 0。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。


class Solution:
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    def divide(self, dividend, divisor):
        min_int = - pow(2, 31)
        if dividend == min_int and divisor == -1:
            return pow(2, 31) - 1

        negative = False
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            negative = True

        if dividend < 0:
            dividend = - dividend

        if divisor < 0:
            divisor = - divisor

        res = 0
        while True:
            count = 1
            di = divisor
            while dividend >= di:
                di <<= 1
                count <<= 1
            res += count >> 1
            dividend -= di >> 1

            if dividend < divisor:
                break

        return - res if negative else res


s = Solution()
print(s.divide(-10, 3))
