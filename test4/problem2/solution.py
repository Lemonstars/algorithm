# Description
# Mike is a lawyer with the gift of photographic memory. He is so good with it that he can tell you all the numbers
# on a sheet of paper by having a look at it without any mistake. Mike is also brilliant with subsets so he thought of
# giving a challenge based on his skill and knowledge to Rachael. Mike knows how many subset are possible in an array
# of N integers. The subsets may or may not have the different sum. The challenge is to find the maximum sum produced
# by any subset under the condition:
# The elements present in the subset should not have any digit in common.
# Note: Subset {12, 36, 45} does not have any digit in common and Subset {12, 22, 35} have digits in common.
# Rachael find it difficult to win the challenge and is asking your help. Can you help her out
# in winning this challenge?
#
# Input
# First Line of the input consist of an integer T denoting the number of test cases.
# Then T test cases follow. Each test case consist of a numbe N denoting the length of the array.
# Second line of each test case consist of N space separated integers denoting the array elements.
#
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 100
# 1 <= array elements <= 100000
#
# Output
# Corresponding to each test case, print output in the new line.
#

# Sample Input 1
#
# 1
# 3
# 12 22 35
# Sample Output 1
#
# 57


def get_mask(x):
    res = 0
    while x > 0:
        d = x % 10
        res |= (1 << d)
        x //= 10
    return res


def solve(nums):
    _size = 1 << 10
    dp = [0 for _ in range(_size)]
    for num in nums:
        mask = get_mask(num)
        for bit in range(_size-1, -1, -1):
            if bit & mask == mask:
                dp[bit] = max(dp[bit], dp[bit ^ mask] + num)

    print(max(dp))


t = int(input())
while t > 0:
    n = int(input())
    num_str = input().split()
    num = [int(i) for i in num_str]
    solve(num)
    t -= 1
