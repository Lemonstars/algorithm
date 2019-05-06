# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
#
# 示例 1:
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
#
# 示例 2:
# 输入: 1->1->1->2->3
# 输出: 2->3

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummy = ListNode(head.val - 1)
        dummy.next = head

        pre = dummy
        cur = dummy.next
        pre_same = False
        while cur.next:
            if cur.val == cur.next.val:
                cur = cur.next
                pre.next = cur
                pre_same = True
            else:
                if pre_same:
                    cur = cur.next
                    pre.next = cur
                    pre_same = False
                else:
                    pre = pre.next
                    cur = cur.next

        if pre_same:
            pre.next = None

        return dummy.next


s = Solution()
n1 = ListNode(1)
n2 = ListNode(1)
n3 = ListNode(2)
n4 = ListNode(3)
n5 = ListNode(3)
n6 = ListNode(4)
n7 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n1 = s.deleteDuplicates(n1)
while n1:
    print(n1.val, end=' ')
    n1 = n1.next
