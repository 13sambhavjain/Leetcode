# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 424 — longest-repeating-character-replacement
# Status   : Accepted ✅
# Date     : 2026-03-30 20:03:18
# Cases    : 
# Runtime  : Runtime (beats 8008%)
# Memory   : ms (beats Beats%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = k
        i = 0
        while i < len(s):
            x = k
            new = i
            while new < len(s) and s[new] == s[i]:
                new += 1
            for j in range(max(new, i+1), len(s)):
                if s[j] != s[i]:
                    if x:
                        x -= 1
                    else:
                        break #already replaced k character, can take this one
            else:
                # means some x is left
                # assuming cant reach the previos same character for a better ans .. just add x
                # just changing i 
                if (i-x) <= 0:
                    return len(s) # no need to continue
                ans = max(len(s) - i + x, ans)
                i = max(new, i+1)
                continue

            ans = max(j - i, ans)
            i = max(new, i+1)
        return ans
        
# @lc code=end
ob = Solution()
tc = [
    dict(s ="CADBBB", k = 4),
]
r = []
for t in tc:
    r.append(ob.characterReplacement(**t))
print(r)

