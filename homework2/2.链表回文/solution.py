# Description
# 判断一个单向链表是否为回文结构。自定义链表数据结构，要求时间复杂度为O(n)，额外空间复杂度为O(1)。
#
# Input
# 输入的每一行的值用空格隔开，第一个值为节点个数，后面为每一个节点值
#
# Output
# 是回文则输出true，不是则输出false，一行表示一个链表的结果。

# Sample Input 1
# 3 1 2 1
# 4 1 2 2 1
# 3 3 5 3
# 6 a b c d c a
#
# Sample Output 1
# true
# true
# true
# false
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


if __name__ == '__main__':

    for line in sys.stdin:
        data_line = line.split()
        number = int(data_line[0])
        array = list()
        for index in range(1, len(data_line)):
            array.append(data_line[index])

        # construct the linked list
        head = tail = Node(array[0])
        for i in range(1, number):
            node = Node(array[i])
            tail.set_next(node)
            tail = node

        # assume that we just have the variable head
        quick, slow = head, head
        while quick.get_next() and quick.get_next().get_next():
            quick = quick.get_next().get_next()
            slow = slow.get_next()

        # reverse the linked list
        reverse = None
        first = slow.get_next()
        while first:
            second = first.get_next()
            first.set_next(reverse)
            reverse = first
            first = second

        is_par = True
        while reverse:
            if reverse.get_data() == head.get_data():
                reverse = reverse.get_next()
                head = head.get_next()
            else:
                is_par = False
                break

        print("true" if is_par else "false")
