# 给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。
#
# 图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。
#
# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
#
# 输入：adjList = [[2,4],[1,3],[2,4],[1,3]]
# 输出：[[2,4],[1,3],[2,4],[1,3]]
# 解释：
# 图中有 4 个节点。
# 节点 1 的值是 1，它有两个邻居：节点 2 和 4 。
# 节点 2 的值是 2，它有两个邻居：节点 1 和 3 。
# 节点 3 的值是 3，它有两个邻居：节点 2 和 4 。
# 节点 4 的值是 4，它有两个邻居：节点 1 和 3 。


class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution:

    def __init__(self):
        self.visit = dict()

    def cloneGraph(self, node: Node) -> Node:
        if node is None:
            return node

        if self.visit.__contains__(node):
            return self.visit[node]

        cloneNode = Node(node.val, [])
        self.visit[node] = cloneNode

        for i in node.neighbors:
            cloneNode.neighbors.append(self.cloneGraph(i))

        return cloneNode

neig1 = []
node1 = Node(1, neig1)
neig2 = []
node2 = Node(2, neig2)
neig3 = []
node3 = Node(3, neig3)
neig4 = []
node4 = Node(4, neig4)

neig1.append(node2)
neig2.append(node4)
neig2.append(node1)
neig2.append(node3)
neig3.append(node2)
neig3.append(node4)
neig4.append(node1)
neig4.append(node3)
