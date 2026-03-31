# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 3474 — lexicographically-smallest-generated-string
# Status   : Accepted ✅
# Date     : 2026-03-31 09:56:01
# Cases    : 739/739
# Runtime  : 303 ms (beats 33.33%)
# Memory   : 20.5 MB (beats 12.82%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from collections import defaultdict
#
# @lc app=leetcode id=3474 lang=python3
#
# [3474] Lexicographically Smallest Generated String
#

# @lc code=start
class Solution:
    # def helper(self, str2, f, ans):
    #     if f == len(self.falses):
    #         # success
    #         pass
    #         return 
    #     fr = self.falses[f]
    #     for j in range(len(str2)):
    #         if ans[fr + j] == "":
                
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        str2 = list(str2)
        ans = [""]*(n+m-1)
        falses = []
        for i, c in enumerate(str1):
            if c == 'T':
                for j in range(m):
                    if ans[i+j] == "":
                        ans[i+j] = str2[j]
                    elif ans[i+j] != str2[j]:
                        return ""
            else:
                falses.append(i)
        can_change = dict()
        for index, i in enumerate(falses):
            last = i-1
            for j in range(m):
                if ans[i+j] != "":
                    if ans[i+j] != str2[j]:
                        break
                else:
                    can_change[i+j] = index
                    ans[i+j] = 'a'
                    if ans[i+j] != str2[j]:
                        break
                    last = max(last, i+j)
            else:
                # no break
                # means need to last one different
                if last == i-1:
                    for k in range(i+m, last, -1):
                        if k in can_change:
                            not_allowed = set()
                            for findex in range(can_change[k], index+1):
                                fat = falses[findex]
                                not_allowed.add(ord(str2[k-fat]))
                            if len(not_allowed) == 26:
                                # cannot put anything
                                continue
                            for i in range(ord('a'), ord('z')+1):
                                if i not in not_allowed:
                                    ans[k] = chr(i)
                                    break
                            break
                    else:
                        return ""
                ans[last] = 'b'
                continue
            # break -> no need to do anything already doesnt match
        for i, c in enumerate(ans):
            if c == "":
                ans[i] = 'a'
        return ''.join(ans)        
        
# @lc code=end

