# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 10 — regular-expression-matching
# Status   : Accepted ✅
# Date     : 2026-03-19 17:25:25
# Cases    : 354/354
# Runtime  : 8874 ms (beats 5.02%)
# Memory   : 19.5 MB (beats 62.91%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str, i=0, j=0) -> bool:
        if i == len(s) and j == len(p):
            return True
        if j < len(p):
            if p[j] == '*':
                if self.isMatch(s, p, i, j+1):
                    return True
                elif i < len(s):
                    if p[j-1] == s[i] or p[j-1] == '.':
                        return self.isMatch(s, p, i + 1, j)
                    else:
                        return False
                else:
                    return False
            elif (j+1) < len(p) and p[j+1] == '*':
                return self.isMatch(s, p, i, j + 1)
            elif p[j] == '.':
                return self.isMatch(s, p, i + 1, j + 1)       
            elif i < len(s) and p[j] == s[i]:
                return self.isMatch(s, p, i+1, j+1)
            else:
                return False
        else:
            return False
        
# @lc code=end

