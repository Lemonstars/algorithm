'''
    滑动窗口
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        i = 0
        j = 0
        length = len(s)
        str_dict = dict()
        max_len = 0

        while j < length:
            if s[j] not in str_dict:
                str_dict[s[j]] = j
                j += 1
                max_len = max(max_len, j-i)
            else:
                origin_index = str_dict[s[j]]
                for m in range(i, origin_index+1):
                    str_dict.pop(s[m])
                i = origin_index+1

        return max_len


s = Solution()
print(s.lengthOfLongestSubstring('abba'))
