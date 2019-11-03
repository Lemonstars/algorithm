# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 3
# 输出: [1,3,3,1]


from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1, 1]

        pre, cur = [1, 1], []
        curIdx = 2

        while curIdx < rowIndex + 2:
            for i in range(0, curIdx):
                cur.append(1 if i == 0 or i == (curIdx - 1) else (pre[i-1] + pre[i]))

            pre, cur = cur, []
            curIdx += 1

        return pre


s = Solution()
print(s.getRow(3))

