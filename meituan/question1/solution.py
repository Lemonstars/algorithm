import sys

line = sys.stdin.readline().strip().split()
n, m = int(line[0]), int(line[1])

total = 0
appear_dict = dict()

matrix = [[-1 for _ in range(m)] for _ in range(n)]
for i in range(n):
    line = sys.stdin.readline().strip().split()
    for j in range(m):
        matrix[i][j] = int(line[j])
        total += matrix[i][j]

        if matrix[i][j] not in appear_dict:
            appear_dict[matrix[i][j]] = 1
        else:
            appear_dict[matrix[i][j]] += 1


res = 0
if total / matrix[0][0] == n * m:
    if m % 2 == 0:
        res = m // 2 * n
    else:
        single = True
        single_add = m // 2
        while n > 0:
            if single:
                res += single_add
            else:
                res += (single_add + 1)

            single = not single
            n -= 1
else:
    most1 = None
    most2 = None
    for key in appear_dict.keys():
        if most1 is None:
            most1 = (key, appear_dict[key])
        elif most2 is None:
            most2 = (key, appear_dict[key])
            if most2[1] > most1[1]:
                most1, most2 = most2, most1
        elif appear_dict[key] > most2[1]:
            most2 = (key, appear_dict[key])
            if most2[1] > most1[1]:
                most1, most2 = most2, most1

    most1, most2 = most1[0], most2[0]

    count1, count2 = 0, 0
    is_col_even = (m % 2 == 0)

    is_most = True
    for i in range(n):
        for j in range(m):
            if is_most and matrix[i][j] != most1:
                count1 += 1
            elif not is_most and matrix[i][j] != most2:
                count1 += 1

            if j != m-1 or (j == m-1 and not is_col_even):
                is_most = not is_most

    is_most = False
    for i in range(n):
        for j in range(m):
            if is_most and matrix[i][j] != most1:
                count2 += 1
            elif not is_most and matrix[i][j] != most2:
                count2 += 1

            if j != m-1 or (j == m-1 and not is_col_even):
                is_most = not is_most

    res = min(count1, count2)

print(res)