# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 2075 — decode-the-slanted-ciphertext
# Status   : Accepted ✅
# Date     : 2026-04-04 07:45:00
# Cases    : 
# Runtime  : Runtime (beats 267%)
# Memory   : ms (beats Beats%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# @lc app=leetcode id=2075 lang=python3
#
# [2075] Decode the Slanted Ciphertext
#

# @lc code=start
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText)//rows
        next = cols+1
        buffer = ""
        for i in range(cols):
            j = i
            while j < len(encodedText):
                buffer += encodedText[j]
                j += next
        
        return buffer.rstrip()
# @lc code=end

