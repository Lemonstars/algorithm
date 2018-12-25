# Description
# 快速排序的核心思想是使用元素的值对数组进行划分。实现其非递归方案
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


def quick_sort(arr):
    num = len(arr)
    stack = [(0, num-1)]
    while stack:
        ran = stack.pop()
        low = ran[0]
        high = ran[1]

        p = partition(arr, low, high)
        if low < p - 1:
            stack.append((low, p-1))
        if p+1 < high:
            stack.append((p+1, high))


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[high], arr[i+1] = arr[i+1], arr[high]
    return i+1


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

        quick_sort(array)
        print_arr(array, number)
