# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 119 — pascals-triangle-ii
# Status   : Accepted ✅
# Date     : 2026-03-18 09:10:18
# Cases    : 34/34
# Runtime  : 1 ms (beats 13.26%)
# Memory   : 19.4 MB (beats 51.04%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from typing import List, Optional, Dict, Tuple
from collections import defaultdict, deque

#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def helper(self, row: int):
        if row == 0:
            return [1]
        prev = self.helper(row-1)
        for i in range(1, len(prev)):
            prev[i-1] += prev[i]
        return [1] + prev

    def getRow(self, rowIndex: int) -> List[int]:
        return self.helper(rowIndex)
# @lc code=end