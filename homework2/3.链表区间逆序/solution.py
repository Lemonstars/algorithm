# Description
# 将单个链表的每K个节点之间逆序，打印出新链表；最后不足K的节点数不需要逆序；要求时间复杂度为O(n)，额外空间复杂度为O(1)。
#
# Input
# 输入的每一行的值用空格隔开，第一个表示链表长度，中间为节点值，最后代表K。
#
# Output
# 输出的每一行为新的链表，节点值用空格隔开，末尾不要空格。

# Sample Input 1
# 8 1 2 3 4 5 6 7 8 3
# 8 a b c d e f g h 4
#
# Sample Output 1
# 3 2 1 6 5 4 7 8
# d c b a h g f e
import sys


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


def reverse(left_node, start_node, end_node, right_node):
    pre = None
    cur = start_node
    while True:
        nex = cur.get_next()
        cur.set_next(pre)
        pre = cur

        if cur == end_node:
            break

        cur = nex

    if left_node:
        left_node.set_next(end_node)

    start_node.set_next(right_node)
    return end_node, start_node


if __name__ == '__main__':

    for line in sys.stdin:
        data_line = line.split()
        number = int(data_line[0])
        array = list()
        for index in range(1, len(data_line)-1):
            array.append(data_line[index])
        k = int(data_line[len(data_line)-1])

        # construct the linked list
        head = tail = Node(array[0])
        for i in range(1, number):
            node = Node(array[i])
            tail.set_next(node)
            tail = node

        # reverse every k interval
        current = head
        previous = None
        start = None
        cnt = 1
        while current:
            next_node = current.get_next()
            if cnt == k:
                start = head if previous is None else previous.get_next()
                if previous is None:
                    head, previous = reverse(previous, start, current, next_node)
                else:
                    previous = reverse(previous, start, current, next_node)[1]
                cnt = 1
            else:
                cnt += 1
            current = next_node

        while head:
            if head.get_next():
                print(head.get_data(), end=' ')
            else:
                print(head.get_data(), end='')
            head = head.get_next()
        print()
