import sys

n = int(sys.stdin.readline().strip())
weapon = list(map(int, sys.stdin.readline().strip().split()))
money = list(map(int, sys.stdin.readline().strip().split()))

count = 0
my_weapon = 0
for i in range(n):
    if my_weapon < weapon[i]:
        count += money[i]
        my_weapon += weapon[i]
print(count)
