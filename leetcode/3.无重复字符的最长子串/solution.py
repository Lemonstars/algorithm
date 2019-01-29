# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

# 示例 1:
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3

# 示例 2:
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1

# 示例 3:
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串

'''
    该解法类似于最长递增子序列的解法
'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0

        length = len(s)
        max_len = [1 for i in range(length)]

        for index in range(1, length):
            pre_len = max_len[index-1]
            current_length = 1
            for j in range(index-1, index-pre_len-1, -1):
                if s[index] != s[j]:
                    current_length += 1
                else:
                    break
            max_len[index] = current_length

        return max(max_len)


s = Solution()
print(s.lengthOfLongestSubstring('au'))
