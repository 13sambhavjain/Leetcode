# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 874 — walking-robot-simulation
# Status   : Accepted ✅
# Date     : 2026-04-06 10:53:55
# Cases    : 51/51
# Runtime  : 43 ms (beats 37.52%)
# Memory   : 23.9 MB (beats 47.05%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from typing import List, Optional, Dict, Tuple
import collections
#
# @lc app=leetcode id=874 lang=python3
#
# [874] Walking Robot Simulation
#

# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set((x[0], x[1]) for x in obstacles)
        dir = collections.namedtuple("dir", "index mult")
        dir_l = (dir(1, 1), dir(0, 1), dir(1, -1), dir(0, -1))
        ans = 0
        current = [0, 0]
        d = 0
        for c in commands:
            if c > 0:
                for _ in range(c):
                    new = current.copy()
                    new[dir_l[d].index] += dir_l[d].mult
                    if (new[0], new[1]) in obs:
                        break
                    current = new
                ans = max(ans, current[0]**2 + current[1]**2)
            elif c == -1:
                d = (d+1)%4
            else: # c == -2:
                d = (d-1)%4
        return ans

# @lc code=end
ob = Solution()
tc = [
    dict(commands = [4,-1,3], obstacles = []),
    dict(commands = [4,-1,4,-2,4], obstacles = [[2,4]]),
    

]
r = []
for t in tc:
    r.append(ob.robotSim(**t))
print(r)
