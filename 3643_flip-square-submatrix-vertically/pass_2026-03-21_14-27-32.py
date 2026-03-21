# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 3643 — flip-square-submatrix-vertically
# Status   : Accepted ✅
# Date     : 2026-03-21 14:27:32
# Cases    : 674/674
# Runtime  : 7 ms (beats 1.01%)
# Memory   : 19.4 MB (beats 99.14%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from typing import List, Optional, Dict, Tuple
from collections import defaultdict, deque
#
# @lc app=leetcode id=3643 lang=python3
#
# [3643] Flip Square Submatrix Vertically
#

# @lc code=start
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        swaps = k//2
        j = x + k - 1
        for i in range(swaps):
            grid[x+i][y:y+k], grid[j-i][y:y+k] = grid[j-i][y:y+k], grid[x+i][y:y+k]
        return grid

# @lc code=end

