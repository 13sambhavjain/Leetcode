# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 51 — n-queens
# Status   : Accepted ✅
# Date     : 2026-03-23 22:03:14
# Cases    : 9/9
# Runtime  : 11 ms (beats 68.96%)
# Memory   : 19.9 MB (beats 26.74%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from typing import List, Optional, Dict, Tuple
from collections import defaultdict, deque
#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def make(self, col:List[int]):
        if len(col) != self.n:
            raise RuntimeError("Something Wrong in Logic")
        ans = []
        row = ['.']*self.n
        for i in col:
            row[i] = 'Q'
            ans.append(''.join(row))
            row[i] = '.'
        return ans
    def helper(self, i):
        if i == self.n:
            self.ans.append(self.make(self.col))
        for j in set(range(self.n)).difference(self.col):
            if ((a:=i - j) in self.d1) or ((b:=i + j) in self.d2):
                continue
            self.d1.add(a)
            self.d2.add(b)
            self.col.append(j)
            self.helper(i+1)
            self.d1.remove(a)
            self.d2.remove(b)
            self.col.pop()
            
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [['Q']]
        self.n = n
        self.col = []
        self.d1 = set() # i - j
        self.d2 = set() # i + j
        self.ans = []
        self.helper(0)
        return self.ans


        raise NotImplementedError
        
# @lc code=end
ob = Solution()
tc = [
    dict(n = 1),
]
r = []      
for t in tc:
    r.append(ob.solveNQueens(**t))
print(r)

