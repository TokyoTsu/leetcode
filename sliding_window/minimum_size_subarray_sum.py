from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        LC 209 — Minimum Size Subarray Sum

        Find the length of the shortest contiguous subarray whose sum is
        >= target. Return 0 if no such subarray exists.

        Sliding window: expand the window by moving `r` right, adding to the
        running total. Whenever the window sum reaches target, record its
        length and shrink from the left to look for an even shorter window.

        Why O(n) despite the nested while: `r` advances n times, and `l` only
        ever moves forward and never passes `r`, so `l` also advances at most
        n times total. Each element is added once and removed once -> O(n).

        Time:  O(n)
        Space: O(1)
        """
        res = float('inf')
        l = 0
        total = 0

        for r in range(len(nums)):
            total += nums[r]                 # grow window to the right
            while total >= target:           # window qualifies — try to shrink it
                res = min(res, r - l + 1)
                total -= nums[l]             # drop the leftmost element
                l += 1                       # shrink from the left

        return res if res != float('inf') else 0