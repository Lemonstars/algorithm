# Description
# Given n Magnets which are placed linearly, with each magnet to be considered as of point object.
# Each magnet suffers force from its left sided magnets such that they repel it to the right and vice versa.
# All forces are repulsive. The force being equal to the distance (1/d , d being the distance).
# Now given the positions of the magnets, the task to find all the points along the linear line where net force is ZERO.
# Note: Distance have to be calculated with precision of 0.0000000000001.
# Constraints:1<=T<=100,1<=N<=100,1<=M[]<=1000
#
# Input
# The first line of input contains an integer T denoting the no of test cases.
# Then T test cases follow. The second line of each test case contains an integer N.
# Then in the next line are N space separated values of the array M[], denoting the positions of the magnet.
#
# Output
# For each test case in a new line print the space separated points
# having net force zero till precised two decimal places.

# Sample Input 1
# 2
# 2
# 1 2
# 4
# 0 10 20 30
#
# Sample Output 1
# 1.50
# 3.82 15.00 26.18


t = int(input())
while t > 0:
    n = int(input())
    data = [int(i) for i in input().split()]
    res = list()

    for index in range(n-1):
        start = data[index]
        end = data[index+1]
        while start <= end:
            mid = (start + end) / 2

            judge = 0
            for item in data:
                judge += 1 / (item - mid)

            if abs(judge) < 0.0001:
                res.append(mid)
                break
            elif judge < 0:
                start = mid
            else:
                end = mid

    res_len = len(res)
    for index in range(res_len):
        if index == res_len - 1:
            print('%.2f' % res[index])
        else:
            print('%.2f' % res[index], end=' ')

    t -= 1
