def solve(weight, value, W):
    # Space complexity: O(n^2)
    n = len(weight)
    res = [[0 for _ in range(W+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, W+1):
            if weight[i-1] > j:
                res[i][j] = res[i-1][j]
            else:
                res[i][j] = max(res[i-1][j], res[i-1][j-weight[i-1]]+value[i-1])

    for line in res:
        for item in line:
            print(item, end=' ')
        print()
    return res[n][W]


def solve2(weight, value, W):
    # Space complexity: O(n^2)
    n = len(weight)
    pre = [0 for _ in range(W+1)]
    cur = [0 for _ in range(W+1)]

    for i in range(1, n+1):
        for j in range(1, W+1):
            if weight[i-1] > j:
                cur[j] = pre[j]
            else:
                cur[j] = max(pre[j], pre[j-weight[i-1]]+value[i-1])
        print(cur)
        pre = cur.copy()

    return cur[W]


w = [2, 3, 4, 5]
v = [3, 4, 5, 6]
w_max = 8
print(solve(w, v, w_max))
print()
print(solve2(w, v, w_max))
