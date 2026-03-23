# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 1594 — maximum-non-negative-product-in-a-matrix
# Status   : Accepted ✅
# Date     : 2026-03-23 21:10:40
# Cases    : 159/159
# Runtime  : 7 ms (beats 44.74%)
# Memory   : 21.3 MB (beats 22.81%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from typing import List, Optional, Dict, Tuple
from collections import defaultdict, deque
#
# @lc app=leetcode id=1594 lang=python3
#
# [1594] Maximum Non Negative Product in a Matrix
#
# @lc code=start
from functools import cache
class Solution:
    @cache
    def traverse(self, i, j) -> tuple:
        if (val:=self.grid[i][j]) == 0:
             return (0,)
        if i == (self.m-1):
            if j == (self.n - 1):
                return (val,)
            else:
                x = self.traverse(i, j+1)
        elif j == (self.n-1):
            x = self.traverse(i+1, j)
        else:
            x = *self.traverse(i+1, j), *self.traverse(i, j+1)
        possible = {i*val for i in x}
        # print(possible)
        ans = []
        if (temp:=min(possible)) < 0:
            ans.append(temp)
        if (temp:=max(possible)) > 0:
            ans.append(temp)
        if 0 in possible:
            ans.append(0)
        return tuple(ans)
        
    def maxProductPath(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid
        x = max(*self.traverse(0, 0), -1)
        MOD = 1000000007
        if x > MOD:
            x %= MOD
        return x
        raise NotImplementedError
# @lc code=end
# ob = Solution()
# tc = [
#     # dict(grid=[[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]),
#     dict(grid=[[2,1,3,0,-3,3,-4,4,0,-4],[-4,-3,2,2,3,-3,1,-1,1,-2],[-2,0,-4,2,4,-3,-4,-1,3,4],[-1,0,1,0,-3,3,-2,-3,1,0],[0,-1,-2,0,-3,-4,0,3,-2,-2],[-4,-2,0,-1,0,-3,0,4,0,-3],[-3,-4,2,1,0,-4,2,-4,-1,-3],[3,-2,0,-4,1,0,1,-3,-1,-1],[3,-4,0,2,0,-2,2,-4,-2,4],[0,4,0,-3,-4,3,3,-1,-2,-2]]),
# ]
# results = [-1, 19215865]
# r = []
# for t in tc:
#     r.append(ob.maxProductPath(**t))
# print(Solution.traverse.cache_info())
# cac = {
#     (i, j) :[ob.traverse(i, j), ob.grid[i][j]] for j in reversed(range(ob.n)) for i in reversed(range(ob.m))
# }
# print(*cac.items(), sep='\n')
# print(Solution.traverse.cache_info())
# print(r)
