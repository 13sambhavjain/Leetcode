# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 3548 — equal-sum-grid-partition-ii
# Status   : Failed ❌
# Date     : 2026-03-26 09:37:46
# ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
# Input    : [[10,5,4,5]]
# Expected : Expected Answer
# Got      : true
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from typing import List, Optional, Dict, Tuple
from collections import defaultdict, deque
#
# @lc app=leetcode id=3548 lang=python3
#
# [3548] Equal Sum Grid Partition II
#

# @lc code=start
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        tsum = sum(sum(row) for row in grid)
        h_sum = tsum/2 #no floor div
        # check on splits of a single line
        m, n = len(grid), len(grid[0])
        for start, end, diff in ((0, m-1, 1), (m-1, 0, -1)):
            sum_till = 0
            setill = set()
            for i in range(start,end, diff):
                setill.update(grid[i])
                sum_till += sum(grid[i])
                if sum_till == h_sum:
                    return True
                elif sum_till > h_sum:
                    # sum_till - x = tsum - sum_till
                    x = 2*sum_till - tsum
                    if i == start:
                        if x == grid[start][0] or x == grid[start][-1]:
                            return True
                    elif x in setill:
                        return True
        for start, end, diff in ((0, n-1, 1), (n-1, 0, -1)):
            sum_till = 0
            setill = set()
            for j in range(start,end,diff):
                setill.update(grid[i][j] for i in range(m))
                sum_till += sum(grid[i][j] for i in range(m))
                if sum_till == h_sum:
                    return True
                elif sum_till > h_sum:
                    # sum_till - x = tsum - sum_till
                    x = 2*sum_till - tsum
                    if j == start:
                        if x == grid[0][start] or x == grid[-1][start]:
                            return True
                    elif x in setill:
                        return True
        return False
        
# @lc code=end

