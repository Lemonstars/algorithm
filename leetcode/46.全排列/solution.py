# 给定一个没有重复数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


class Solution:
    def permute(self, nums):
        cur_res = []
        all_res = []
        self.solve(nums, cur_res, all_res)
        return all_res

    def solve(self, nums, cur_res, all_res):
        if len(nums) == 1:
            cur_res.append(nums[0])
            all_res.append(cur_res)
            return

        for i in range(len(nums)):
            res_copy = cur_res.copy()
            res_copy.append(nums[i])
            num_copy = nums.copy()
            del num_copy[i]
            self.solve(num_copy, res_copy, all_res)


s = Solution()
print(s.permute([1, 2, 3]))
