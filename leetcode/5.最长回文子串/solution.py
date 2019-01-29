# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# #
# # 示例 1：
# # 输入: "babad"
# # 输出: "bab"
# # 注意: "aba" 也是一个有效答案。
# #
# # 示例 2：
# # 输入: "cbbd"
# # 输出: "bb"


class Solution:
    def longestPalindrome(self, s):
        length = len(s)
        res_start = 0
        res_end = 0

        for i in range(length):
            odd_len = self.lenOfPalindrome(s, i, i)
            even_len = self.lenOfPalindrome(s, i, i+1)
            current_len = max(odd_len, even_len)
            if current_len > res_end - res_start + 1:
                res_start = i - (current_len-1)//2
                res_end = i + current_len//2

        return s[res_start: res_end+1]

    def lenOfPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1


s = Solution()
print(s.longestPalindrome('babad'))
