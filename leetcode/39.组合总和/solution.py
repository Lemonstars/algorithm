# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。
#
# 示例 1:
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
#   [7],
#   [2,2,3]
# ]
#
# 示例 2:
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]


class Solution:

    def combinationSum(self, candidates, target):
        candidates.sort()
        current = list()
        all_res = list()
        self.solve(candidates, target, current, 0, all_res)
        return all_res

    def solve(self, candidates, target, cur, start, all_res):
        for i in range(start, len(candidates)):
            new_target = target - candidates[i]
            if new_target < 0:
                break
            else:
                cur_copy = cur.copy()
                cur_copy.append(candidates[i])

                if new_target == 0:
                    all_res.append(cur_copy)
                    break
                else:
                    self.solve(candidates, new_target, cur_copy, i, all_res)


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))
