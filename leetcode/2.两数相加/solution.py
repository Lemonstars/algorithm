# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode(-1)
        current = dummy_head
        carry = 0

        while l1 is not None or l2 is not None:
            if l1 is not None:
                l1_num = l1.val
                l1 = l1.next
            else:
                l1_num = 0

            if l2 is not None:
                l2_num = l2.val
                l2 = l2.next
            else:
                l2_num = 0

            num = l1_num + l2_num + carry
            if num > 9:
                carry = 1
                num -= 10
            else:
                carry = 0

            node = ListNode(num)
            current.next = node
            current = node

        if carry != 0:
            current.next = ListNode(carry)

        return dummy_head.next
