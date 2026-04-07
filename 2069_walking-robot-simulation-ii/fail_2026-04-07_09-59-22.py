# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 2069 — walking-robot-simulation-ii
# Status   : Failed ❌
# Date     : 2026-04-07 09:59:22
# ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
# Input    : 76 / 142
# Expected : Wrong
# Got      : wrong
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
        self.pos = [0,0]
    def step(self, num: int) -> None:
        x, y = self.pos
        x1, y1 = self.Move[self.dir]
        for i in range(num):
            if 0 <= x + x1 < self.w and 0 <= y + y1 < self.h:
                x += x1
                y += y1
            else:
                self.pos = [x, y]
                self.dir = next(self.Directions)
                return self.step(num - i)
        self.pos = [x, y]

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.dir


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
# @lc code=end

