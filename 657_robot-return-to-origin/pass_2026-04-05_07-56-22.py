# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 657 — robot-return-to-origin
# Status   : Accepted ✅
# Date     : 2026-04-05 07:56:22
# Cases    : 78/78
# Runtime  : 15 ms (beats 60.08%)
# Memory   : 19.2 MB (beats 67.4%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# @lc app=leetcode id=657 lang=python3
#
# [657] Robot Return to Origin
#

# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        h = 0
        v = 0
        for m in moves:
            if m == 'U':
                v += 1
            elif m == 'D':
                v-=1
            elif m == 'L':
                h -= 1
            else: # m == 'R':
                h += 1
        return v == 0 and h==0 
# @lc code=end

