# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Problem  : 83 — remove-duplicates-from-sorted-list
# Status   : Accepted ✅
# Date     : 2026-03-26 18:31:17
# Cases    : 
# Runtime  : Runtime (beats 0%)
# Memory   : ms (beats Beats%)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        p = head
        q = p.next
        while q:
            if p.val == q.val:
                q = q.next
                del p.next
                p.next = q
            else:
                p = q
                q = q.next
        return head 
# @lc code=end

