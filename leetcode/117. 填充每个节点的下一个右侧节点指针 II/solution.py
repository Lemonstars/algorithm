# 给定一个二叉树
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
# 初始状态下，所有 next 指针都被设置为 NULL。
#
#
# 示例：
# 输入：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":null,"next":null,"right":{"$id":"6","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}
# 输出：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":null,"right":null,"val":7},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"6","left":null,"next":null,"right":{"$ref":"5"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"6"},"val":1}
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
#  
#
# 提示：
# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。


class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:

    def next_node(self, root: 'Node') -> 'Node':
        while root:
            if root.left:
                return root.left
            elif root.right:
                return root.right
            else:
                root = root.next
        return root

    def connect(self, root: 'Node') -> 'Node':
        if root is None or (root.left is None and root.right is None):
            return root

        if root.left and root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = self.next_node(root.next)
        else:
            if root.next:
                target_node = root.left if root.left else root.right
                target_node.next = self.next_node(root.next)

        self.connect(root.right)
        self.connect(root.left)

        return root


node4 = Node(4, None, None, None)

node8 = Node(8, None, None, None)
node7 = Node(7, None, node8, None)
node6 = Node(6, None, node7, None)
node5 = Node(5, None, None, None)
node3 = Node(3, node7, None, None)
node2 = Node(2, node3, node5, None)
node1 = Node(1, node2, node6, None)