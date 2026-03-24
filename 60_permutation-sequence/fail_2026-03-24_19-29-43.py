# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 60 — permutation-sequence
# Status   : Failed ❌
# Date     : 2026-03-24 19:29:43
# ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
# Input    : 1, 1
# Expected : ""
# Got      : "1"
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
import functools
@functools.cache
def factorial(i):
    if i <= 2:
        return i
    return i*factorial(i-1)
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = []
        left = list(range(1, n+1))
        for i in range(n-1, 0, -1):
            x, k = divmod(k, factorial(i))
            if k == 0:
                ans.append(left.pop(x-1))
                ans.extend(reversed(left))
                break
            ans.append(left.pop(x))
        return ''.join(str(x) for x in ans)
        raise NotImplementedError
        
# @lc code=end

