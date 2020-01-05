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

    def __init__(self):
        self.board = None
        self.visit = None

    def find(self, x: int, y: int, res: List):
        self.visit[x][y] = True
        item = self.board[x][y]
        if item == 'X':
            return False

        n, m = len(self.visit), len(self.visit[0])
        res.append((x, y))
        is_board = x == 0 or x == (n - 1) or y == 0 or y == (m - 1)
        if x - 1 >= 0 and not self.visit[x - 1][y]:
            is_board = self.find(x - 1, y, res) or is_board

        if x + 1 < n and not self.visit[x + 1][y]:
            is_board = self.find(x + 1, y, res) or is_board

        if y - 1 >= 0 and not self.visit[x][y - 1]:
            is_board = self.find(x, y - 1, res) or is_board

        if y + 1 < m and not self.visit[x][y + 1]:
            is_board = self.find(x, y + 1, res) or is_board

        return is_board

    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        if n == 0:
            return

        m = len(board[0])
        self.board = board
        self.visit = visit = [[False for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if not visit[i][j]:
                    area = list()
                    isB = self.find(i, j, area)
                    if not isB:
                        for item in area:
                            board[item[0]][item[1]] = 'X'


s = Solution()
# data = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]
# data = [["O"]]
data = [["O", "O", "O", "O", "X", "X"], ["O", "O", "O", "O", "O", "O"], ["O", "X", "O", "X", "O", "O"],
        ["O", "X", "O", "O", "X", "O"], ["O", "X", "O", "X", "O", "O"], ["O", "X", "O", "O", "O", "O"]]
s.solve(data)
print(data)
