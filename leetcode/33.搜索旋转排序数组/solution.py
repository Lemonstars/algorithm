# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
# 你可以假设数组中不存在重复的元素。
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 示例 1:
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
#
# 示例 2:
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1


class Solution:
    def search(self, nums, target):
        if len(nums) == 0:
            return -1

        return self.find(nums, target, 0, len(nums) - 1)

    def find(self, nums, target, start, end):
        if start > end:
            return -1

        if nums[start] <= nums[end]:
            return self.binary_search(nums, start, end, target)

        mid = (start + end) // 2
        if nums[mid] == target:
            return mid

        if nums[start] <= nums[mid]:
            if target < nums[mid]:
                if nums[end] < target:
                    return self.binary_search(nums, start, mid, target)
                else:
                    return self.find(nums, target, mid+1, end)
            else:
                return self.find(nums, target, mid+1, end)
        else:
            if target < nums[mid]:
                return self.find(nums, target, start, mid)
            else:
                if nums[end] >= target:
                    return self.binary_search(nums, mid+1, end, target)
                else:
                    return self.find(nums, target, start, mid)

    def binary_search(self, nums, start, end, target):
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return -1


s = Solution()
print(s.search([1, 3], 0))
print(s.search([4,5,6,7,0,1,2], 0))
