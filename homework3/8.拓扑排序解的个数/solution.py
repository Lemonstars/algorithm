# Description
# 给定有向无环图中所有边，计算图的拓扑排序解的个数。
#
# Input
# 输入第一行为用例个数，后面每一行表示一个图中的所有边，边的起点和终点用空格隔开，边之间使用逗号隔开。
#
# Output
# 输出拓扑排序解的个数

# Sample Input 1
# 1
# a c,b c,c d,d e,d f,e g,f g
#
# Sample Output 1
# 4


class SymbolGraph:
    def __init__(self, edges):
        self.v_num = 0
        self.name2index_dict = dict()

        # compute the dict from symbol to index
        for edge in edges:
            start = edge[0]
            end = edge[1]

            if start not in self.name2index_dict:
                self.name2index_dict[start] = self.v_num
                self.v_num += 1

            if end not in self.name2index_dict:
                self.name2index_dict[end] = self.v_num
                self.v_num += 1

        # use adjacent list to store the graph
        self.adj = [[] for i in range(self.v_num)]
        for edge in edges:
            self.adj[self.name2index_dict[edge[0]]].append(self.name2index_dict[edge[1]])

    def num_of_topological(self):
        son = [0 for i in range(self.v_num)]
        for i in range(len(self.adj)):
            for j in range(len(self.adj[i])):
                son[i] |= (1 << self.adj[i][j])

        end = (1 << self.v_num)
        dp = [0 for i in range(end)]
        dp[0] = 1

        for i in range(end):
            if dp[i] > 0:
                for j in range(self.v_num):
                    if ((i & son[j]) == son[j]) and ((i & (1 << j)) == 0):
                        dp[i | (1 << j)] += dp[i]

        return dp[end-1]


# time = int(input())
time = 1
while time > 0:
    all_edge = [(item.split()[0], item.split()[1])for item in 'a c,b c,c d,d e,d f,e g,f g'.split(',')]
    # all_edge = [(item.split()[0], item.split()[1])for item in input().split(',')]
    symbol_graph = SymbolGraph(all_edge)
    print(symbol_graph.num_of_topological())
    time -= 1
