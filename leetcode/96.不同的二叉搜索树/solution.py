# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
#
# 示例:
#
# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3


class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 2

        res_dict = {1: 1, 2: 2}
        for j in range(3, n+1):
            num = 2 * res_dict[j - 1]
            for i in range(1, j - 1):
                num += res_dict[i] * res_dict[j - i - 1]
            res_dict[j] = num

        return res_dict[n]


s = Solution()
print(s.numTrees(3))