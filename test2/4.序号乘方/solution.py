# Description
# There are Infinite People Standing in a row, indexed from 1. A person having index 'i' has strength of (i*i).
# You have Strength 'P'. You need to tell what is the maximum number of People You can Kill With your Strength P.
# You can only Kill a person with strength 'X' if P >= 'X' and after killing him, Your Strength decreases by 'X'.
#
# Input
# First line contains an integer 'T' - the number of test cases,
# Each of the next 'T' lines contains an integer 'P'- Your Power.Constraints:1<=T<=100001<=P<=1000000000000000
#
# Output
# For each test case Output The maximum Number of People You can kill.

# Sample Input 1
# 1
# 14
#
# Sample Output 1
# 3


def num_of_kill(power):
    num = 0
    i = 1
    while True:
        power -= i*i

        if power >= 0:
            i += 1
            num += 1
        else:
            break
    return num


t = int(input())
while t > 0:
    p = int(input())
    print(num_of_kill(p))
    t -= 1