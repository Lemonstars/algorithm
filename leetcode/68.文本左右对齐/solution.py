# 给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。
# 你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。
# 要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
# 文本的最后一行应为左对齐，且单词之间不插入额外的空格。
#
# 说明:
# 单词是指由非空格字符组成的字符序列。
# 每个单词的长度大于 0，小于等于 maxWidth。
# 输入单词数组 words 至少包含一个单词。
# 示例:
#
# 输入:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# 输出:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
#
# 示例 2:
# 输入:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# 输出:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# 解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
#      因为最后一行应为左对齐，而不是左右两端对齐。
#      第二行同样为左对齐，这是因为这行只包含一个单词。
#
# 示例 3:
# 输入:
# words = ["Science","is","what","we","understand","well","enough","to","explain",
#          "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# 输出:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        n = len(words)
        res = list()

        new_line = True
        last_num = maxWidth
        this_line = list()

        i = 0
        while i < n:
            this_len = len(words[i])

            if new_line:
                new_line = False
                last_num -= this_len
                if i == n-1:
                    res.append(words[i] + ' ' * last_num)
                else:
                    this_line.append(words[i])

                i += 1
            else:
                if last_num > this_len:
                    last_num -= (this_len + 1)
                    this_line.append(words[i])

                    if i == n - 1:
                        mid_str = ' '.join(this_line)
                        mid_str += ' ' * (maxWidth - len(mid_str))
                        res.append(mid_str)

                    i += 1
                else:
                    ch_sum = sum(map(lambda p: len(p), this_line))

                    num = len(this_line)
                    if num == 1:
                        res.append(this_line[0] + ' ' * (maxWidth - ch_sum))
                    else:
                        blank = maxWidth - ch_sum
                        j = 1
                        while blank > 0:
                            this_line[j] = ' ' + this_line[j]
                            j += 1
                            if j == num:
                                j = 1

                            blank -= 1

                        res.append(''.join(this_line))

                    new_line = True
                    last_num = maxWidth
                    this_line.clear()

        return res


s = Solution()
print(s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
