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


t = int(input())
while t > 0:
    # input
    size = int(input())
    arr = list()
    for item in input().split():
        arr.append(int(item))

    # store the sorted array and corresponding dict
    sort_arr = sorted(arr)
    value2index_dict = dict()
    for index in range(size):
        value2index_dict[sort_arr[index]] = index

    # compute the number of swap
    cnt = 0
    for i in range(size):
        if arr[i] == sort_arr[i]:
            continue
        else:
            tmp = arr[i]
            arr[i] = arr[value2index_dict[tmp]]
            arr[value2index_dict[tmp]] = tmp
            cnt += 1
    print(cnt)

    t -= 1

