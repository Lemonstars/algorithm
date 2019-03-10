# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
# 如果不存在最后一个单词，请返回 0 。
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
#
# 示例:
# 输入: "Hello World"
# 输出: 5


class Solution(object):
    def lengthOfLastWord(self, s):
        n = len(s)
        if n == 0:
            return 0

        i = n - 1
        target = ord(' ')
        end_blank = True
        num = 0
        while i >= 0:
            ch = ord(s[i])
            if ch == target:
                if end_blank:
                    i -= 1
                else:
                    break
            else:
                end_blank = False
                num += 1
                i -= 1

        return num
