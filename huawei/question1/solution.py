# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))

#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         for v in values:
#             ans += v
#     print(ans)

import sys

line = sys.stdin.readline().strip().split()
n = int(line[0])
arr = list()
for item in line[1:]:
    arr.append(item)

res = list()
for item in arr:
    length = len(item)
    if length <= 8:
        gap = 8 - length
        res.append(item+'0'*gap)
    else:
        i = 8
        while i < length:
            res.append(item[i-8: i])
            i += 8

        reminder = length % 8
        if reminder != 0:
            res.append(item[length-reminder: length] + '0'*(8-reminder))

res.sort()
for i in range(len(res)):
    if i == len(res) - 1:
        print(res[i])
    else:
        print(res[i], end=' ')