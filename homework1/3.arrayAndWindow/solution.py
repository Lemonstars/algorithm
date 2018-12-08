# -*- coding: utf-8 -*
# Description
# 给定一个整型数组arr和一个大小为w的窗口，窗口从数组最左边滑动到最右边，
# 每次向右滑动一个位置，求出每一次滑动时窗口内最大元素的和。
# Input
# 输入的第一行为数组，每一个元素使用空格隔开；第二行为窗口大小。
# Output

# Sample Input 1
# 4 3 5 4 3 3 6 7
# 3
# Sample Output 1
# 27

from collections import deque

# input: data & width
data = list()
arr = input()
num = arr.split(' ')
for item in num:
    data.append(int(item))
width = int(input())

# process
res = 0
max_queue = deque()
for index in range(len(data)):
    item = data[index]
    while max_queue and item >= data[max_queue[-1]]:
        max_queue.pop()
    max_queue.append(index)

    while max_queue and max_queue[0] <= index - width:
        max_queue.popleft()

    if index >= width-1:
        res += data[max_queue[0]]

print(res)
