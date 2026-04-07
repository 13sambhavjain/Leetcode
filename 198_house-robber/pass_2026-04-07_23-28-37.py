# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 198 — house-robber
# Status   : Accepted ✅
# Date     : 2026-04-07 23:28:37
# Cases    : 
# Runtime  : Runtime (beats 0%)
# Memory   : ms (beats Beats%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        nums[-3] += nums[-1]
        for i in range(n-4, -1, -1):
            nums[i] += max(nums[i+2], nums[i+3])
        return max(nums[0], nums[1])
# @lc code=end

