# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 3548 — equal-sum-grid-partition-ii
# Status   : Accepted ✅
# Date     : 2026-03-26 18:11:29
# Cases    : 942/942
# Runtime  : 619 ms (beats 91.67%)
# Memory   : 43.6 MB (beats 100%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from typing import List, Optional, Dict, Tuple
from collections import defaultdict, deque
#
# @lc app=leetcode id=3548 lang=python3
#
# [3548] Equal Sum Grid Partition II
#

# @lc code=start
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        tsum = sum(sum(row) for row in grid)
        h_sum = tsum/2 #no floor div
        # check on splits of a single line
        m, n = len(grid), len(grid[0])
        if m == 1 or n == 1:
            if n == 1:
                arr = list(grid[i][0] for i in range(m))
            else:
                arr = grid[0]
            if arr[0] == h_sum or arr[-1] == h_sum:
                return True
            
            sum_till = arr[0]
            for i in range(1, len(arr)-1):
                if 2*sum_till == tsum - arr[i]:
                    return True
                sum_till += arr[i]
                if sum_till < h_sum:
                    if tsum - arr[-1] == 2*sum_till:
                        return True 
                elif sum_till == h_sum:
                    return True
                else:
                    if tsum + arr[0] == 2*sum_till:
                        return True
            return False
        for start, end, diff in ((0, m-1, 1), (m-1, 0, -1)):
            sum_till = 0
            setill = set()
            for i in range(start,end, diff):
                setill.update(grid[i])
                sum_till += sum(grid[i])
                if sum_till == h_sum:
                    return True
                elif sum_till > h_sum:
                    # sum_till - x = tsum - sum_till
                    x = 2*sum_till - tsum
                    if i == start:
                        if x == grid[start][0] or x == grid[start][-1]:
                            return True
                    elif x in setill:
                        return True
        for start, end, diff in ((0, n-1, 1), (n-1, 0, -1)):
            sum_till = 0
            setill = set()
            for j in range(start,end,diff):
                setill.update(grid[i][j] for i in range(m))
                sum_till += sum(grid[i][j] for i in range(m))
                if sum_till == h_sum:
                    return True
                elif sum_till > h_sum:
                    # sum_till - x = tsum - sum_till
                    x = 2*sum_till - tsum
                    if j == start:
                        if x == grid[0][start] or x == grid[-1][start]:
                            return True
                    elif x in setill:
                        return True
        return False
        
# @lc code=end

ob = Solution()
tc = [
    dict(grid = [[73816],[71688]]),
    dict(grid = [[10,5,4,5]]),
    dict(grid = [[25372],[100000],[100000]])
]
r = []
for t in tc:
    r.append(ob.canPartitionGrid(**t))
print(r)