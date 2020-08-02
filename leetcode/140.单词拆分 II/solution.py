# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
#
# 说明：
# 分隔时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
#
# 示例 1：
# 输入:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# 输出:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
#
# 示例 2：
# 输入:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# 输出:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# 解释: 注意你可以重复使用字典中的单词。
#
# 示例 3：
# 输入:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出:
# []

from typing import List


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set()
        for item in wordDict:
            word_set.add(item)
        memory = dict()

        def f(start: int) -> List[str]:
            if start in memory:
                return memory[start]

            res = []
            if start == len(s):
                res.append('')

            for end in range(start + 1, len(s) + 1):
                if s[start: end] in word_set:
                    cur_res = f(end)
                    for m in cur_res:
                        res.append(s[start: end] + ('' if m == '' else ' ') + m)

            memory[start] = res
            return res

        return f(0)


solution = Solution()
s1 = "catsanddog"
wordDict1 = ["cat", "cats", "and", "sand", "dog"]
print(solution.wordBreak(s1, wordDict1))

s2 = "pineapplepenapple"
wordDict2 = ["apple", "pen", "applepen", "pine", "pineapple"]
print(solution.wordBreak(s2, wordDict2))

s3 = "catsandog"
wordDict3 = ["cats", "dog", "sand", "and", "cat"]
print(solution.wordBreak(s3, wordDict3))