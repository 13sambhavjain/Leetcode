# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 2751 — robot-collisions
# Status   : Accepted ✅
# Date     : 2026-04-01 10:04:33
# Cases    : 2433/2433
# Runtime  : 1309 ms (beats 5.95%)
# Memory   : 48.8 MB (beats 44.05%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from typing import List, Optional, Dict, Tuple
import collections
#
# @lc app=leetcode id=2751 lang=python3
#
# [2751] Robot Collisions
#

# @lc code=start
from dataclasses import dataclass
@dataclass
class Robot():
    pos: int
    dir: str
    health: int
    index: int
class Solution:

    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        line :list[Robot] = sorted((Robot(positions[i], directions[i], healths[i], i) for i in range(n)), key=lambda robot: robot.pos)
        found = 0
        at = []
        i = 0
        while i < len(line):
            if line[i].dir == 'R':
                found += 1
                i += 1
            else:
                while found and len(line) > 1:
                    if (line[i-1].health) == (line[i].health):
                        found -= 1
                        line.pop(i)
                        line.pop(i-1)
                        i -= 1
                        break
                    elif line[i-1].health > line[i].health:
                        line[i-1].health -= 1
                        line.pop(i)
                        # no change in i
                        break
                    else:
                        line[i].health -= 1
                        line.pop(i-1)
                        found -= 1
                        # current is shifted to i-1
                        i -= 1
                        continue
                else:
                    # means there is a one robot goind to left .. 
                    # no root is going to collide with it as all before it are gone, or are going to left themselves
                    i += 1
        # line here must be pure .. ans
        line.sort(key=lambda robot: robot.index)
        return [robot.health for robot in line]
            


# @lc code=end

