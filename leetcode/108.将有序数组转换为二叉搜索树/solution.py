# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
#
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
# 示例:
# 给定有序数组: [-10,-3,0,5,9],
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
#


# Definition for a binary tree node.

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def divide(nums: List[int], lo: int, hi: int) -> TreeNode:
            if lo == hi:
                return TreeNode(nums[lo])

            mid = (lo + hi) // 2
            root = TreeNode(nums[mid])
            root.left = divide(nums, lo, mid - 1) if lo <= mid - 1 else None
            root.right = divide(nums, mid + 1, hi) if mid + 1 <= hi else None

            return root

        if not nums:
            return None

        return divide(nums, 0, len(nums) - 1)
