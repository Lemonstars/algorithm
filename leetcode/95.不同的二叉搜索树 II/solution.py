# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
#
# 示例:
#
# 输入: 3
# 输出:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# 解释:
# 以上的输出对应以下 5 种不同结构的二叉搜索树：
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
from typing import List
import copy


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def f(tree):
            res = []
            for i in range(len(tree)):
                val = tree[i]
                left_tree, right_tree = f(tree[:i]), f(tree[i+1:])
                for ltree in left_tree or [None]:
                    for rtree in right_tree or [None]:
                        root = TreeNode(val)
                        root.left = ltree
                        root.right = rtree
                        res.append(root)
            return res

        return f([i + 1 for i in range(n)])


s = Solution()
print(len(s.generateTrees(3)))