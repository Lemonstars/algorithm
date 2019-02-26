# Description
# 对给定的点集合构造KD树，要求如下：将方差最大的维度作为当前的分割维度，
# 将数据集在分割维度上排序后的中位数作为分割点。程序要检索给定点对应的最近的K个点的坐标。
#
# Input
# 输入第一行为测试用例个数，后面为测试用例，每一个用例包含三行，
# 第一行为点集合（点之间用逗号隔开，两个坐标用空格隔开），第二行为检索的点，第三行为K值。
#
# Output
# 输出每一个用例的最近K个点，按照距离从小到大的顺序打印

# Sample Input 1
# 1
# 3 5,6 2,5 8,9 3,8 6,1 1,2 9
# 8.2 4.6
# 2
#
# Sample Output 1
# 8 6,9 3
import sys
import math


class Node:

    def __init__(self, point, d):
        self.left = None
        self.right = None
        self.point = point
        self.d = d


class KD_Tree:

    def __init__(self, data):
        self.root = None

        while len(data) > 0:
            variance1 = self.variance([i[0] for i in data])
            variance2 = self.variance([i[1] for i in data])

            d = 0 if variance1 > variance2 else 1
            cur_index = self.quick_mid(data, 0, len(data)-1, (len(data)-1)//2, d)
            node = Node(data[cur_index], d)

            if self.root is None:
                self.root = node
            else:
                start = self.root
                while True:
                    if start.point[start.d] > node.point[start.d]:
                        if start.left is None:
                            start.left = node
                            break
                        else:
                            start = start.left
                    else:
                        if start.right is None:
                            start.right = node
                            break
                        else:
                            start = start.right

            del data[cur_index]

    def distance(self, point1, point2):
        return math.sqrt((point1[0]-point2[0]) * (point1[0]-point2[0]) + (point1[1]-point2[1]) * (point1[1]-point2[1]))

    def quick_mid(self, point_arr, start, end, target, dimension):
        pivot = point_arr[end][dimension]
        i = start - 1
        for j in range(start, end):
            if point_arr[j][dimension] < pivot:
                i += 1
                point_arr[i], point_arr[j] = point_arr[j], point_arr[i]
        point_arr[i + 1], point_arr[end] = point_arr[end], point_arr[i + 1]

        if i + 1 == target:
            return i+1
        elif i + 1 > target:
            return self.quick_mid(point_arr, start, i, target, dimension)
        else:
            return self.quick_mid(point_arr, i + 2, end, target, dimension)

    def variance(self, arr):
        length = len(arr)
        if length == 0:
            return -1
        avg = sum(arr) / length
        res = 0
        for num in arr:
            res += (num - avg) * (num - avg)

        return res / length

    def search(self, target, k):
        path = list()
        start = self.root
        while start is not None:
            path.append(start)
            if target[start.d] < start.point[start.d]:
                start = start.left
            else:
                start = start.right

        dis = [((-1, -1), sys.maxsize) for i in range(k)]
        while path:
            cur_node = path[-1]
            cur_dis = self.distance(target, cur_node.point)

            i = len(dis) - 1
            dis.append(((-1, -1), sys.maxsize))
            while i >= 0:
                if cur_dis < dis[i][1]:
                    dis[i+1] = dis[i]
                else:
                    break
                i -= 1
            dis[i+1] = (cur_node, cur_dis)

            del dis[-1]
            del path[-1]

            if i+1 <= k-1:
                another = cur_node.right if target[cur_node.d] <= cur_node.point[cur_node.d] else cur_node.left
                if another is not None:
                    path.append(another)

        return [d[0] for d in dis]


def wrap_num(num):
    num_int = int(num)
    return str(num_int) if abs(num_int - num) < 0.000001 else str(num)


time = int(input())
while time > 0:
    data = [i for i in input().split(',')]
    point = [(float(i.split()[0]), float(i.split()[1])) for i in data]
    line2 = input().split()
    search = (float(line2[0]), float(line2[1]))
    k = int(input())

    solution = KD_Tree(point)
    res = solution.search(search, k)
    for i in range(len(res)):
        if i == len(res) - 1:
            print(wrap_num(res[i].point[0]) + ' ' + wrap_num(res[i].point[1]))
        else:
            print(wrap_num(res[i].point[0]) + ' ' + wrap_num(res[i].point[1]), end=',')

    time -= 1
