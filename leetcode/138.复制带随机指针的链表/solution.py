# 给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
# 要求返回这个链表的 深拷贝。 
# 我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
#
# val：一个表示 Node.val 的整数。
# random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    def __init__(self):
        self.visit = dict()

    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return head

        if self.visit.__contains__(head):
            return self.visit[head]

        copy_node = Node(head.val)
        self.visit[head] = copy_node

        copy_node.random = self.copyRandomList(head.random)
        copy_node.next = self.copyRandomList(head.next)

        return copy_node