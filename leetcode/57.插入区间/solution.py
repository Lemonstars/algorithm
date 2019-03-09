# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
#
# 示例 1:
# 输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出: [[1,5],[6,9]]
#
# 示例 2:
# 输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出: [[1,2],[3,10],[12,16]]
# 解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        n = len(intervals)
        if n == 0:
            return [newInterval]

        intervals.append(newInterval)
        i = n - 1
        while i >= 0:
            if newInterval.start < intervals[i].start:
                intervals[i+1] = intervals[i]
                i -= 1
            elif newInterval.start == intervals[i].start and newInterval.end <= intervals[i].end:
                intervals[i+1] = intervals[i]
                i -= 1
            else:
                break
        intervals[i+1] = newInterval

        res = list()
        res.append(intervals[0])
        for interval in intervals[1:]:
            if interval.start <= res[-1].end:
                if interval.end > res[-1].end:
                    new_interval = Interval(res[-1].start, interval.end)
                    del res[-1]
                    res.append(new_interval)
            else:
                res.append(interval)
        return res


i1 = Interval(1, 2)
i2 = Interval(3, 5)
i3 = Interval(6, 7)
i4 = Interval(8, 10)
i5 = Interval(12, 16)
lis = [i1, i2, i3, i4, i5]
a = Interval(4, 8)
s = Solution()
res = s.insert(lis, a)
for i in res:
    print(str(i.start) + ' ' + str(i.end))

