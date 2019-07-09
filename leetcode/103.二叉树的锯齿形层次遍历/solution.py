# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回锯齿形层次遍历如下：
#
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
#

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        res = []
        cur = [root]
        idx, n = 0, len(cur)
        left2right = True
        while idx < len(cur):
            if idx == n:
                sort_list = list(map(lambda d: d.val, cur[:n]))
                res.append(sort_list if left2right else list(reversed(sort_list)))
                del cur[:n]
                idx, n = 0, len(cur)
                left2right = not left2right

                continue

            node = cur[idx]
            if node.left is not None:
                cur.append(node.left)

            if node.right is not None:
                cur.append(node.right)

            idx += 1

        final_list = list(map(lambda d: d.val, cur))
        res.append(final_list if left2right else list(reversed(final_list)))
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
print(solution.zigzagLevelOrder(n1))