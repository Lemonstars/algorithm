# Description
# 按照给定的起始顶点深度优先遍历给定的无向图，尝试所有可能的遍历方式，打印遍历过程中出现的最大深度。
#
# Input
# 输入第一行是用例个数，后面每个用例使用多行表示，用例的第一行是图中节点的个数n和起始点，
# 用空格隔开，后面n+1行为图的邻接矩阵，其中第一行为节点名称。值之间使用空格隔开。
#
# Output
# 输出深度优先遍历中遇到的最大深度。

# Sample Input 1
# 1
# 4 a
# a b c d
# a 0 1 1 0
# b 1 0 1 0
# c 1 1 0 1
# d 0 0 1 0
#
# Sample Output 1
# 4


class DepthFirstSearch:

    def __init__(self, numOfVertice, matrixOfEdge, nameOfVertice):
        self.numOfVertice = numOfVertice
        self.matrixOfEdge = matrixOfEdge
        self.vertice = [False for i in range(numOfVertice)]

        self.name_dict = dict()
        m = 0
        for name in nameOfVertice:
            self.name_dict[name] = m
            m += 1
        self.maxDepth = 1

    def depth_first_search(self, start_vertice, depth):
        self.vertice[start_vertice] = True
        all_edge = self.matrixOfEdge[start_vertice]
        for index in range(self.numOfVertice):
            if all_edge[index] == 1 and not self.vertice[index]:
                if depth + 1 > self.maxDepth:
                    self.maxDepth = depth + 1
                self.vertice[index] = True
                self.depth_first_search(index, depth + 1)

    def getMaxDepth(self, start_vertice):
        self.depth_first_search(self.name_dict[start_vertice], 1)
        return self.maxDepth


time = int(input())
while time > 0:
    info = input().split()
    num = int(info[0])
    start = info[1]

    allVertice = [i for i in input().split()]
    matrix = list()
    count = num
    while count > 0:
        matrix.append([int(item) for item in input().split()[1:]])
        count -= 1

    depth = DepthFirstSearch(num, matrix, allVertice)
    print(depth.getMaxDepth(start))

    time -= 1
