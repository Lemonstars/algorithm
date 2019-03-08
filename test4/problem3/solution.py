# Description
# Let's define a Series Whose recurrence formula is as follows :
#
# C(n)= 3C(i-1) + 4C(i-2) + 5C(i-3) + 6C(i-4)
# C(0)= 2
# C(1)= 0
# C(2)= 1
# C(3)= 7
#
# Now based on this Series a Matrix Mi,j of size nn is to be formed.The top left cell is(1,1) and the
# bottom right corner is (n,n). Each cell (i,j) of the Matrix contains either 1 or 0.
# If C( (i*j)^3 ) is odd, Mi,j is 1, otherwise, it's 0.Count the total number of ones in the Matrix.
#
# Input
# First Line Of the input will contain an integer 'T'- the number of test cases .
# Each of the next 'T' lines consists of an integer 'n'.-denoting the size of the matrix.
#
# Constraints :
# 1 ≤ T ≤ 1000
# 1 ≤ n ≤ 1000
#
# Output
# For each test case, output a single Integer -the taste value fo the dish of size-n*n

# Sample Input 1
# 1
# 2
# Sample Output 1
# 0


def solve(n):
    c = [0 for _ in range(pow(n, 6) + 1)]
    c[0], c[1], c[2], c[3] = 2, 0, 1, 7
    for i in range(4, pow(n, 6) + 1):
        c[i] = 3 * c[i-1] + 4 * c[i-2] + 5*c[i-3] + 6 * c[i-4]

    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            target = c[pow((i+1)*(j+1), 3)]
            if target % 2 == 1:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0

    print(sum(sum(row)for row in matrix))


t = int(input())
while t > 0:
    n = int(input())
    solve(n)
    t -= 1
