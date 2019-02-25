# Description
# 棋盘覆盖问题：给定一个大小为2^n * 2^n个小方格的棋盘，其中有一个位置已经被填充，
# 现在要用一个L型（2*2个小方格组成的大方格中去掉其中一个小方格）形状去覆盖剩下的小方格。
# 求出覆盖方案，即哪些坐标下的小方格使用同一个L型格子覆盖。注意：坐标从0开始。左上方的第一个格子坐标为(0,0)，
# 第一行第二个坐标为(0,1)，第二行第一个为(1,0)，以此类推。
#
# Input
# 输入第一行为测试用例个数，后面每一个用例有两行，第一行为n值和特殊的格子的坐标（用空格隔开），
# 第二行为需要查找其属于同一个L型格子的格子坐标。
#
# Output
# 输出每一行为一个用例的解，先按照行值从小到大、再按照列值从小到大的顺序输出每一个用例的两个坐标；用逗号隔开

# Sample Input 1
# 1
# 1 1 1
# 0 0
#
# Sample Output 1
# 0 1,1 0


class Solution:

    def __init__(self, special, target, n):
        self.matrix = [[0 for j in range(pow(2, n))] for i in range(pow(2, n))]
        self.tag = 0
        self.process((0, 0), special, pow(2, n))
        self.target = target
        self.n = n

    def process(self, start, special, size):
        if size == 1:
            return

        s = size // 2
        self.tag += 1
        t = self.tag

        # left and up
        if special[0] < start[0] + s and special[1] < start[1] + s:
            self.process(start, special, s)
        else:
            self.matrix[start[0]+s-1][start[1]+s-1] = t
            self.process(start, (start[0]+s-1, start[1]+s-1), s)

        # right and up
        if special[0] < start[0] + s and special[1] >= start[1] + s:
            self.process((start[0], start[1]+s), special, s)
        else:
            self.matrix[start[0]+s-1][start[1]+s] = t
            self.process((start[0], start[1]+s), (start[0]+s-1, start[1]+s), s)

        # left and down
        if special[0] >= start[0] + s and special[1] < start[1] + s:
            self.process((start[0]+s, start[1]), special, s)
        else:
            self.matrix[start[0]+s][start[1]+s-1] = t
            self.process((start[0]+s, start[1]), (start[0]+s, start[1]+s-1), s)

        # right and down
        if special[0] >= start[0] + s and special[1] >= start[1] + s:
            self.process((start[0]+s, start[1]+s), special, s)
        else:
            self.matrix[start[0]+s][start[1]+s] = t
            self.process((start[0]+s, start[1]+s), (start[0]+s, start[1]+s), s)

    def solve(self):
        res = list()
        for i in range(max(0, target[0]-1), min(pow(2, self.n)-1, target[0]+1)+1):
            for j in range(max(0, target[1]-1), min(pow(2, self.n)-1, target[1]+1)+1):
                if self.matrix[i][j] == self.matrix[self.target[0]][self.target[1]] and \
                        (i != target[0] or j != target[1]):
                    res.append((i, j))
        return res


time = int(input())
while time > 0:
    # n & special coordinate
    line1 = [int(i) for i in input().split()]
    nk = line1[0]
    sp = (line1[1], line1[2])

    # target coordinate
    line2 = [int(i) for i in input().split()]
    target = (line2[0], line2[1])

    solution = Solution(sp, target, nk)
    res = solution.solve()

    for i in range(len(res)):
        if i == len(res) - 1:
            print(str(res[i][0]) + ' ' + str(res[i][1]))
        else:
            print(str(res[i][0]) + ' ' + str(res[i][1]), end=',')

    time -= 1
