# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 65 — valid-number
# Status   : Accepted ✅
# Date     : 2026-03-24 20:32:53
# Cases    : 
# Runtime  : Runtime (beats 0%)
# Memory   : ms (beats Beats%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from typing import List, Optional, Dict, Tuple, List
from collections import defaultdict, deque
#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#

# @lc code=start
class Solution:
    def remove_sign(self, s: str) -> str:
        if s and (s[0] == '+' or s[0] == '-'):
            return s[1:]
        return s
    def check_int(self, s: str) -> bool:
        s = self.remove_sign(s)
        return s.isdigit()
    def check_deci(self, s: str) -> bool:
        if '.' not in s:
            return False
        s = self.remove_sign(s)
        if s[-1] == '.':
            return s[:-1].isdigit()
        elif s[0] == '.':
            return s[1:].isdigit()
        else:
            l = s.split('.')
            return len(l) <= 2 and not any(not x.isdigit() for x in l)
    def isNumber(self, s: str) -> bool:
        c = s.count('e') + s.count('E')
        if c > 1:
            return False
        if c:
            l = s.split('e')
            if len(l) == 1:
                l = s.split('E')
            return (self.check_deci(l[0]) or self.check_int(l[0])) and self.check_int(l[1])
        return self.check_deci(s) or self.check_int(s)
        raise NotImplementedError

ob = Solution()
tc = [
#     dict(s =
# "-1E+3"),
dict(s="i.1")
]
r = []
for t in tc:
    r.append(ob.isNumber(**t))
print(r)# @lc code=end


