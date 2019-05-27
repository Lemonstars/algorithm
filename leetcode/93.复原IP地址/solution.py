# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
#
# 示例:
#
# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def traceback(idx: int, segment: int, cur: str):
            if segment == 4 and idx == n:
                res.append(cur)
                return

            for i in range(3):
                if idx + i < n and 0 <= int(s[idx:idx + i + 1]) <= 255:
                    if n - (idx + i + 1) <= (3 - segment) * 3:
                        if (i > 0 and s[idx] != '0') or i == 0:
                            traceback(idx + i + 1, segment + 1, cur + s[idx:idx + i + 1] + '.' if segment < 3 else cur + s[idx:idx + i + 1])

        res, n = list(), len(s)
        traceback(0, 0, '')

        return res


s = Solution()
print(s.restoreIpAddresses('25525511135'))










