# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 你的算法时间复杂度必须是 O(log n) 级别。
# 如果数组中不存在目标值，返回 [-1, -1]。
#
# 示例 1:
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
#
# 示例 2:
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]


class Solution:
    def searchRange(self, nums, target):
        low, high = -1, -1
        if not nums:
            return [low, high]

        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            number = nums[mid]
            if number == target:
                low = self.find(nums, target, lo, mid, True)
                high = self.find(nums, target, mid, hi, False)
                break
            elif number < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return [low, high]

    def find(self, nums, target, start, end, left):
        res = end if left else start
        index = start if left else end

        while abs(res-index) > 1:
            mid = (res + index) // 2
            if nums[mid] == target:
                res = mid
            elif nums[mid] < target:
                index = mid + 1
            else:
                index = mid - 1

        return index if nums[index] == target else res


s = Solution()
print(s.searchRange([5,7,7,8,8,10], 6))
