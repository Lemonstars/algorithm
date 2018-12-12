# Description
# 给定数组arr和整数num，求arr的子数组中满足：
# 其最大值减去最小值的结果大于num的个数。请实现一个时间复杂度为O(length(arr))的算法。
# Input
# 输入的第一行为数组，每一个数用空格隔开，第二行为num。
# Output
# 输出一个值。

# Sample Input 1
# 3 6 4 3 2
# 2
# Sample Output 1
# 6
# [3, 6] [3, 6, 4] [3, 6, 4, 3] [3, 6, 4, 3, 2] [6, 4, 3] [6, 4, 3, 2]

from collections import deque

# input
line = input()
nums = line.split()
arr = list()
for item in nums:
    arr.append(int(item))
num = int(input())

qmax = deque()
qmin = deque()
length = len(arr)
i = 0
j = 0
res = 0

while i < length:
    while j < length:
        # maintain the decreasing order and store the index
        while qmax and arr[j] >= arr[qmax[-1]]:
            qmax.pop()
        qmax.append(j)

        # maintain the increasing order and store the index
        while qmin and arr[j] <= arr[qmin[-1]]:
            qmin.pop()
        qmin.append(j)

        # if the current arr[i...j] does't satisfy the property,
        # stop moving j and check for i
        if arr[qmax[0]] - arr[qmin[0]] > num:
            break

        # if the current arr[i..j] satisfy the property,
        # continue to move j and iterate
        j += 1

    # the current arr[i...j] is the first that does't satisfy the property
    # for a given i, so the every sub array is the target
    res += j - i

    # print all the sub array
    # for k in range(j-i):
    #     for p in range(k+1):
    #         print(arr[i+p], end=" ")
    #     print()

    # if the index of the max or the min of the current array is
    # out of the range from i to j, pop the first one
    if qmax[0] == i:
        qmax.popleft()
    if qmin[0] == i:
        qmin.popleft()

    # the step of i is one so that the above code would pop all elements
    # that are out of the range
    i += 1

data_len = len(arr)
res = data_len * (data_len + 1) / 2 - res
print(int(res))
