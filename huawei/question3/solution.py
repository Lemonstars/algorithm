import sys
import copy


def backtrace(n, m, cur, end, visit, count):
    visit[cur[0]][cur[1]] = True
    if cur[0] == end[0] and cur[1] == end[1]:
        return count + 1

    x, y = cur[0], cur[1]
    to_visit = list()
    if x+1 < n and not(visit[x+1][y]) and map_matrix[x+1][y] > map_matrix[x][y]:
        to_visit.append((x+1, y))

    if x-1 >= 0 and not(visit[x-1][y]) and map_matrix[x-1][y] > map_matrix[x][y]:
        to_visit.append((x-1, y))

    if y+1 < m and not(visit[x][y+1]) and map_matrix[x][y+1] > map_matrix[x][y]:
        to_visit.append((x, y+1))

    if y-1 >= 0 and not(visit[x][y-1]) and map_matrix[x][y-1] > map_matrix[x][y]:
        to_visit.append((x, y-1))

    for item in to_visit:
        visit_copy = copy.deepcopy(visit)
        count = backtrace(n, m, item, end, visit_copy, count)

    return count


line = sys.stdin.readline().strip().split()
n = int(line[0])
m = int(line[1])

map_matrix = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    line = sys.stdin.readline().split()
    for j in range(m):
        map_matrix[i][j] = int(line[j])

ab = sys.stdin.readline().strip().split()
a = int(ab[0]), int(ab[1])
b = int(ab[2]), int(ab[3])

v = [[False for _ in range(m)] for _ in range(n)]

print(backtrace(n, m, a, b, v, 0))

