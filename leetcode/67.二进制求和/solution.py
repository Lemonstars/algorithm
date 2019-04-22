# 给定两个二进制字符串，返回他们的和（用二进制表示）。
# 输入为非空字符串且只包含数字 1 和 0。
#
# 示例 1:
# 输入: a = "11", b = "1"
# 输出: "100"
#
# 示例 2:
# 输入: a = "1010", b = "1011"
# 输出: "10101"


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        len1 = len(a)
        len2 = len(b)
        i = 0

        carry = 0
        while i < len1 and i < len2:
            num = int(a[len1-1-i]) + int(b[len2-1-i]) + carry
            if num > 1:
                num -= 2
                carry = 1
            else:
                carry = 0

            res += str(num)
            i += 1

        while i < len1:
            num = int(a[len1-1-i]) + carry
            if num > 1:
                num -= 2
                carry = 1
            else:
                carry = 0

            res += str(num)
            i += 1

        while i < len2:
            num = int(b[len2-1-i]) + carry
            if num > 1:
                num -= 2
                carry = 1
            else:
                carry = 0

            res += str(num)
            i += 1

        if carry:
            res += '1'

        return res[::-1]


s = Solution()
print(s.addBinary('1010', '1011'))
