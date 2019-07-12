# 根据一棵树的中序遍历与后序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
# 返回如下的二叉树：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def divide(in_lo: int, in_hi: int, post_lo: int, post_hi: int) -> TreeNode or None:
            if post_lo > post_hi:
                return None

            if post_lo == post_hi:
                return TreeNode(postorder[post_lo])

            root_val = postorder[post_hi]
            root_node = TreeNode(root_val)

            inorder_idx = inorder.index(root_val, in_lo, in_hi + 1)
            left_node = divide(in_lo, inorder_idx - 1, post_lo, post_hi - in_hi + inorder_idx - 1)
            right_node = divide(inorder_idx + 1, in_hi, post_hi - in_hi + inorder_idx, post_hi - 1)

            root_node.left = left_node
            root_node.right = right_node
            return root_node

        return divide(0, len(inorder) - 1, 0, len(postorder) - 1)


s = Solution()
tree = s.buildTree([2, 1], [2, 1])
print(tree)