# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 30 — substring-with-concatenation-of-all-words
# Status   : Accepted ✅
# Date     : 2026-03-20 09:52:11
# Cases    : 182/182
# Runtime  : 725 ms (beats 30.06%)
# Memory   : 19.8 MB (beats 85.25%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from typing import List, Optional, Dict, Tuple
from collections import defaultdict, deque
#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
from collections import Counter
class Solution:
    def helper(self, s: str, words: Counter) -> bool:
        if s in self.dp:
            return True
        for i in range(0, len(s), self.n1):
            if (curr:=s[i:i+self.n1]) in words:
                words.subtract([curr])
                if words[curr] == 0:
                    del words[curr]
            else:
                return False
        self.dp.add(s)
        return True
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words)
        self.n1 = len(words[0])
        self.nc = n*self.n1
        ans = []
        self.dp :set[str]= set()
        c_words = Counter(words)
        for i in range(len(s) - self.nc + 1):
            if self.helper(s[i:self.nc+i], c_words.copy()):
                ans.append(i)
        return ans
        raise NotImplementedError
# @lc code=end

# ob = Solution()
# tc = (
#     dict(s="wordgoodgoodgoodbestword",words =["word","good","best","word"]),
# )
# r = []

# for t in tc:
#     r.append(ob.findSubstring(**t))

# print(r)
