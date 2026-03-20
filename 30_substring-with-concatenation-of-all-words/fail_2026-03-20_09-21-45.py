# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 30 — substring-with-concatenation-of-all-words
# Status   : Failed ❌
# Date     : 2026-03-20 09:21:45
# ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
# Input    : "a..."
# Expected : list(range(5001))
# Got      : TLE 181/182 cases passed (N/A)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from typing import List, Optional, Dict, Tuple
from collections import defaultdict, deque
#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
class Solution:
    def helper(self, s: str, words: list[str], start: int) -> bool:
        for i in range(start, start + self.nc, self.n1):
            if (curr:=s[i:i+self.n1]) in words:
                words.remove(curr)
            else:
                return False
        return True
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words)
        self.n1 = len(words[0])
        self.nc = n*self.n1
        ans = []
        for i in range(len(s) - self.nc + 1):
            if self.helper(s, words.copy(), i):
                ans.append(i)
        return ans
        raise NotImplementedError
# @lc code=end

