# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
# 同一个单元格内的字母不允许被重复使用。
#
# 示例:
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true.
# 给定 word = "SEE", 返回 true.
# 给定 word = "ABCB", 返回 false.
from typing import List


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:

        def traceback(cur_i, cur_j, k):
            if k == len(word):
                return True

            if 0 <= cur_i < n and 0 <= cur_j < m and board[cur_i][cur_j] == word[k]:
                path.append(board[cur_i][cur_j])
                board[cur_i][cur_j] = '-'

                if traceback(cur_i + 1, cur_j, k+1):
                    return True

                if traceback(cur_i - 1, cur_j, k+1):
                    return True

                if traceback(cur_i, cur_j + 1, k+1):
                    return True

                if traceback(cur_i, cur_j - 1, k+1):
                    return True

                board[cur_i][cur_j] = path.pop()

            return False

        n, m = len(board), len(board[0])
        if len(word) > n * m:
            return False

        path = list()
        for i in range(n):
            for j in range(m):
                if traceback(i, j, 0):
                    return True

                path.clear()

        return False


s = Solution()
print(s.exist([["a", "b", "b", "a", "b"], ["a", "a", "b", "b", "a"], ["a", "a", "a", "a", "b"],
               ["a", "a", "a", "b", "a"], ["a", "a", "a", "a", "a"], ["a", "b", "a", "b", "b"],
               ["a", "b", "b", "a", "b"]], 'abbbbaababaa'))
