# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 70 — climbing-stairs
# Status   : Accepted ✅
# Date     : 2026-04-04 23:58:35
# Cases    : 
# Runtime  : Runtime (beats 0%)
# Memory   : ms (beats Beats%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    @functools.cache
    def helper(self, n: int) -> int:
        if n <= 3:
            return n
        return self.helper(n-1) + self.helper(n-2)
    def climbStairs(self, n: int) -> int:
        return self.helper(n)
# @lc code=end

