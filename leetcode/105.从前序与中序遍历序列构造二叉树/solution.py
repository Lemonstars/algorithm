# 根据一棵树的前序遍历与中序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 返回如下的二叉树：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def divide(pre_lo: int, pre_hi: int, in_lo: int, in_mid: int, in_hi: int, parent: TreeNode):
            left_num = in_mid - in_lo
            right_num = in_hi - in_mid

            if left_num > 0:
                left_val = preorder[pre_lo]
                left_node = TreeNode(left_val)
                parent.left = left_node

                left_idx = inorder.index(left_val, in_lo, in_mid)
                divide(pre_lo + 1, pre_lo + left_num - 1, in_lo, left_idx, in_mid - 1, left_node)

            if right_num > 0:
                right_val = preorder[pre_lo + left_num]
                right_node = TreeNode(right_val)
                parent.right = right_node

                right_idx = inorder.index(right_val, in_mid + 1, in_hi + 1)
                divide(pre_lo + left_num + 1, pre_hi, in_mid + 1, right_idx, in_hi, right_node)

        if preorder is None or len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        divide(1, len(preorder)-1, 0, idx, len(inorder) - 1, root)

        return root


s = Solution()
tree = s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
print(tree)