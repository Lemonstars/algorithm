# 给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
# 例如，从根到叶子节点路径 1->2->3 代表数字 123。
#
# 计算从根到叶子节点生成的所有数字之和。
# 说明: 叶子节点是指没有子节点的节点。
#

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def sumNumbers(self, root: TreeNode) -> int:
        return self.fun(root, 0)

    def fun(self, root: TreeNode, num: int) -> int:
        if not root:
            return 0

        if (not root.left) and (not root.right):
            return num * 10 + root.val

        return self.fun(root.left, num * 10 + root.val) + self.fun(root.right, num * 10 + root.val)
