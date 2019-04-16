import sys


def solve(start, cur_pos, remain, cur_cost, min_cost):
    if not remain and cur_cost < min_cost:
        min_cost = cur_cost
        return min_cost

    for city in remain:
        if (len(remain) != 1 and city != start) or len(remain) == 1:
            remain.remove(city)
            min_cost = solve(start, city, remain, cur_cost + cost[cur_pos][city], min_cost)
            remain.add(city)

    return min_cost


n = int(sys.stdin.readline().strip())
cost = list()
for line in sys.stdin:
    values = list(map(int, line.split()))
    cost.append(values)

remain = set()
for i in range(n):
    remain.add(i)
print(solve(0, 0, remain, 0, sys.maxsize))
