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


def reserve_num(data, p, r):
    count = 0
    if p < r:
        q = (p + r) // 2
        left_num = reserve_num(data, p, q)
        right_num = reserve_num(data, p+1, r)
        mid_num = merge(data, p, q, r)
        count = left_num + right_num + mid_num
    return count


def merge(data, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    left = list()
    right = list()
    for i in range(p, q+1):
        left.append(data[i])
    for i in range(q+1, r+1):
        right.append(data[i])

    i, j, cnt = 0, 0, 0
    for k in range(p, r+1):
        # when either of the index reaches the end,
        # all reserved pairs have been calculated.
        if i == n1 or j == n2:
            break
        elif left[i] <= right[j]:
            data[k] = left[i]
            i += 1
        elif left[i] > right[j]:
            data[k] = right[j]
            j += 1
            # 以逆序对的第二项为累加的标准
            cnt += n1-i
    return cnt


t = int(input())
while t > 0:
    size = int(input())
    arr = list()
    for item in input().split():
        arr.append(int(item))

    print(reserve_num(arr, 0, len(arr)-1))
    t -= 1
