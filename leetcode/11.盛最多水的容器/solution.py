# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
# 在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 说明：你不能倾斜容器，且 n 的值至少为 2。
#
# 示例:
# 输入: [1,8,6,2,5,4,8,3,7]
# 输出: 49


class Solution:

    """
    :type height: List[int]
    :rtype: int
    """
    def maxArea(self, height):
        area = 0
        i = 0
        j = len(height) - 1

        while i != j:
            cur_area = (j-i) * min(height[i], height[j])
            if cur_area > area:
                area = cur_area

            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return area


s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))