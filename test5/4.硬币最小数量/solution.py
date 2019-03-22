# Description
# Given the list of coins of distinct denominations and total amount of money. Output the minimum number of coins
# required to make up that amount. Output -1 if that money cannot be made up using given coins. You may assume that
# there are infinite numbers of coins of each type.
#
# Input
# The first line contains 'T' denoting the number of test cases. Then follows description of test cases.
# Each cases begins with the two space separated integers 'n' and 'amount' denoting the total number of distinct
# coins and total amount of money respectively. The second line contains N space-separated integers A1, A2, ..., AN
# denoting the values of coins.
#
# Constraints:1<=T<=30，1<=n<=100，1<=Ai<=1000，1<=amount<=100000
#
# Output
# Print the minimum number of coins required to make up that amount or return -1 if it is impossible
# to make that amount using given coins.
#
# Sample Input 1
# 2
# 3 11
# 1 2 5
# 2 7
# 2 6
#
# Sample Output 1
# 3
# -1


def solve(target, num, count):
    if target < 0:
        return -1

    if target == 0:
        return count

    for i in range(len(num)-1, -1, -1):
        c = solve(target - num[i], num, count + 1)
        if c > 0:
            return c

    return -1


t = int(input())
while t > 0:
    n, amount = map(int, input().split())
    a = [int(i) for i in input().split()]

    print(solve(amount, a, 0))

    t -= 1
