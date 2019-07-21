# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
#
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
# 示例:
#
# 给定的有序链表： [-10, -3, 0, 5, 9],
#
# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def length(self, node: ListNode) -> int:
        n = 0
        while node:
            n += 1
            node = node.next

        return n

    def sortedListToBST(self, head: ListNode) -> TreeNode:

        def f(lo: int, hi: int):
            if lo > hi:
                return

            nonlocal head
            mid = (lo + hi) // 2

            left = f(lo, mid - 1)
            node = TreeNode(head.val)
            head = head.next
            right = f(mid + 1, hi)

            node.left = left
            node.right = right

            return node

        return f(0, self.length(head) - 1)


node1 = ListNode(-10)
node2 = ListNode(-3)
node3 = ListNode(0)
node4 = ListNode(5)
node5 = ListNode(9)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
s = Solution()
print(s.sortedListToBST(node1))
