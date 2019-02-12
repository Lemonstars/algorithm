# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
#
# 示例 1:
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
#
# 示例 2:
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
# 说明：
# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。


class Solution:
    def multiply(self, num1, num2):
        if num1 == '0' or num2 == '0':
            return '0'

        len2 = len(num2)

        res = ''
        carry = '0'
        for j in range(len2-1, -1, -1):
            digit = self.add(self.single_multiply(num1, num2[j]), carry)
            res = digit[-1] + res
            if len(digit) > 1:
                carry = digit[0:len(digit)-1]
            else:
                carry = '0'

        if carry != '0':
            res = carry + res
        return res

    def single_multiply(self, num, ch):
        if ch == '0' or num == '0':
            return '0'

        res = ''
        carry = 0
        for i in range(len(num)-1, -1, -1):
            digit = num[i]
            mul = int(digit) * int(ch) + carry
            res = str(mul % 10) + res
            carry = mul // 10

        if carry != 0:
            res = str(carry) + res
        return res

    def add(self, num1, num2):
        len1 = len(num1)
        len2 = len(num2)
        if len1 < len2:
            less = num1
            more = num2
        else:
            less = num2
            more = num1

        res = ''
        carry = 0
        i = 0
        while i < len(less):
            digit = int(num1[len1 - 1 - i]) + int(num2[len2 - 1 - i]) + carry
            res = str(digit % 10) + res
            carry = digit // 10
            i += 1

        if len1 == len2:
            if carry != 0:
                res = str(carry) + res
            return res

        last = abs(len1-len2)-1
        for i in range(last, -1, -1):
            digit = int(more[i]) + carry
            res = str(digit % 10) + res
            carry = digit // 10

        if carry == 1:
            res = '1' + res

        return res


s = Solution()
print(s.multiply('123', '456'))
