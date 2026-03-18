# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 3070 — count-submatrices-with-top-left-element-and-sum-less-than-k
# Status   : Accepted ✅
# Date     : 2026-03-18 09:58:20
# Cases    : 859/859
# Runtime  : 117 ms (beats 96.55%)
# Memory   : 53.9 MB (beats 100%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from typing import List, Optional, Dict, Tuple
from collections import defaultdict, deque

#
# @lc app=leetcode id=3070 lang=python3
#
# [3070] Count Submatrices with Top-Left Element and Sum Less Than k
#

# @lc code=start
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        limit_j = len(grid[0])
        prev_sum = [0]*limit_j
        ans = 0
        for i in range(len(grid)):
            sumt = 0
            for j in range(limit_j):
                prev_sum[j] += grid[i][j]
                sumt += prev_sum[j]
                if sumt <= k:
                    ans += 1
                else:
                    limit_j = j
                    break
        return ans
# @lc code=end  

