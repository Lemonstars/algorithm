# 给出一个区间的集合，请合并所有重叠的区间。
#
# 示例 1:
#
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2:
#
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):

    def partion(self, intervals, lo, hi):
        pivot = intervals[hi]
        i = lo - 1
        for j in range(lo, hi):
            if intervals[j].start < pivot.start:
                i += 1
                intervals[i], intervals[j] = intervals[j], intervals[i]
        intervals[i+1], intervals[hi] = intervals[hi], intervals[i+1]
        return i+1

    def quick_sort(self, intervals, lo, hi):
        if lo < hi:
            p = self.partion(intervals, lo, hi)
            self.quick_sort(intervals, lo, p-1)
            self.quick_sort(intervals, p+1, hi)

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        n = len(intervals)
        if n == 0:
            return []

        # self.quick_sort(intervals, 0, n-1)
        intervals.sort(key=lambda x:x.start)

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


i1 = Interval(1, 3)
i2 = Interval(2, 6)
i3 = Interval(8, 10)
i4 = Interval(15, 18)
target = [i1, i2, i3, i4]
s = Solution()
res = s.merge(target)
for i in res:
    print(str(i.start) + ' ' + str(i.end))

