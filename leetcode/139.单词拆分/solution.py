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
        n = len(s)

        dp = [False for _ in range(n+1)]
        word_set = set()
        for item in wordDict:
            word_set.add(item)
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j: i] in word_set:
                    dp[i] = True
                    break

        return dp[n]


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