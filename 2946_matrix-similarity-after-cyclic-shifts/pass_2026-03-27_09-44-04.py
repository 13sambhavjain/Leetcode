# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 2946 — matrix-similarity-after-cyclic-shifts
# Status   : Accepted ✅
# Date     : 2026-03-27 09:44:04
# Cases    : 914/914
# Runtime  : 2 ms (beats 67.65%)
# Memory   : 19.3 MB (beats 91.18%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from typing import List, Optional, Dict, Tuple
from collections import defaultdict, deque
#
# @lc app=leetcode id=2946 lang=python3
#
# [2946] Matrix Similarity After Cyclic Shifts
#

# @lc code=start
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        if (k := k%(n := len(mat[0]))) == 0:
            return True
        k1 = n - k
        for i, row in enumerate(mat):
            if i&1:
                if row[k1:] + row[:k1] != row:
                    return False
            elif row[k:] + row[:k] != row:
                return False
        return True
# @lc code=end

