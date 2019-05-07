import sys

n = int(sys.stdin.readline().strip())
target = sys.stdin.readline().strip()

# stack = list()
# for item in target:
#     if not stack or stack[-1] == item:
#         stack.append(item)
#     else:
#         del stack[-1]
# print(len(stack))

count_0 = 0
count_1 = 0
for item in target:
    if item == '0':
        count_0 += 1
    else:
        count_1 += 1
print(abs(count_1-count_0))
