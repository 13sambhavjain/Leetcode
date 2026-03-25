# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 3546 — equal-sum-grid-partition-i
# Status   : Accepted ✅
# Date     : 2026-03-25 08:03:39
# Cases    : 687/687
# Runtime  : 153 ms (beats 56.16%)
# Memory   : 44 MB (beats 55.48%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from typing import List, Optional, Dict, Tuple
from collections import defaultdict, deque
#
# @lc app=leetcode id=3546 lang=python3
#
# [3546] Equal Sum Grid Partition I
#

# @lc code=start
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        sums = set()
        tsum = 0
        for row in grid:
            tsum += sum(row)
            sums.add(tsum)
        if tsum&1:
            return False
        hsum = tsum//2
        if hsum in sums:
            return True
        sums.clear()
        tsum = 0
        for j in range(len(grid[0])):
            tsum += sum(grid[i][j] for i in range(len(grid)))
            sums.add(tsum)
        return hsum in sums

# @lc code=end

