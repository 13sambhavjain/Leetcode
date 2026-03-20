# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 3567 — minimum-absolute-difference-in-sliding-submatrix
# Status   : Accepted ✅
# Date     : 2026-03-20 08:54:04
# Cases    : 723/723
# Runtime  : 35 ms (beats 95.16%)
# Memory   : 19.4 MB (beats 62.9%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# @lc app=leetcode id=3567 lang=python3
#
# [3567] Minimum Absolute Difference in Sliding Submatrix
#

# @lc code=start
class Solution:
    def helper(self, grid, k, i, j) -> int:
        l = []
        for i1 in range(i, i+k):
            l.extend(grid[i1][j:j+k])
        l = sorted(set(l))
        if len(l) > 1:
            d = l[1] - l[0]
        else:
            return 0
        for p in range(1, len(l)):
            d = min(d, l[p] - l[p-1])
        return d
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # brute force
        m, n = map(len, (grid, grid[0]))
        ans = [[0]*(n-k+1) for _ in range(m-k+1)]
        if k == 1:
            return ans
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                ans[i][j] = self.helper(grid, k, i, j)
        return ans
# @lc code=end

