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

        self.index2name_dict = dict()
        for item in self.name2index_dict.items():
            self.index2name_dict[item[1]] = item[0]

        # use adjacent list to store the graph
        self.adj = [[] for i in range(self.v_num)]
        for edge in edges:
            self.adj[self.name2index_dict[edge[0]]].append(self.name2index_dict[edge[1]])

        # whether a vertice has been visited
        self.visit = [False for i in range(self.v_num)]

        self.sort_stack = list()
        # dfs to topological sort
        for v in range(self.v_num):
            if not self.visit[v]:
                self.dfs(v)

    def dfs(self, v):
        self.visit[v] = True
        for e in self.adj[v]:
            if not self.visit[e]:
                self.dfs(e)
        self.sort_stack.append(self.index2name_dict[v])

    def print_sort(self):
        for i in range(len(self.sort_stack)-1, -1, -1):
            print(self.sort_stack[i], end=' ')
