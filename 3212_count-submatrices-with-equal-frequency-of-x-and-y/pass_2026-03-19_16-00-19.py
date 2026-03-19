# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 3212 — count-submatrices-with-equal-frequency-of-x-and-y
# Status   : Accepted ✅
# Date     : 2026-03-19 16:00:19
# Cases    : 770/770
# Runtime  : 451 ms (beats 78.49%)
# Memory   : 103.7 MB (beats 82.8%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from typing import List, Optional, Dict, Tuple
from collections import defaultdict, deque

#
# @lc app=leetcode id=3212 lang=python3
#
# [3212] Count Submatrices With Equal Frequency of X and Y
#

# @lc code=start
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        ans = 0
        prev = [[0,0] for _ in range(len(grid[0]))]
        for i in range(len(grid)):
            # print(prev)÷
            row = [0, 0]
            for j in range(len(grid[0])):
                if grid[i][j] == 'X':
                    row[0] += 1
                elif grid[i][j] == 'Y':
                    row[1] += 1
                prev[j][0] += row[0]
                prev[j][1] += row[1]
                if prev[j][0] and prev[j][0] == prev[j][1]:
                    ans += 1
        return ans
# @lc code=end

