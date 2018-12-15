# Description
# 从一列数中筛除尽可能少的数使得从左往右看，这些数是从小到大再从大到小的，连续出现的数值不应该有相等的情况
# Input
# 输入时一个数组，数值通过空格隔开。
# Output
# 输出筛选之后的数组，用空格隔开。如果有多种结果，则一行一种结果

# Sample Input 1
# 1 2 4 7 11 10 9 15 3 5 8 6
# Sample Output 1
# 1 2 4 7 11 10 9 8 6


def LIS(arr, increase):
    n = len(arr)
    pre = [i for i in range(n)]
    lis = [1 for i in range(n)]

    # compute the number of  longest increasing/decreasing
    # sequence end with every element
    for i in range(1, n):
        for j in range(i):
            is_consistent = arr[i] > arr[j] if increase else arr[i] < arr[j]
            if is_consistent and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                pre[i] = j

    # find the max number and the corresponding index
    end_index = 0
    num = 0
    for ind in range(n):
        if lis[ind] > num:
            num = lis[ind]
            end_index = ind

    # compute the increasing result
    res = [-1 for i in range(num)]
    while num > 0:
        res[num-1] = arr[end_index]
        end_index = pre[end_index]
        num -= 1

    return res


line = input().split()
data = [int(item) for item in line]
length = len(data)
max_size = 0
final_res = []
for index in range(length):
    increasing_res = LIS([data[i] for i in range(index)], True)
    increasing_size = len(increasing_res)
    decreasing_res = LIS([data[i] for i in range(index, length)], False)
    decreasing_size = len(decreasing_res)
    total_size = increasing_size + decreasing_size

    if total_size > max_size:
        max_size = total_size
        final_res.clear()
        for item in increasing_res:
            final_res.append(item)
        for item in decreasing_res:
            final_res.append(item)

for item in final_res:
    print(item, end=' ')
