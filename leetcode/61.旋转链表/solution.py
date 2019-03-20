# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
# 示例 2:
#
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None

        n = 1
        t = head
        while t.next:
            n += 1
            t = t.next
        k %= n

        if k == 0:
            return head

        quick_dummy = ListNode(-1)
        quick_dummy.next = head

        slow_dummy = ListNode(-1)
        slow_dummy.next = head

        while k > 0:
            quick_dummy = quick_dummy.next
            k -= 1

        while quick_dummy.next:
            quick_dummy = quick_dummy.next
            slow_dummy = slow_dummy.next

        new_head = slow_dummy.next
        slow_dummy.next = None
        t.next = head
        return new_head


s = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
p = s.rotateRight(n1, 2)
while p:
    print(p.val, end=' ')
    p = p.next
