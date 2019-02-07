# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 你可以假设数组中无重复元素。
#
# 示例 1:
# 输入: [1,3,5,6], 5
# 输出: 2
#
# 示例 2:
# 输入: [1,3,5,6], 2
# 输出: 1
#
# 示例 3:
# 输入: [1,3,5,6], 7
# 输出: 4
#
# 示例 4:
# 输入: [1,3,5,6], 0
# 输出: 0


class Solution:
    def searchInsert(self, nums, target):
        if not nums:
            return 0

        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            number = nums[mid]

            if number == target:
                return mid
            elif number < target:
                if mid == hi:
                    return hi + 1
                else:
                    lo = mid + 1
            else:
                if mid == lo:
                    return lo
                else:
                    hi = mid - 1


s = Solution()
print(s.searchInsert([1,3,5,6], 2))