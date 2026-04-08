# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 5 — longest-palindromic-substring
# Status   : Accepted ✅
# Date     : 2026-04-08 18:58:20
# Cases    : 143/143
# Runtime  : 6567 ms (beats 8.1%)
# Memory   : 19.3 MB (beats 51.27%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def helper(self, i, j) -> bool:
        s, n = self.s, self.n
        if i >= n or i > j:
            return False
        if i == j or i == (j-1):
            return True
        if s[i] == s[j-1]:
            return self.helper(i+1, j-1)
        return False
        
    def longestPalindrome(self, s: str) -> str:
        self.s = s
        self.n = n =len(s)
        if n < 1:
            return s
        ans = 1, 0, 1
        for i in range(n):
            for j in range(i+ans[0]+1, n+1):
                if self.helper(i, j):
                    ans = j-i, i, j
        return s[ans[1]:ans[2]]
        
# @lc code=end

