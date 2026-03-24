# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 2906 — construct-product-matrix
# Status   : Accepted ✅
# Date     : 2026-03-24 09:11:35
# Cases    : 1566/1566
# Runtime  : 723 ms (beats 13.24%)
# Memory   : 42.9 MB (beats 74.17%)
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
        zeroes = None
        for i in range(n):
            for j in range(m):
                if (x := (grid[i][j]%12345)) == 0:
                    if zeroes:
                        return [[0]*m for _ in range(n)]
                    zeroes = (i, j)
                else:
                    prod *= x
        ans = [[0]*m for _ in range(n)]
        if zeroes:
            ans[zeroes[0]][zeroes[1]] = prod%12345
            return ans
        for i in range(n):
            for j in range(m):
                ans[i][j] = (prod//(grid[i][j]%12345))%12345
        return ans
# @lc code=end

