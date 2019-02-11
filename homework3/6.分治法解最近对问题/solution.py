# Description
# 最近对问题：使用分治算法解决最近对问题。
#
# Input
# 第一行为测试用例个数。后面每一行表示一个用例，一个用例为一些平面上点的集合，
# 点与点之间用逗号隔开，一个点的两个坐标用空格隔开。坐标值都是正数。
#
# Output
# 对每一个用例输出两个距离最近的点（坐标使用空格隔开），用逗号隔开，先按照第一个坐标大小排列，
# 再按照第二个坐标大小排列。如果有多个解，则按照每个解的第一个点的坐标排序，连续输出多个解，用逗号隔开。

# Sample Input 1
# 1
# 1 1,2 2,3 3,4 4,5 5,1.5 1.5
#
# Sample Output 1
# 1 1,1.5 1.5,1.5 1.5,2 2
import sys
from functools import cmp_to_key


def solve(data):
    unsort = divide(data, sys.maxsize, [], 0, len(data))[1]
    return sorted(unsort, key=cmp_to_key(answer_compare))


def divide(data, val, res, start, end):
    if start == end:
        return val, res

    mid = (start + end) // 2
    left = divide(data, val, res, start, mid)
    if left[0] < val:
        val = left[0]
        res = left[1]
    elif left[0] == val:
        res += left[1]

    right = divide(data, val, res, mid + 1, end)
    if right[0] < val:
        val = right[0]
        res = right[1]
    elif right[0] == val:
        res += right[1]

    for i in range(start, mid+1):
        for j in range(mid+1, end):
            current_val = (data[i][0] - data[j][0]) * (data[i][0] - data[j][0]) + \
                          (data[i][1] - data[j][1]) * (data[i][1] - data[j][1])
            if current_val < val:
                val = current_val
                res = [(data[i], data[j])] if compare(data[i], data[j]) < 0 else [(data[j], data[i])]
            elif current_val == val:
                res.append((data[i], data[j]) if compare(data[i], data[j]) < 0 else (data[j], data[i]))

    return val, res


def compare(i, j):
    if i[0] > j[0]:
        return 1

    if i[0] < j[0]:
        return -1

    if i[1] > j[1]:
        return 1

    if i[1] < j[1]:
        return -1

    return 0


def answer_compare(i, j):
    first = compare(i[0], j[0])
    if first != 0:
        return first

    second = compare(i[1], j[1])
    return second


time = int(input())
while time > 0:
    coordinate = input().split(',')
    data = [(float(item.split()[0]), float(item.split()[1])) for item in coordinate]
    res = solve(data)
    for i in range(len(res)):
        if i != len(res)-1:
            print(str(res[i][0][0]) + ' ' + str(res[i][0][1]) + ',' +
                  str(res[i][1][0]) + ' ' + str(res[i][1][1]), end=',')
        else:
            print(str(res[i][0][0]) + ' ' + str(res[i][0][1]) + ',' +
                  str(res[i][1][0]) + ' ' + str(res[i][1][1]))
    time -= 1
