# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 2069 — walking-robot-simulation-ii
# Status   : Accepted ✅
# Date     : 2026-04-07 10:00:08
# Cases    : 
# Runtime  : Runtime (beats 71%)
# Memory   : ms (beats Beats%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# @lc app=leetcode id=2069 lang=python3
#
# [2069] Walking Robot Simulation II
#

# @lc code=start
from itertools import cycle
class Robot:
    Directions = cycle(["East", "North", "West", "South"])
    Move = dict(East=(1, 0), North=(0, 1), West=(-1, 0), South=(0, -1))
    def __init__(self, width: int, height: int):
        self.dir = next(self.Directions)
        self.w = width
        self.h = height
        self.pos = 0
        self.peri = 2 * (width + height - 2)
        self.start = True
    def step(self, num: int) -> None:
        self.pos = (self.pos + num)%self.peri
        self.start = False
    def getPos(self) -> List[int]:
        if self.start:
            return [0,0]
        pos = self.pos
        if pos < self.w:
            return [pos, 0]
        pos -= self.w - 1
        if pos < self.h:
            return [self.w - 1, pos]
        pos -= self.h - 1
        if pos < self.w:
            return [self.w - 1 - pos, self.h - 1]
        pos -= self.w - 1
        if pos < self.h:
            return [0, self.h - 1 - pos]
        return [pos - (self.h - 1), 0]
    def getDir(self) -> str:
        if self.start:
            return "East"
        pos = self.pos
        if pos == 0:
            return "South"
        if pos < self.w:
            return "East"
        pos -= self.w - 1
        if pos < self.h:
            return "North"
        pos -= self.h - 1
        if pos < self.w:
            return "West"
        pos -= self.w - 1
        if pos < self.h:
            return "South"
        return "East"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
# @lc code=end

