# Description
# Satish wants to prepare for tommorow's exam. He knows the distribution of marks for the subject along with time to
# learn the concepts.You are given remaining time for the exam along with marks for each topic and passing marks for
# the subject.Find the max marks Satish can attain by studing max no of topic in max no hours not excedding (p) .
#
# Input
# The first line of input contains the number of test cases t.The first line of each testcase contains the no of
# topics(n), time remaining for exam(h) in hour and passing marks(p).Each 'n' lines contain
# u(time to learn topic) and v(weight age of topic in exam) .
#
# Output
# For each test case print "YES" along with time taken or "NO".
#
# Constraints:
# 1<=t<=100
# 1<=n<=300
# 1<=h<=150
# 1<=p<=35
# 1<=u,v<=25
#
# Sample Input 1
#
# 1
# 5 40 21
# 12 10
# 16 10
# 20 10
# 24 10
# 8 3
# Sample Output 1
#
# YES 36


def solve(n, h, p, mark, time):
    dp = [[0 for _ in range(h+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, h+1):
            if j >= time[i-1]:
                dp[i][j] = max(mark[i-1] + dp[i-1][j-time[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    if dp[n][h] < p:
        print('NO')
        return

    ti = 0
    i, j = n, h
    while i != 0 and j != 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            ti += time[i-1]
            j -= time[i-1]
            i -= 1

    print('YES ' + str(ti))


t = int(input())
while t > 0:
    n, h, p = map(int, input().split())
    time = list()
    mark = list()
    m = n
    while m > 0:
        u, v = map(int, input().split())
        time.append(u)
        mark.append(v)
        m -= 1

    solve(n, h, p, mark, time)

    t -= 1

