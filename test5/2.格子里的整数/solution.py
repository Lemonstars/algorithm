# Description
#
# Given a square grid of size n, each cell of which contains integer cost which represents a cost to traverse through
# that cell, we need to find a path from top left cell to bottom right cell by which total cost incurred is minimum.
#
# Note : It is assumed that negative cost cycles do not exist in input matrix.
#
# Input
# The first line of input will contain number of test cases T. Then T test cases follow . Each test case contains 2
# lines.The first line of each test case contains an integer n denoting the size of the grid. Next line of each test
# contains a single line containing N*N space separated integers depecting cost of respective cell from (0,0) to (n,n).
#
# Constraints:1<=T<=50，1<= n<= 50
#
# Output
# For each test case output a single integer depecting the minimum cost to reach the destination.
#
# Sample Input 1
# 2
# 5
# 31 100 65 12 18 10 13 47 157 6 100 113 174 11 33 88 124 41 20 140 99 32 111 41 20
# 2
# 42 93 7 14
#
# Sample Output 1
# 327
# 63
import sys


def solve(matrix, n):
    x_inc = [-1, 1, 0, 0]
    y_inc = [0, 0, -1, 1]

    cost = [[sys.maxsize // 2 for _ in range(n)] for _ in range(n)]
    cost[0][0] = matrix[0][0]
    point_set = set()
    point_set.add((cost[0][0], 0, 0))

    while point_set:
        point_min = min(point_set)
        c, i, j = point_min
        point_set.remove(point_min)

        for k in range(4):
            x_new = i + x_inc[k]
            y_new = j + y_inc[k]

            if 0 <= x_new < n and 0 <= y_new < n:
                if cost[x_new][y_new] > c + matrix[x_new][y_new]:
                    cost[x_new][y_new] = c + matrix[x_new][y_new]
                    point_set.add((cost[x_new][y_new], x_new, y_new))

    return cost[n-1][n-1]


t = int(input())
while t > 0:
    n = int(input())
    num = [[-1 for _ in range(n)] for _ in range(n)]
    m = 0

    num_str = input().split()
    for m in range(n * n):
        num[m // n][m % n] = int(num_str[m])

    print(solve(num, n))

    t -= 1
