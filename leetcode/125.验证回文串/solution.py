# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
#
# 示例 2:
# 输入: "race a car"
# 输出: false


class Solution:

    def isValiad(self, ch: str) -> bool:
        if ('0' <= ch <= '9') or ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
            return True

        return False

    def isEqual(self, ch1: str, ch2: str) -> bool:
        if ch1 == ch2:
            return True

        if (('a' <= ch1 <= 'z' and 'A' <= ch2 <= 'Z') or ('a' <= ch2 <= 'z' and 'A' <= ch1 <= 'Z')) \
                and (abs(ord(ch1) - ord(ch2))) == 32:
            return True

        return False

    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        if n == 0 or n == 1:
            return True

        lo, hi = 0, n - 1
        while lo < hi:
            if not self.isValiad(s[lo]):
                lo += 1
                continue

            if not self.isValiad(s[hi]):
                hi -= 1
                continue

            if self.isEqual(s[lo], s[hi]):
                lo += 1
                hi -= 1
                continue

            return False

        return True


s = Solution()
data = 'A man, a plan, a canal: Panama'
# data = 'race a car'
# data = '0P'
print(s.isPalindrome(data))