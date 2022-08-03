# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
#
# 示例 1：
# 输入：root = [1,null,2,3]
# 输出：[1,2,3]
#
# 示例 2：
# 输入：root = []
# 输出：[]
#
# 示例 3：
# 输入：root = [1]
# 输出：[1]
#
# 示例 4：
# 输入：root = [1,2]
# 输出：[1,2]
#
# 示例 5：
# 输入：root = [1,null,2]
# 输出：[1,2]
#
# 提示：
# 树中节点数目在范围 [0, 100] 内
# -100 <= Node.val <= 100


# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def f(self, list: List[int], root: Optional[TreeNode]):
        if not root:
            return

        list.append(root.val)
        self.f(list, root.left)
        self.f(list, root.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.f(res, root)
        return res


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.right = node2
node2.left = node3

solution = Solution()
print(solution.preorderTraversal(node1))