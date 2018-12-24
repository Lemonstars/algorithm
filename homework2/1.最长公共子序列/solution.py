# Description
# 给定两个字符串，返回两个字符串的最长公共子序列（不是最长公共子字符串），可能是多个。
#
# Input
# 输入为两行，一行一个字符串
#
# Output
# 输出如果有多个则分为多行，先后顺序不影响判断。

# Sample Input 1
# 1A2BD3G4H56JK
# 23EFG4I5J6K7
#
# Sample Output 1
# 23G456K
# 23G45JK


def LCS(str1, str2):
    m = len(str1)
    n = len(str2)
    L = [[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                L[i][j] = 1 + L[i-1][j-1]
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    return L


def getAllLCS(str1, str2, m, n):
    res = set()

    if m == 0 or n == 0:
        res.add('')
        return res

    if str1[m-1] == str2[n-1]:
        tmp = getAllLCS(str1, str2, m-1, n-1)
        for s in tmp:
            res.add(s + str1[m-1])
    else:
        if length[m-1][n] > length[m][n-1]:
            res = getAllLCS(str1, str2, m-1, n)
        elif length[m][n-1] > length[m-1][n]:
            res = getAllLCS(str1, str2, m, n-1)
        else:
            res = getAllLCS(str1, str2, m-1, n)
            for s in getAllLCS(str1, str2, m, n-1):
                res.add(s)

    return res


data1 = input()
data2 = input()
length = LCS(data1, data2)
all_res = getAllLCS(data1, data2, len(data1), len(data2))
for item in all_res:
    print(item)
