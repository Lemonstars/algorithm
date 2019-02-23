# Description
# 实现Shell排序，对给定的无序数组，按照给定的间隔变化（间隔大小即同组数字index的差），
# 打印排序结果，注意不一定是最终排序结果！
#
# Input
# 输入第一行表示测试用例个数，后面为测试用例，每一个用例有两行，
# 第一行为给定数组，第二行为指定间隔，每一个间隔用空格隔开。
#
# Output
# 输出的每一行为一个用例对应的指定排序结果。

# Sample Input 1
# 1
# 49 38 65 97 76 13 27 49 55 4
# 5 3
#
# Sample Output 1
# 13 4 49 38 27 49 55 65 97 76


def shell_sort(data, gap_arr):
    length = len(data)
    gap_len = len(gap_arr)
    index = 0
    while index < gap_len:
        gap = gap_arr[index]
        for i in range(gap, length):
            tmp = data[i]
            j = i
            while j >= gap and data[j - gap] > tmp:
                data[j] = data[j - gap]
                j -= gap
            data[j] = tmp

        index += 1


time = int(input())
while time > 0:
    num = [int(i) for i in input().split()]
    gap_arr = [int(i) for i in input().split()]
    shell_sort(num, gap_arr)
    for i in range(len(num)):
        if i == len(num) - 1:
            print(num[i], )
        else:
            print(num[i], end=' ')
    time -= 1
