# Description
# 实现插入排序。
#
# Input
# 输入的每一行代表一个数组，其中的值用空格隔开，第一个值表示数组的长度。
#
# Output
# 输出排序的数组，用空格隔开，末尾不要空格。

# Sample Input 1
# 13 24 3 56 34 3 78 12 29 49 84 51 9 100
#
# Sample Output 1
# 3 3 9 12 24 29 34 49 51 56 78 84 100
import sys


def insert_sort(arr, num):
    for i in range(1, num):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


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
