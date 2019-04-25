# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
#
# 注意:
# 不能使用代码库中的排序函数来解决这道题。
#
# 示例:
# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]
# 进阶：
#
# 一个直观的解决方案是使用计数排序的两趟扫描算法。
# 首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
# 你能想出一个仅使用常数空间的一趟扫描算法吗？
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red_idx, white_idx, blue_idx = 0, 0, 0
        n = len(nums)

        for i in range(n):
            c = nums.pop(i)
            if c == 0:
                nums.insert(red_idx, c)
                red_idx += 1
                white_idx += 1
                blue_idx += 1
            elif c == 1:
                nums.insert(white_idx, c)
                white_idx += 1
                blue_idx += 1
            else:
                nums.insert(blue_idx, c)
                blue_idx += 1


s = Solution()
arr = [2, 0, 2, 1, 1, 0]
s.sortColors(arr)
print(arr)


