# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 495 — teemo-attacking
# Status   : Accepted ✅
# Date     : 2026-04-02 23:38:24
# Cases    : 40/40
# Runtime  : 0 ms (beats 100%)
# Memory   : 20.5 MB (beats 98.72%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# @lc app=leetcode id=495 lang=python3
#
# [495] Teemo Attacking
#

# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        start_time = timeSeries[0]
        for i in range(1, len(timeSeries)):
            if timeSeries[i] < (x := timeSeries[i-1] + duration):
                continue
            else:
                ans += x - start_time
                start_time = timeSeries[i]
        ans += timeSeries[-1] + duration - start_time
        return ans
# @lc code=end

