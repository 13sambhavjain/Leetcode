# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 10 — regular-expression-matching
# Status   : Accepted ✅
# Date     : 2026-03-20 08:23:22
# Cases    : Analysis
# Runtime  :  (beats Solution%)
# Memory   : Runtime (beats 6619%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if len(p) > 1 and p[1] == '*':
            return (
                self.isMatch(s, p[2:]) or
                (bool(s) and (p[0] == '.' or s[0] == p[0]) and self.isMatch(s[1:], p))
            )
        elif p[0] == '.':
            return (bool(s) and self.isMatch(s[1:], p[1:]))
        else:
            return bool(s) and s[0] == p[0] and self.isMatch(s[1:], p[1:])
        
# @lc code=end

