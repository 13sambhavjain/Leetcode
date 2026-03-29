# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 2839 — check-if-strings-can-be-made-equal-with-operations-i
# Status   : Accepted ✅
# Date     : 2026-03-29 13:24:58
# Cases    : 1003/1003
# Runtime  : 0 ms (beats 100%)
# Memory   : 19.4 MB (beats 15.79%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# @lc app=leetcode id=2839 lang=python3
#
# [2839] Check if Strings Can be Made Equal With Operations I
#

# @lc code=start
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return {s1[0], s1[2]} == {s2[0], s2[2]} and {s1[1], s1[3]} == {s2[1], s2[3]}
        
        
# @lc code=end

