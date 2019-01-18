# Description
# Given a text txt[0..n-1] and a pattern pat[0..m-1],
# write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[].
# You may assume that n > m.
#
# Input
# 输入第一行是用例个数，后面一行表示一个用例；用例包括两部分，第一部分为给定文本，第二部分为搜索串，两部分使用","隔开。
#
# Output
# 每一个用例输出一行，每行按照找到的位置先后顺序排列，使用空格隔开

# Sample Input 1
# 2
# THIS IS A TEST TEXT,TEST
# AABAACAADAABAABA,AABA
#
# Sample Output 1
# 10
# 0 9 12


# todo
def kmp(text, patter):
    res = list()
    m = len(text)
    n = len(patter)
    for i in range(m-n+1):
        for j in range(n):
            if text[i+j] != patter[j]:
                break
            else:
                if j == n-1:
                    res.append(i)

    return res


t = int(input())
while t > 0:
    line = input().split(',')
    txt = line[0]
    pat = line[1]

    result = kmp(txt, pat)
    for k in range(len(result)):
        if k == len(result)-1:
            print(result[k])
        else:
            print(result[k], end=' ')

    t -= 1