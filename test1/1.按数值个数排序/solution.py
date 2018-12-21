# Description
# Given an array of integers, sort the array according to frequency of elements. For example,
# if the input array is {2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12},
# then modify the array to {3, 3, 3, 3, 2, 2, 2, 12, 12, 4, 5}.
# If frequencies of two elements are same, print them in increasing order.

# Input
# The first line of input contains an integer T denoting the number of test cases.
# The description of T test cases follows. The first line of each test case contains
# a single integer N denoting the size of array. The second line contains N space-separated
# integers A1, A2, ..., AN denoting the elements of the array.
# （1 ≤ T ≤ 70；30 ≤ N ≤ 130；1 ≤ A [ i ] ≤ 60 ）

# Output
# Print each sorted array in a separate line.
# For each array its numbers should be separated by space.

# Sample Input 1
# 1
# 5
# 5 5 4 6 4

# Sample Output 1
# 4 4 5 5 6


def quick_sort(data, low, high):
    if low < high:
        p = partition(data, low, high)
        quick_sort(data, low, p-1)
        quick_sort(data, p+1, high)


def partition(data, low, high):
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if (data[j][1] > pivot[1]) or \
                (data[j][1] == pivot[1] and data[j][0] < pivot[0]):
            i += 1
            tmp = data[i]
            data[i] = data[j]
            data[j] = tmp

    tmp = data[high]
    data[high] = data[i+1]
    data[i+1] = tmp

    return i+1


t = int(input())
while t > 0:
    # input
    size = int(input())
    arr = list()
    for item in input().split():
        arr.append(int(item))

    # store the frequency
    value_to_num_dict = dict()
    for item in arr:
        if item not in value_to_num_dict:
            value_to_num_dict[item] = 1
        else:
            value_to_num_dict[item] += 1

    # use tuple to store
    value_to_num_list = list()
    for key in value_to_num_dict:
        value_to_num_list.append((key, value_to_num_dict[key]))

    # use custom quick sort
    quick_sort(value_to_num_list, 0, len(value_to_num_list) - 1)

    # print the result
    for item in value_to_num_list:
        for i in range(int(item[1])):
            print(item[0], end=' ')

    t -= 1
