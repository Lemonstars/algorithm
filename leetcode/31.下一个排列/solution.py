# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
# 必须原地修改，只允许使用额外常数空间。
#
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


class Solution:
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    def nextPermutation(self, nums):
        length = len(nums)
        if length == 1:
            return

        for i in range(length - 1, -1, -1):
            current = nums[i]
            if current >= nums[-1]:
                for j in range(i + 1, length, 1):
                    nums[j-1] = nums[j]
                nums[-1] = current
            else:
                target = i
                while current >= nums[target]:
                    target += 1
                nums[i], nums[target] = nums[target], nums[i]
                break


s = Solution()
n = [1, 3, 4, 7, 5, 3, 2, 1]
s.nextPermutation(n)
print(n)
