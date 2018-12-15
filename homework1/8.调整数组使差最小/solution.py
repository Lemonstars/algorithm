# Description
# 有两个序列 a,b,大小都为n,序列元素的值任意整数,无序；
# 要求：通过交换 a,b 中的元素，使[序列a元素的和]与[序列b元素的和]之间的差最小。
# Input
# 输入为两行，分别为两个数组，每个值用空格隔开。
# Output
# 输出变化之后的两个数组内元素和的差绝对值。

# Sample Input
# 100 99 98 1 2 3
# 1 2 3 4 5 40
# Sample Output
# 48
# [1 2 3 4 98 100]
# [1 2 3 5 40 99]

arr1 = list()
for item in input().split():
    arr1.append(int(item))
arr2 = list()
for item in input().split():
    arr2.append(int(item))

n = len(arr1)
sumA = sum(arr1)
sumB = sum(arr2)

diff = abs(sumA - sumB)
min_i = -1
min_j = -1

while diff != 0:
    isBetter = False
    for i_index in range(len(arr1)):
        for j_index in range(len(arr2)):
            cur_diff = abs(sumA - sumB - 2 * (arr1[i_index] - arr2[j_index]))
            if diff > cur_diff:
                isBetter = True
                diff = cur_diff
                min_i = i_index
                min_j = j_index

    if isBetter:
        arr1[min_i], arr2[min_j] = arr2[min_j], arr1[min_i]
        sumA = sum(arr1)
        sumB = sum(arr2)
    else:
        break

print(diff)
