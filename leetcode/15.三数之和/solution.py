# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
# 使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
#
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


class Solution:
    def threeSum(self, nums):
        length = len(nums)
        if length < 3:
            return []

        sort_num = sorted(nums)
        if sort_num[length-1] < 0 or sort_num[0] > 0:
            return []

        num_dict = dict()
        for i in range(length):
            num_dict[sort_num[i]] = i

        res = list()
        for i in range(length - 2):
            if i != 0 and sort_num[i] == sort_num[i - 1]:
                continue
            for j in range(i+1, length - 1):
                if j != i+1 and sort_num[j] == sort_num[j - 1]:
                    continue
                third_num = -(sort_num[i] + sort_num[j])
                if third_num in num_dict and num_dict[third_num] > j:
                    res.append([sort_num[i], sort_num[j], third_num])

        return res


s = Solution()
print(s.threeSum([0, 0, 0, 0]))
