# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
#
# L   C   I   R
# E T O E S I I G
# E   D   H   N
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
#
# 请你实现这个将字符串进行指定行数变换的函数：
#
# string convert(string s, int numRows);
# 示例 1:
# 输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
#
# 示例 2:
# 输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G


class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s

        length = len(s)
        group_num = numRows * 2 - 2
        row_num = min(numRows, length)

        row_list = ['' for i in range(row_num)]
        current_row = 0
        down = False
        for index in range(length):
            row_list[current_row] += s[index]

            inner_index = index % group_num
            if inner_index == 0 or inner_index == numRows-1:
                down = not down
            current_row += 1 if down else -1

        res = ''
        for item in row_list:
            res += item
        return res


s = Solution()
print(s.convert('A', 1))
