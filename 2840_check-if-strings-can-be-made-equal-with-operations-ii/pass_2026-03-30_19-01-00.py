# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 2840 — check-if-strings-can-be-made-equal-with-operations-ii
# Status   : Accepted ✅
# Date     : 2026-03-30 19:01:00
# Cases    : 
# Runtime  : Runtime (beats 50%)
# Memory   : ms (beats Beats%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import collections
#
# @lc app=leetcode id=2840 lang=python3
#
# [2840] Check if Strings Can be Made Equal With Operations II
#

# @lc code=start
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return collections.Counter(s1[::2]) == collections.Counter(s2[::2]) and collections.Counter(s1[1::2]) == collections.Counter(s2[1::2])
        raise NotImplementedError
        
# @lc code=end