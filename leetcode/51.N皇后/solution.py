# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#
# 示例:
#
# 输入: 4
# 输出: [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。


class Solution(object):

    def solveNQueens(self, n):
        all_res = list()

        def backtrace(current_res):
            if len(current_res) == n:
                all_res.append(current_res)
                return

            for i in range(n):
                m = len(current_res)

                # check for the column
                if i in current_res:
                    continue

                conflict = False
                # check for the diagonal
                for j in range(m):
                    if abs(m - j) == abs(i - current_res[j]):
                        conflict = True
                        break

                if not conflict:
                    current_res_copy = current_res.copy()
                    current_res_copy.append(i)
                    backtrace(current_res_copy)

        backtrace([])

        ans = list()
        for res in all_res:
            this_ans = list()
            for k in range(n):
                target = res[k]
                this_row = ''
                for j in range(n):
                    this_row += 'Q' if j == target else '.'
                this_ans.append(this_row)
            ans.append(this_ans)
        return ans


s = Solution()
s.solveNQueens(4)




