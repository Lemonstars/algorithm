# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre_node = dummy_node
        cur_node = dummy_node

        while n > 0:
            cur_node = cur_node.next
            n -= 1

        while cur_node.next:
            cur_node = cur_node.next
            pre_node = pre_node.next

        pre_node.next = pre_node.next.next
        return dummy_node.next
