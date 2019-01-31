# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
# 示例 2:
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
# 说明:
# 所有输入只包含小写字母 a-z 。


class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''

        first_str = strs[0]
        length = len(first_str)

        end = 0
        while end < length:
            same = True
            for str in strs[1:]:
                if end >= len(str) or str[end] != first_str[end]:
                    same = False
                    break

            if same:
                end += 1
            else:
                break

        return first_str[:end]


s = Solution()
print(s.longestCommonPrefix(["aa", "a"]))
