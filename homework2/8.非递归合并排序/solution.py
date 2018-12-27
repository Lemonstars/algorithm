# Description
# 合并（归并）排序的核心思想是：每次从中间位置将数组分组再分别排序。请实现其非递归方案。
#
# Input
# 输入的每一行表示一个元素为正整数的数组，所有值用空格隔开，第一个值为数值长度，其余为数组元素值。
#
# Output
# 输出的每一行为排序结果，用空格隔开，末尾不要空格。

# Sample Input 1
# 13 24 3 56 34 3 78 12 29 49 84 51 9 100
#
# Sample Output 1
# 3 3 9 12 24 29 34 49 51 56 78 84 100
import sys


def merge_sort(arr):
    num = len(arr)
    step = 1
    while step < num:
        left = 0
        while left + step < num:
            # the mid index
            mid = left + step - 1

            # the right index
            right_tmp = left + 2 * step - 1
            right = right_tmp if right_tmp < num else num-1

            # merge from bottom
            merge(arr, left, mid, right)

            # break when reach the end
            left += 2 * step

        step *= 2


def merge(arr, p, q, r):
    left_len = q-p+1
    right_len = r-q
    left = [arr[p+i] for i in range(left_len)]
    right = [arr[q+1+i] for i in range(right_len)]
    i = 0
    j = 0

    for k in range(p, r+1):
        if i == left_len:
            arr[k] = right[j]
            j += 1
        elif j == right_len:
            arr[k] = left[i]
            i += 1
        elif left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1


def print_arr(arr, num):
    for i in range(num):
        if i == num - 1:
            print(arr[i])
        else:
            print(arr[i], end=' ')


if __name__ == '__main__':

    for line in sys.stdin:
        data = line.split()
        number = int(data[0])
        array = list()
        for index in range(1, len(data)):
            array.append(int(data[index]))

        merge_sort(array)
        print_arr(array, number)
