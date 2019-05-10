# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
#
# 说明:
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 示例:
#
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# 输出: [1,2,2,3,5,6]
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        if m == 0:
            for k in range(n):
                nums1[k] = nums2[k]
            return

        i, j = 0, 0
        while i < m + j and j < n:
            if nums1[i] < nums2[j]:
                i += 1
            else:
                for k in range(m + j - 1, i - 1, -1):
                    nums1[k+1] = nums1[k]
                nums1[i] = nums2[j]

                i += 1
                j += 1

        while j != n:
            nums1[i] = nums2[j]
            i += 1
            j += 1


s = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2,5,6]
s.merge(nums1, 3, nums2, 3)
print(nums1)
