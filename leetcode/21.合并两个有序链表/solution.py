# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例：
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy_head = ListNode(-1)
        cur_node = dummy_head

        while True:
            if l1 and not l2:
                cur_node.next = l1
                l1 = l1.next
                cur_node = cur_node.next
            elif l2 and not l1:
                cur_node.next = l2
                l2 = l2.next
                cur_node = cur_node.next
            elif not l1 and not l2:
                break
            else:
                if l1.val < l2.val:
                    cur_node.next = l1
                    l1 = l1.next
                else:
                    cur_node.next = l2
                    l2 = l2.next
                cur_node = cur_node.next

        return dummy_head.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
node1.next = node2
node2.next = node3

node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)
node4.next = node5
node5.next = node6

s = Solution()
s.mergeTwoLists(node1, node4)
