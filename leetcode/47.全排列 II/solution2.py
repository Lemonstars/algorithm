# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
#
# 示例:
#
# 输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]


class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        cur_res = list()
        all_res = list()
        self.solve(nums, cur_res, all_res)
        return all_res

    def solve(self, nums, cur_res, all_res):
        if len(nums) == 1:
            cur_res.append(nums[0])
            all_res.append(cur_res)
            return

        length = len(nums)
        for i in range(length):
            if i != 0 and nums[i-1] == nums[i]:
                continue

            res_copy = cur_res.copy()
            res_copy.append(nums[i])
            num_copy = nums.copy()
            del num_copy[i]
            self.solve(num_copy, res_copy, all_res)


s = Solution()
print(s.permuteUnique([3,3,0,3]))