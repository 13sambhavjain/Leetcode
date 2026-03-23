# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 52 — n-queens-ii
# Status   : Accepted ✅
# Date     : 2026-03-23 22:11:55
# Cases    : 9/9
# Runtime  : 11 ms (beats 44.6%)
# Memory   : 19.4 MB (beats 42%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
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
            self.ans += 1
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
            
    def totalNQueens(self, n: int) -> int:
        if n == 1:
            return 1
        self.n = n
        self.col = []
        self.d1 = set() # i - j
        self.d2 = set() # i + j
        self.ans = 0
        self.helper(0)
        return self.ans   
# @lc code=end

