# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 32 — longest-valid-parentheses
# Status   : Accepted ✅
# Date     : 2026-03-21 08:11:40
# Cases    : 235/235
# Runtime  : 15 ms (beats 22.47%)
# Memory   : 22.9 MB (beats 6.03%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        open = 0
        current = 0
        ans = 0
        prev = []
        for c in s:
            if c == ')':
                if open:
                    open -= 1
                    current += 2
                    if prev and (prev[-1][1] == open):
                        current += prev.pop()[0]
                    ans = max(current, ans)
                else:
                    current = 0
                    prev.clear()
                    open = 0
            else:
                prev.append((current, open))
                open += 1
                current = 0
        return ans

        raise NotImplementedError

# @lc code=end
ob = Solution()
tc = (
    dict(s = "(()"),
    dict(s = ")()())"),
    dict(s = ""),
    dict(s="()(()"),
    dict(s="(())("),
)
rc = [2, 4, 0, 2, 4]
r = []
for t in tc:
    r.append(ob.longestValidParentheses(**t))
print(rc==r, rc, r)


