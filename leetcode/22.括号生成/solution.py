# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


class Solution:
    def __init__(self):
        self.res = list()

    def generateParenthesis(self, n):
        self.trace('', 0, 0, n)
        return self.res

    def trace(self, s, open, close, max):
        if len(s) == max * 2:
            self.res.append(s)
            return

        if open < max:
            self.trace(s + '(', open + 1, close, max)

        if close < open:
            self.trace(s + ')', open, close + 1, max)


solution = Solution()
m = solution.generateParenthesis(4)
print(m)
