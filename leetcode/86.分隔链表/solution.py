# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
# 你应当保留两个分区中每个节点的初始相对位置。
#
# 示例:
# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy_more = ListNode(-1)
        more_cur = dummy_more

        dummy = ListNode(-1)
        dummy.next = head

        cur, pre = head, dummy
        while cur:
            if cur.val >= x:
                more_cur.next = cur
                more_cur = more_cur.next

                pre.next = cur.next
                cur = cur.next
            else:
                cur = cur.next
                pre = pre.next

        more_cur.next = None
        pre.next = dummy_more.next
        return dummy.next


s = Solution()
n1 = ListNode(1)
n2 = ListNode(4)
n3 = ListNode(3)
n4 = ListNode(2)
n5 = ListNode(5)
n6 = ListNode(2)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
res = s.partition(n1, 3)
while res:
    print(res.val, end=' ')
    res = res.next
