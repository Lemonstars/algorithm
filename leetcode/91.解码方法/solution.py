# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
#
# 示例 1:
# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
#
# 示例 2:
# 输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6)


class Solution:

    def numDecodings(self, s: str) -> int:
        length = len(s)

        if length == 0:
            return 0

        if length == 1:
            return 0 if s == '0' else 1

        if s[0] == '0':
            return 0

        i, pre, cur = 2, 1, -1
        if s[1] == '0':
            if s[0] == '1' or s[0] == '2':
                cur = 1
            else:
                return 0
        else:
            if length == 2:
                return 2 if (s[0] == '1' and '0' < s[1] <= '9') or (s[0] == '2' and '0' < s[1] <= '6') else 1

            if s[2] == '0':
                if (s[1] == '1') or (s[1] == '2'):
                    cur = 1
                    i = 3
                else:
                    return 0
            else:
                cur = 2 if (s[0] == '1' and '0' < s[1] <= '9') or (s[0] == '2' and '0' < s[1] <= '6') else 1

        while i < length:
            if s[i] == '0':
                return 0

            if (i + 1 < length) and ((s[i] == '1' and s[i+1] == '0') or (s[i] == '2' and s[i+1] == '0')):
                pre = cur
                i += 2
            elif (s[i-1] == '1' and '0' < s[i] <= '9') or (s[i-1] == '2' and '0' < s[i] <= '6'):
                pre, cur = cur, pre + cur
                i += 1
            else:
                pre = cur
                i += 1

        return cur


s = Solution()
print(s.numDecodings('20'))
