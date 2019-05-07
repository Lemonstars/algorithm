import sys

m, n = map(int, sys.stdin.readline().split())
arr = list()
for i in range(n):
    num = int(sys.stdin.readline())
    arr.append(num)

arr.sort()
if 1 not in arr:
    print(-1)
else:
    count = 0
    a = m-1
    for i in range(n-1, -1, -1):
        b = arr[i]
        count += a // b
        a = b - 1
    print(count)
