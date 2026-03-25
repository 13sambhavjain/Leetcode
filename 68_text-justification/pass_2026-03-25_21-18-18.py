# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 68 — text-justification
# Status   : Accepted ✅
# Date     : 2026-03-25 21:18:18
# Cases    : 29/29
# Runtime  : 0 ms (beats 100%)
# Memory   : 19.3 MB (beats 72.72%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from typing import List, Optional, Dict, Tuple
from collections import defaultdict, deque

#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        start = 0
        chars = len(words[0])
        for i in range(1, len(words)):
            if (chars + 1 + len(words[i])) > maxWidth:
                # line decided - will not be the last line
                # adding line to answer
                slots = (i - start) - 1 #words - 1, words are from start to i-1 (included)
                if slots == 0:
                    extraleft = maxWidth - chars
                    ans.append(words[start] + " "*extraleft)
                else:
                    each_slot, extraleft = divmod(maxWidth - chars, slots) 
                    each_slot += 1 #already count in chars for extra space (necessary)
                    space = ' '*each_slot
                    for j in range(start, start + extraleft):
                        words[j] += ' '
                    ans.append(space.join(words[start:i]))
                # reseting vars
                start = i
                chars = len(words[i]) # space sfter first word only not before it so no +1
            else:
                chars += 1 + len(words[i])
        # handling last line
        ans.append(' '.join(words[start:]) + " "*(maxWidth-chars))
        return ans
            

# @lc code=end

