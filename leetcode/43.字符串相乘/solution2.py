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

        len1 = len(num1)
        len2 = len(num2)
        length = len1 + len2
        digit = [0 for i in range(length)]
        carry = 0

        for j in range(0, len2):
            for i in range(0, len1):
                pre = digit[length-1-i-j]
                cur = int(num1[len1-1-i]) * int(num2[len2-1-j]) + pre + carry
                digit[length-1-i-j] = cur % 10
                carry = cur // 10

                if i == len1-1 and carry != 0:
                    digit[length-2-i-j] = carry
                    carry = 0

        res = ''
        head = True
        for item in digit:
            if head and item != 0:
                head = False
                res += str(item)
                continue

            if head and item == 0:
                continue

            res += str(item)

        return res


s = Solution()
print(s.multiply('999', '999'))
