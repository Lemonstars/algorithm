# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素

# 示例:
# 给定 nums = [2, 7, 11, 15], target = 9
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]


class Solution:
    def twoSum(self, nums, target):
        num_dict = dict()
        length = len(nums)
        for index in range(length):
            num = nums[index]
            target_num = target-num
            if target_num in num_dict:
                return num_dict[target_num], index
            else:
                num_dict[num] = index

        return -1, -1


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
