# Description
# 实现冒泡排序。
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


def insert_sort(arr, num):
    for i in range(num - 1):
        for j in range(num - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]


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

        insert_sort(array, number)
        print_arr(array, number)
