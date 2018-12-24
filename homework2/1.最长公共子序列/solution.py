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

    return L[m][n]


data1 = '1A2BD3G4H56JK'
data2 = '23EFG4I5J6K7'
print(LCS(data1, data2))


