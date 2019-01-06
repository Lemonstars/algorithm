# Return all non-negative integers of length N such that the absolute difference
# between every two consecutive digits is K.
# Note that every number in the answer must not have leading zeros except for the number 0 itself.
# For example, 01 has one leading zero and is invalid, but 0 is valid.
# You may return the answer in any order.

# Example 1:
# Input: N = 3, K = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading zeroes.
# Example 2:
#
# Input: N = 2, K = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]


def nums_same_consec_diff(N, K):
    final_res = list()
    if N == 1:
        for i in range(0, 10):
            final_res.append(i)
        return final_res

    res = list()
    for i in range(1, 10 - K):
        res.append(i)
    for i in range(max(1, K, 10-K), 10):
        res.append(i)
    N -= 1

    tmp_res = list()
    while N > 0:
        tmp_res.clear()
        for item in res:
            reminder = item % 10
            if K != 0:
                if reminder + K <= 9:
                    tmp_res.append(item * 10 + reminder + K)
                if reminder - K >= 0:
                    tmp_res.append(item * 10 + reminder - K)
            else:
                tmp_res.append(item * 10 + reminder)
        res.clear()
        for i in tmp_res:
            res.append(i)
        N -= 1

    for i in res:
        final_res.append(i)
    return final_res


N = 3
K = 7
print(nums_same_consec_diff(N, K))
