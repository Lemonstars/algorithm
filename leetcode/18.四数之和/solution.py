# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
# 使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
# 注意：
# 答案中不可以包含重复的四元组。
#
# 示例：
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]


class Solution:
    def fourSum(self, nums, target):
        length = len(nums)
        nums.sort()
        res = list()
        for i in range(length-3):
            if i != 0 and nums[i - 1] == nums[i]:
                continue
            for j in range(length-1, i+1, -1):
                if j != length - 1 and nums[j + 1] == nums[j]:
                    continue

                i_val = nums[i]
                j_val = nums[j]
                left = i + 1
                right = j - 1
                while left < right:
                    if left != i + 1 and nums[left - 1] == nums[left]:
                        left += 1
                        continue
                    elif right != j - 1 and nums[right + 1] == nums[right]:
                        right -= 1
                        continue

                    current_val = i_val + j_val + nums[left] + nums[right]
                    if current_val == target:
                        res.append([i_val, nums[left], nums[right], j_val])
                        left += 1
                    elif current_val < target:
                        left += 1
                    else:
                        right -= 1
        return length


s = Solution()
print(s.fourSum([-4, -3, -2, -1, 0, 0, 1, 2, 3, 4], 0))
