# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
#
# 说明：
#
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 示例 1：
#
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 示例 2：
#
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#      注意你可以重复使用字典中的单词。
# 示例 3：
#
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false


from typing import List


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set()
        for item in wordDict:
            wordSet.add(item)

        length = len(s)

        def backtrace(start) -> bool:
            if start == length:
                return True

            for i in range(start, length):
                if s[start: i+1] in wordSet and backtrace(i+1):
                    return True

            return False

        return backtrace(0)


s1 = "leetcode"
word1 = ["leet", "code"]

s2 = "applepenapple"
word2 = ["apple", "pen"]

s3 = "catsandog"
word3 = ["cats", "dog", "sand", "and", "cat"]

solution = Solution()
print(solution.wordBreak(s1, word1))
print(solution.wordBreak(s2, word2))
print(solution.wordBreak(s3, word3))