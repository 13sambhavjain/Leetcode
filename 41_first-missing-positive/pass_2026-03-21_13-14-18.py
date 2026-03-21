# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 41 — first-missing-positive
# Status   : Accepted ✅
# Date     : 2026-03-21 13:14:18
# Cases    : 179/179
# Runtime  : 54 ms (beats 44.84%)
# Memory   : 30.8 MB (beats 72.76%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from typing import List, Optional, Dict, Tuple
from collections import defaultdict, deque
#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(n := len(nums)):
            x = nums[i]
            while n >= x > 0 and x != nums[x-1]:
                nums[x-1], x = x, nums[x-1]
        for i in range(n):
            if nums[i] != (i + 1):
                return i + 1
        return n + 1
        raise NotImplementedError

# @lc code=end
# ob = Solution()
# tc = [
#     dict(nums=[1,2,0]),
#     dict(nums = [3,4,-1,1]),
#     dict(nums = [7,8,9,11,12]),
# ]
# r = []
# for t in tc:
#     r.append(ob.firstMissingPositive(**t))
# print(r)

