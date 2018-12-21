# Description
# 有一个由N个实数构成的数组，如果一对元素A[i]和A[j]是倒序的，
# 即i<j但是A[i]>A[j]则称它们是一个倒置，设计一个计算该数组中所有倒置数量的算法。要求算法复杂度为O(nlogn)
#
# Input
# 输入有多行，第一行整数T表示为测试用例个数，后面是T个测试用例，
# 每一个用例包括两行，第一行的一个整数是元素个数，第二行为用空格隔开的数组值。
#
# Output
# 输出每一个用例的倒置个数，一行表示一个用例。

# Sample Input 1
# 1
# 8
# 8 3 2 9 7 1 5 4
#
# Sample Output 1
# 17


def InversionNum(lst):
    if len(lst) == 1:
        return lst, 0
    else:
        n = len(lst) // 2
        lst1, count1 = InversionNum(lst[0:n])
        lst2, count2 = InversionNum(lst[n:len(lst)])
        lst, count = Count(lst1, lst2, 0)
        return lst, count1 + count2 + count


def Count(lst1, lst2, count):
    i = 0
    j = 0
    res = []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            count += len(lst1) - i
            j += 1
    res += lst1[i:]
    res += lst2[j:]
    return res, count


t = int(input())
while t > 0:
    size = int(input())
    arr = list()
    for item in input().split():
        arr.append(int(item))

    print(InversionNum(arr)[1])
    t -= 1
