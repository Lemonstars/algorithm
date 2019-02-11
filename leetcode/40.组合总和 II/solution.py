# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用一次。
#
# 说明：
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。
#
# 示例 1:
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
#
# 示例 2:
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
#   [1,2,2],
#   [5]
# ]


class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        all_res = list()
        self.solve(candidates, target, 0, [], all_res)
        return all_res

    def solve(self, num, target, start, cur, all):
        i = start
        length = len(num)
        while start <= i < length:
            current_num = num[i]
            if current_num > target:
                break
            else:
                cur_copy = cur.copy()
                cur_copy.append(current_num)

                if current_num == target:
                    all.append(cur_copy)
                    break
                else:
                    self.solve(num, target - current_num, i + 1, cur_copy, all)
                    while i < len(num) and num[i] == current_num:
                        i += 1


s = Solution()
print(s.combinationSum2([2,5,2,1,2], 5))
