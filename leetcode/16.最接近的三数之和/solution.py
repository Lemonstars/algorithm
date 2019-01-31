# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，
# 使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).


class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        length = len(nums)

        for i in range(length-2):
            this_num = nums[i]
            left = i + 1
            right = length - 1

            while left < right:
                current_sum = this_num + nums[left] + nums[right]
                if current_sum == target:
                    return target
                else:
                    if abs(current_sum - target) < abs(res - target):
                        res = current_sum

                    if current_sum < target:
                        left += 1
                    else:
                        right -= 1
        return res


s = Solution()
print(s.threeSumClosest([-1, 2, 1, -4], 1))
