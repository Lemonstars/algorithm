# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
#
# 示例:
# X X X X
# X O O X
# X X O X
# X O X X
# 运行你的函数后，矩阵变为：
#
# X X X X
# X X X X
# X X X X
# X O X X
# 解释:
# 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。
# 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

from typing import List


class Solution:

    def dfs(self, x: int, y: int, board: List[List[str]]):
        if x < 0 or x >= n or y < 0 or y >= m:
            return

        if board[x][y] == 'O':
            board[x][y] = '-'
            self.dfs(x - 1, y, board)
            self.dfs(x + 1, y, board)
            self.dfs(x, y - 1, board)
            self.dfs(x, y + 1, board)

    def solve(self, board: List[List[str]]) -> None:
        global n
        n = len(board)
        if n == 0:
            return

        global m
        m = len(board[0])
        if m == 0:
            return

        for i in range(0, n):
            self.dfs(i, 0, board)
            self.dfs(i, m - 1, board)

        for j in range(1, m - 1):
            self.dfs(0, j, board)
            self.dfs(n - 1, j, board)

        for i in range(n):
            for j in range(m):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


s = Solution()
# data = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]
# data = [["O"]]
data = [["O", "O", "O", "O", "X", "X"], ["O", "O", "O", "O", "O", "O"], ["O", "X", "O", "X", "O", "O"],
        ["O", "X", "O", "O", "X", "O"], ["O", "X", "O", "X", "O", "O"], ["O", "X", "O", "O", "O", "O"]]
s.solve(data)
print(data)
