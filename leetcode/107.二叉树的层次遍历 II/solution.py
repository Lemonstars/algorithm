# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其自底向上的层次遍历为：
#
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

# Definition for a binary tree node.

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        res = []
        cur = [root]
        idx, n = 0, len(cur)
        while idx < len(cur):
            if idx == n:
                res.insert(0, list(map(lambda d: d.val, cur[:n])))
                del cur[:n]
                idx, n = 0, len(cur)

                continue

            node = cur[idx]
            if node.left is not None:
                cur.append(node.left)

            if node.right is not None:
                cur.append(node.right)

            idx += 1

        res.insert(0, list(map(lambda d: d.val, cur)))
        return res


n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(15)
n5 = TreeNode(7)
n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

solution = Solution()
print(solution.levelOrderBottom(n1))