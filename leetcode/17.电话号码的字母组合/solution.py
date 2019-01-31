# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
# 示例:
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

class Solution:
    letter = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    def letterCombinations(self, digits):
        length = len(digits)
        if length == 0:
            return []

        res = [i for i in self.letter[int(digits[0]) - 2]]
        if length == 1:
            return res

        for digint in digits[1:]:
            let = self.letter[int(digint) - 2]
            times = len(res)
            for pre_res in res[0: times]:
                for add_letter in let:
                    res.append(pre_res + add_letter)

            while times > 0:
                res.pop(0)
                times -= 1

        return res


s = Solution()
print(s.letterCombinations("234"))
