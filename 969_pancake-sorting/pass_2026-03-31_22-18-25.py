# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 969 — pancake-sorting
# Status   : Accepted ✅
# Date     : 2026-03-31 22:18:25
# Cases    : 
# Runtime  : Runtime (beats 0%)
# Memory   : ms (beats Beats%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# @lc app=leetcode id=969 lang=python3
#
# [969] Pancake Sorting
#

# @lc code=start
class Solution:
    @functools.cache
    def numTrees(self, n: int) -> int:
        if n < 2:
            return 1
        if n == 2: return 2
        ans = 0
        for i in range(n):
            ans += self.numTrees(i)*self.numTrees(n-1-i)
        return ans
        
        
# @lc code=end

