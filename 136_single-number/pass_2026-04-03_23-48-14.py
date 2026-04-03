# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 136 — single-number
# Status   : Accepted ✅
# Date     : 2026-04-03 23:48:14
# Cases    : 61/61
# Runtime  : 0 ms (beats 100%)
# Memory   : 21 MB (beats 96.49%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            ans ^= x
        return ans
# @lc code=end

