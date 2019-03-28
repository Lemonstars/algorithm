def horspool(tet, pat):
    n = len(tet)
    m = len(pat)
    if n < m:
        return [-1]

    # 对于文本中的字符ch，考察模式中前(m-1)个字符与其关系
    # 在完全匹配的情况下，右移距离分情况如下:
    # 1. ch在模式中未出现，则移动距离未模式长度m
    # 2. ch在模式中出现，只出现在前(m-1)个字符中，移动模式中最右侧该字符到最后一个字符的距离
    # 3. ch在模式中出现，出现在最后一个字符，且前(m-1)个字符没有出现，移动模式长度m
    # 4. ch在模式中出现，出现在最后一个字符，且在前(m-1)个字符中出现，移动模式中最右侧该字符到最后一个字符的距离
    # 该四种情况，1、3可视为一组：前(m-1)个字符中没有ch，2、4视为另一组
    shift_dict = dict()
    for i in range(m-1):
        shift_dict[pat[i]] = i

    for k in shift_dict.keys():
        shift_dict[k] = (m-1) - shift_dict[k]

    def get_shirt_num(ch):
        if ch not in shift_dict:
            return m

        return shift_dict[ch]

    res = list()
    j = m-1
    while j < n:
        match = True
        for t in range(j, j-m, -1):
            if tet[t] != pat[t-(j-m+1)]:
                match = False
                break

        if match:
            res.append(j-m+1)
            j += 1
        else:
            j += get_shirt_num(tet[j])

    return res


text = 'THIS IS A TEST TEXT'
pattern = 'TEST'
print(horspool(text, pattern))
