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
        nums.sort()
        length = len(nums)

        ij_dict = dict()
        for i in range(length - 1, 0, -1):
            if i != length - 1 and nums[i + 1] == nums[i]:
                continue
            for j in range(i-1, -1, -1):
                if j != i - 1 and nums[j + 1] == nums[j]:
                    continue
                ij_sum = nums[i] + nums[j]
                if ij_sum not in ij_dict:
                    ij_dict[ij_sum] = [(j, i)]
                else:
                    ij_dict[ij_sum].append((j, i))

        res = list()
        for i in range(length - 1):
            if i != 0 and nums[i - 1] == nums[i]:
                continue
            for j in range(i+1, length):
                if j != i+1 and nums[j - 1] == nums[j]:
                    continue
                m = target - nums[i] - nums[j]
                if m in ij_dict:
                    for item in ij_dict[m]:
                        if item[0] > j:
                            res.append([nums[i], nums[j], nums[item[0]], nums[item[1]]])
        return res


s = Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
