# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# 返回:
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        res, path = [], []

        def f(node: TreeNode, cur: int):
            path.append(node.val)

            if node.left is None and node.right is None:
                if sum == cur + node.val:
                    res.append(path.copy())
                    del path[-1]
                    return

            if node.left is not None:
                f(node.left, cur + node.val)

            if node.right is not None:
                f(node.right, cur + node.val)

            del path[-1]

        if root is None:
            return []

        f(root, 0)
        return res


node1 = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(8)
node4 = TreeNode(11)
node5 = TreeNode(13)
node6 = TreeNode(4)
node7 = TreeNode(7)
node8 = TreeNode(2)
node9 = TreeNode(5)
node10 = TreeNode(1)

node1.left = node2
node1.right = node3
node2.left = node4
node3.left = node5
node3.right = node6
node4.left = node7
node4.right = node8
node6.left = node9
node6.right = node10

s = Solution()
print(s.pathSum(node1, 22))
