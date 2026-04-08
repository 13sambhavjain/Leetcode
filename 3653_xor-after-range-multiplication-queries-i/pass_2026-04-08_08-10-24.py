# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 3653 — xor-after-range-multiplication-queries-i
# Status   : Accepted ✅
# Date     : 2026-04-08 08:10:24
# Cases    : 999/999
# Runtime  : 1592 ms (beats 49.93%)
# Memory   : 20 MB (beats 79.94%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from typing import List, Optional, Dict, Tuple
from collections import defaultdict, deque
#
# @lc app=leetcode id=3653 lang=python3
#
# [3653] XOR After Range Multiplication Queries I
#

# @lc code=start
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 1000000007
        for l, r, k, v in queries:
            for i in range(l, r+1, k):
                nums[i] = (nums[i]*v)%MOD
        ans = 0
        for x in nums:
            ans ^= x
        return ans
# @lc code=end

