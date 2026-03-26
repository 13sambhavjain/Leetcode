# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 77 — combinations
# Status   : Accepted ✅
# Date     : 2026-03-26 18:50:04
# Cases    : 27/27
# Runtime  : 99 ms (beats 83.81%)
# Memory   : 61.3 MB (beats 68.72%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from typing import List, Optional, Dict, Tuple
from collections import defaultdict, deque
#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def helper(self, i):
        if i == self.k:
            self.ans.append(self.curr[1:])
            return
        for n in range(self.curr[i]+1, self.n+1):
            self.curr[i+1] = n
            self.helper(i+1)

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.curr = [0] + [0]*k
        self.ans = []
        self.n = n
        self.k = k
        self.helper(0)
        return self.ans
# @lc code=end
ob = Solution()
tc = [
    dict(n = 4, k = 2),
]
r = []
for t in tc:
    r.append(ob.combine(**t))
print(*r, sep='\n')

