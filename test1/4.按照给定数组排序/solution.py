# Description
# Given two array A1[] and A2[], sort A1 in such a way that the relative order among the elements will
# be same as those in A2. For the elements not present in A2. Append them at last in sorted order.
# It is also given that the number of elements in A2[] are smaller than or equal to number of elements
# in A1[] and A2[] has all distinct elements.
#
# Input:A1[] = {2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8} A2[] = {2, 1, 8, 3}
# Output: A1[] = {2, 2, 1, 1, 8, 8, 3, 5, 6, 7, 9}
# Since 2 is present first in A2[], all occurrences of 2s should appear first in A[],
# then all occurrences 1s as 1 comes after 2 in A[]. Next all occurrences of 8 and then
# all occurrences of 3. Finally we print all those elements of A1[] that are not present in A2[]
# Constraints:1 ≤ T ≤ 501 ≤ M ≤ 501 ≤ N ≤ 10 & N ≤ M1 ≤ A1[i], A2[i] ≤ 1000
#
# Input
# The first line of input contains an integer T denoting the number of test cases.
# The first line of each test case is M and N. M is the number of elements in A1 and N is
# the number of elements in A2.The second line of each test case contains M elements.
# The third line of each test case contains N elements.
#
# Output
# Print the sorted array according order defined by another array.

# Sample Input 1
# 1
# 11 4
# 2 1 2 5 7 1 9 3 6 8 8
# 2 1 8 3
#
# Sample Output 1
# 2 2 1 1 8 8 3 5 6 7 9


def quick_sort(data, low, high):
    if low < high:
        p = partition(data, low, high)
        quick_sort(data, low, p-1)
        quick_sort(data, p+1, high)


def partition(data, low, high):
    pivot = data[high]
    pivot_index = standard[pivot] if pivot in standard else -1
    i = low - 1
    for j in range(low, high):
        is_swap = False
        is_in_standard = data[j] in standard
        if pivot_index != -1 and is_in_standard:
            current_index = standard[data[j]]
            if current_index < pivot_index:
                is_swap = True
        elif pivot_index == -1 and is_in_standard:
            is_swap = True
        else:
            if data[j] < pivot:
                is_swap = True

        if is_swap:
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
    nums = input().split()
    m = int(nums[0])
    n = int(nums[1])
    arr1 = list()
    arr2 = list()
    for item in input().split():
        arr1.append(int(item))
    for item in input().split():
        arr2.append(int(item))

    standard = dict()
    for index in range(len(arr2)):
        standard[arr2[index]] = index

    quick_sort(arr1, 0, len(arr1)-1)

    for item in arr1:
        print(item, end=' ')
    t -= 1
