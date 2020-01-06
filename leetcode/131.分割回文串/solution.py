# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
# 返回 s 所有可能的分割方案。
#
# 示例:
# 输入: "aab"
# 输出:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

from typing import List
from copy import deepcopy


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def traceback(start: int, end: int, cur: List[str], res: List[List[str]]):
            if start > end:
                res.append(deepcopy(cur))
                return

            for i in range(start, end+1):
                if check(start, i):
                    cur.append(s[start: i + 1])
                    traceback(i+1, end, cur, res)
                    del cur[-1]

        def check(start: int, end: int):
            while start <= end:
                if s[start] != s[end]:
                    return False

                start += 1
                end -= 1
            return True

        global path
        path = list()
        traceback(0, len(s) - 1, [], path)
        return path


data = 'aab'
solution = Solution()
print(solution.partition(data))