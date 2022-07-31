# 给定一个单链表 L 的头节点 head ，单链表 L 表示为：
# L0 → L1 → … → Ln - 1 → Ln

# 请将其重新排列后变为：
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

# 提示：
#
# 链表的长度范围为 [1, 5 * 104]
# 1 <= node.val <= 1000

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def printList(self, head: Optional[ListNode]) -> None:
        while head:
            print(head.val, ',', end='')
            head = head.next
        print()

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # use quick and slow pointer
        slow = head
        quick = head.next
        while quick and quick.next:
            slow = slow.next
            quick = quick.next.next
        even_head = slow.next
        odd_head = head
        slow.next = None

        # reverse the even node list
        pre = None
        pointer = even_head
        while pointer:
            temp = pointer.next
            pointer.next = pre

            pre = pointer
            pointer = temp

        even_head = pre

        # join the two node list
        odd_pointer = odd_head
        even_pointer = even_head
        while odd_pointer or even_pointer:
            odd_temp = odd_pointer.next
            odd_pointer.next = even_pointer
            odd_pointer = odd_temp

            if even_pointer:
                even_temp = even_pointer.next
                even_pointer.next = odd_pointer
                even_pointer = even_temp

        self.printList(head)


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
# node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
# node4.next = node5
solution = Solution()
solution.reorderList(node1)