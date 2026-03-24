# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 2906 — construct-product-matrix
# Status   : Failed ❌
# Date     : 2026-03-24 09:10:23
# ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
# Input    : long big numbers
# Expected : all 0's
# Got      : TLE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from typing import List, Optional, Dict, Tuple
from collections import defaultdict, deque
#
# @lc app=leetcode id=2906 lang=python3
#
# [2906] Construct Product Matrix
#

# @lc code=start
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        prod = 1
        n, m = len(grid), len(grid[0])
        for row in grid:
            for cell in row:
                prod *= cell
        ans = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j] = (prod//grid[i][j])%12345
        return ans
# @lc code=end

