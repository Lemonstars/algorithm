# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
# 两个字符串完全匹配才算匹配成功。
#
# 说明:
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
#
# 示例 1:
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
#
# 示例 2:
# 输入:
# s = "aa"
# p = "*"
# 输出: true
# 解释: '*' 可以匹配任意字符串。
#
# 示例 3:
# 输入:
# s = "cb"
# p = "?a"
# 输出: false
# 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
#
# 示例 4:
# 输入:
# s = "adceb"
# p = "*a*b"
# 输出: true
# 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
#
# 示例 5:
# 输入:
# s = "acdcb"
# p = "a*c?b"
# 输入: false


class Solution:
    def isMatch(self, s, p):
        len1 = len(s)
        len2 = len(p)

        # dp[i][j]代表s[:i-1]和p[:j-1]是否完全匹配
        dp = [[False for _ in range(len2+1)] for _ in range(len1+1)]

        # 当字符串和和模式都为空时，匹配成功
        dp[0][0] = True
        # 当匹配模式为空、字符串长度不为0时，匹配失败
        for i in range(1, len1+1):
            dp[i][0] = False
        # 当字符串为空、模式不为空时
        for j in range(1, len2+1):
            dp[0][j] = dp[0][j-1] and p[j-1] == '*'

        for i in range(1, len2+1):
            for j in range(1, len1+1):
                if p[i-1] != '*':
                    dp[j][i] = dp[j-1][i-1] and (p[i-1] == s[j-1] or p[i-1] == '?')
                else:
                    dp[j][i] = dp[j][i-1] or dp[j-1][i]

        return dp[len1][len2]
