# Description
# 实现计数排序，通过多次遍历数组，统计比每一个元素小的其它元素个数，根据该统计量对数据进行排序。
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


def counting_sort(arr, num):
    if num == 0:
        return

    min_num, max_num = arr[0], arr[0]
    for item in arr:
        if item > max_num:
            max_num = item
        if item < min_num:
            min_num = item
    r = max_num - min_num + 1

    count = [0 for i in range(r)]
    for i in range(num):
        count[arr[i] - min_num] += 1

    for i in range(r):
        c = count[i]
        while c != 0:
            if i == r-1 and c == 1:
                print(i + min_num)
            else:
                print(i + min_num, end=' ')
            c -= 1


if __name__ == '__main__':
    for line in sys.stdin:
        data = line.split()
        number = int(data[0])
        array = list()
        for index in range(1, len(data)):
            array.append(int(data[index]))

        counting_sort(array, number)
