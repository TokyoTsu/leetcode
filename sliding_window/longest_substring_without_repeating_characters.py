from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        LC 3 — Longest Substring Without Repeating Characters

        Return the length of the longest substring of s containing no repeated
        characters.

        Sliding window: `r` expands the window to the right one char at a time.
        If s[r] is already inside the window, shrink from the LEFT (removing
        s[l] and advancing l) until the duplicate is gone — then the window is
        valid again. Track the largest window size seen.

        Why O(n) despite the nested while: each character is added to the set
        once (by r) and removed at most once (by l). Both pointers only move
        forward, so total work is linear, not quadratic.

        Time:  O(n)
        Space: O(min(n, charset)) — the set holds at most one window of chars
        """
        charSet = set()      # characters currently inside the window [l, r]
        l = 0                # left edge of the window
        res = 0              # longest valid window length seen so far

        for r in range(len(s)):
            # If s[r] duplicates a char already in the window, shrink from the
            # left until that duplicate is evicted.
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])                # extend window to include s[r]
            res = max(res, r - l + 1)        # window size = r - l + 1

        return res