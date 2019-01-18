# 字符串1
# Description
# Given a string ‘str’ of digits, find length of the longest substring of ‘str’,
# such that the length of the substring is 2k digits and sum of left k digits is equal to the sum of right k digits.
#
# Input
# 输入第一行是测试用例的个数，后面每一行表示一个数字组成的字符串，例如："123123"
#
# Output
# 输出找到的满足要求的最长子串的长度。例如，给定的例子长度应该是 6。每行对应一个用例的结果。

# Sample Input 1
# 1
# 1538023
#
# Sample Output 1
# 4


def len_of_max_sub(digit):
    max_len = 0
    n = len(digit)
    for i in range(n-1):
        left_index = i
        right_index = i+1
        left_sum = 0
        right_sum = 0
        while left_index >= 0 and right_index <= n-1:
            left_sum += int(digit[left_index])
            right_sum += int(digit[right_index])

            if left_sum == right_sum and right_index-left_index+1 > max_len:
                max_len = right_index - left_index + 1

            left_index -= 1
            right_index += 1

    return max_len


t = int(input())
while t > 0:
    s = input()
    print(len_of_max_sub(s))
    t -= 1
