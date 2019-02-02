# Description
# 按照给定的起始顶点广度优先遍历图，每一次通过字母顺序选择顶点查找下一层邻接点，打印遍历顺序。
#
# Input
# 输入第一行为测试用例个数，后面每一个用例用多行表示，用例第一行是节点个数n和开始顶点，
# 用空格隔开，后面n+1行为图的邻接矩阵，其中第一行为节点名称。值之间使用空格隔开。
#
# Output
# 输出遍历顺序，用空格隔开

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
# a b c d


class BreadthFirstSearch:

    def __init__(self, numOfVertice, matrixOfEdge, nameOfVertice):
        self.numOfVertice = numOfVertice
        self.matrixOfEdge = matrixOfEdge
        self.vertice = [False for i in range(numOfVertice)]

        self.name_dict = dict()
        self.index_dict = dict()
        m = 0
        for name in nameOfVertice:
            self.name_dict[name] = m
            m += 1
        for key in self.name_dict.items():
            self.index_dict[key[1]] = key[0]

    def breadth_first_search(self, start_vertice):
        res = list()
        visit = list()

        start = self.name_dict[start_vertice]
        visit.append(start)
        self.vertice[start] = True

        while visit:
            v = visit.pop(0)
            all_edge = self.matrixOfEdge[v]
            for index in range(self.numOfVertice):
                if all_edge[index] == 1 and not self.vertice[index]:
                    self.vertice[index] = True
                    visit.append(index)
            res.append(v)

        return [self.index_dict[i] for i in res]


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

    breadth = BreadthFirstSearch(num, matrix, allVertice)
    r = breadth.breadth_first_search(start)
    for index in range(len(r)):
        if index == len(r) - 1:
            print(r[index])
        else:
            print(r[index], end=' ')

    time -= 1