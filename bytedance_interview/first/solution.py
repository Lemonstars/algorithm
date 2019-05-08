# coding=utf-8


def f(list1, list2):
    stack = list()
    i = 0
    j = 0
    len1 = len(list1)
    len2 = len(list2)

    if len1 != len2:
        return False

    if len1 == 0:
        return True

    while i < len1:
        stack.append(list1[i])

        while j < len2 and stack[-1] == list2[j]:
            del stack[-1]
            j += 1

        i += 1

    return not stack


print(f('123', '312'))
