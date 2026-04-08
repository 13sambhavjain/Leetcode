# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 213 — house-robber-ii
# Status   : Accepted ✅
# Date     : 2026-04-08 08:30:34
# Cases    : 75/75
# Runtime  : 0 ms (beats 100%)
# Memory   : 19.3 MB (beats 77.92%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from typing import List, Optional, Dict, Tuple
from collections import defaultdict, deque
#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [(0, nums[0]), (nums[1], 0), (nums[2], nums[2]+nums[0])] + [None]*(n-3)
        for i in range(3, n):
            dp[i] = (nums[i] + max(dp[i-2][0], dp[i-3][0]), nums[i] + max(dp[i-3][1], dp[i-2][1]))
        # cant take dp[-1][1] - 
        return max(dp[-1][0], max(dp[-2]), max(dp[-3]))
        
# @lc code=end

