# Description
# Given an array of positive integers and many queries for divisibility.
# In every query Q[i], we are given an integer K ,
# we need to count all elements in the array which are perfectly divisible by K.
# Constraints:1<=T<=1001<=N,M<=1051<=A[i],Q[i]<=105
#
# Input
# The first line of input contains an integer T denoting the number of test cases.
# Then T test cases follow. Each test case consists of three lines.
# First line of each test case contains two integers N & M, second line contains N space separated array elements
# and third line contains M space separated queries.
#
# Output
# For each test case,In new line print the required count for each query Q[i].

# Sample Input 1
# 2
# 6 3
# 2 4 9 15 21 20
# 2 3 5
# 3 2
# 3 4 6
# 2 3
#
# Sample Output 1
# 3 3 2
# 2 2


def num_div(div_list, query_list):
    res = list()
    for item in query_list:
        cnt = 0
        for d in div_list:
            if d % item == 0:
                cnt += 1
        res.append(cnt)
    return res


t = int(input())
while t > 0:
    mn = input().split()
    n = int(mn[0])
    m = int(mn[1])

    div = [int(i) for i in input().split()]
    query = [int(i) for i in input().split()]

    result = num_div(div, query)
    for i in range(len(result)):
        if i == len(result)-1:
            print(result[i])
        else:
            print(result[i], end=' ')

    t -= 1
