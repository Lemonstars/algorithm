# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 示例 1:
#
# 输入:
#     2
#    / \
#   1   3
# 输出: true

# 示例 2:
# 输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        left_null = root.left is None
        right_null = root.right is None

        if not left_null:
            left_max = root.left
            if left_max and left_max.val >= root.val:
                return False

            while left_max.right:
                left_max = left_max.right

            if left_max and left_max.val >= root.val:
                return False

        if not right_null:
            right_min = root.right
            if right_min and right_min.val <= root.val:
                return False

            while right_min.left:
                right_min = right_min.left

            if right_min and right_min.val <= root.val:
                return False

        if left_null and right_null:
            return True
        elif left_null:
            return self.isValidBST(root.right)
        elif right_null:
            return self.isValidBST(root.left)
        else:
            return self.isValidBST(root.left) and self.isValidBST(root.right)


node1 = TreeNode(10)
node2 = TreeNode(5)
node3 = TreeNode(15)
node4 = TreeNode(6)
node5 = TreeNode(20)
node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5
s = Solution()
print(s.isValidBST(node1))

