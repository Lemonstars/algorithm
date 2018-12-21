# Description
# Given an array of N distinct elements A[], find the minimum number of swaps required to sort the array.
# Your are required to complete the function which returns an integer denoting the minimum number of swaps,
# required to sort the array.
#
# Input
# The first line of input contains an integer T denoting the number of test cases.
# Then T test cases follow. Each test case contains an integer N denoting
# the number of element of the array A[]. In the next line are N space separated
# values of the array A[] .(1<=T<=100; 1<=N<=100; 1<=A[]<=1000)
#
# Output
# For each test case in a new line output will be an integer denoting minimum umber
# of swaps that are required to sort the array.

# Sample Input 1
# 2
# 4
# 4 3 2 1
# 5
# 1 5 4 3 2
#
# Sample Output 1
# 2
# 2


def min_swaps(arr, length):
    arr_pos = [*enumerate(arr)]
    arr_pos.sort(key=lambda it: it[1])
    vis = {k: False for k in range(length)}

    ans = 0
    for i in range(length):
        if vis[i] or arr_pos[i][0] == i:
            continue
        cycle_size = 0
        j = i
        while not vis[j]:
            vis[j] = True
            j = arr_pos[j][0]
            cycle_size += 1
        if cycle_size > 0:
            ans += (cycle_size - 1)
    return ans


t = int(input())
while t > 0:
    size = int(input())
    arr = list()
    for item in input().split():
        arr.append(int(item))

    print(min_swaps(arr, len(arr)))
    t -= 1

