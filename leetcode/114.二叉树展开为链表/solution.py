# 给定一个二叉树，原地将它展开为链表。
#
# 例如，给定二叉树
#
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# 将其展开为：
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:

        def f(node: TreeNode) -> TreeNode:
            if node.left is None and node.right is None:
                return node

            if node.left is None and node.right is not None:
                return f(node.right)

            if node.left is not None and node.right is None:
                final_left_node = f(node.left)
                node.right = node.left
                node.left = None
                return final_left_node

            left = f(node.left)
            right = f(node.right)
            left.right = node.right
            node.right = node.left
            node.left = None
            return right

        if root is None:
            return None

        f(root)


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(5)
node4 = TreeNode(3)
node5 = TreeNode(4)
node6 = TreeNode(6)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6

s = Solution()
s.flatten(node1)
print(node1)























