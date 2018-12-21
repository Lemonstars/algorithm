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


def first(arr, low, high, x, n):
    if high >= low:
        mid = low + (high - low) // 2;  # (low + high)/2;
        if (mid == 0 or x > arr[mid - 1]) and arr[mid] == x:
            return mid
        if x > arr[mid]:
            return first(arr, (mid + 1), high, x, n)
        return first(arr, low, (mid - 1), x, n)

    return -1


def sortAccording(A1, A2, m, n):
    temp = [0] * m
    visited = [0] * m

    for i in range(0, m):
        temp[i] = A1[i]
        visited[i] = 0

    temp.sort()
    ind = 0

    for i in range(0, n):
        f = first(temp, 0, m - 1, A2[i], m)
        if f == -1:
            continue
        j = f
        while j < m and temp[j] == A2[i]:
            A1[ind] = temp[j]
            ind = ind + 1
            visited[j] = 1
            j = j + 1

    for i in range(0, m):
        if visited[i] == 0:
            A1[ind] = temp[i]
            ind = ind + 1


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

    sortAccording(arr1, arr2, m, n)
    for item in arr1:
        print(item, end=' ')
    t -= 1
