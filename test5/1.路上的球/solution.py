# Description
#
# There are two parallel roads, each containing N and M buckets, respectively. Each bucket may contain some balls.
# The buckets on both roads are kept in such a way that they are sorted according to the number of balls in them.
# Geek starts from the end of the road which has the bucket with a lower number of balls(i.e. if buckets are sorted
# in increasing order, then geek will start from the left side of the road). The geek can change the road only at the
# point of intersection(which means, buckets with the same number of balls on two roads). Now you need to help Geek to
# collect the maximum number of balls.
#
# Input
# The first line of input contains T denoting the number of test cases. The first line of each test case contains two
# integers N and M, denoting the number of buckets on road1 and road2 respectively. 2nd line of each test case contains
# N integers, number of balls in buckets on the first road. 3rd line of each test case contains M integers, number of
# balls in buckets on the second road.
#
# Constraints:1<= T <= 1000，1<= N <= 10^3，1<= M <=10^3，0<= A[i],B[i]<=10^6
#
# Output
# For each test case output a single line containing the maximum possible balls that Geek can collect.
#
# Sample Input 1
# 1
# 5 5
# 1 4 5 6 8
# 2 3 4 6 9
#
# Sample Output 1
# 29


def solve(arr1, arr2, len1, len2):
    pre_i, pre_j = 0, 0
    i, j = 0, 0
    count = 0

    while i < len1 or j < len2:
        same = False
        while i < len1 and j < len2 and arr1[i] != arr2[j]:
            if arr1[i] < arr2[j]:
                i += 1
            else:
                j += 1

            if i < len1 and j < len2 and arr1[i] == arr2[j]:
                same = True

        if same:
            sum1 = sum(arr1[pre_i:i+1])
            sum2 = sum(arr2[pre_j:j+1])
        else:
            sum1 = sum(arr1[pre_i:len1])
            sum2 = sum(arr2[pre_j:len2])

        count += max(sum1, sum2)
        if not same:
            return count

        pre_i, pre_j = i + 1, j + 1
        i, j = pre_i, pre_j

    return count


t = int(input())
t = 1
while t > 0:
    n, m = map(int, input().split())
    road1 = [int(i) for i in input().split()]
    road2 = [int(i) for i in input().split()]

    print(solve(road1, road2, n, m))

    t -= 1
