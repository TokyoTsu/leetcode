from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        LC 42 — Trapping Rain Water

        Given an elevation map, compute how much rain water it can trap.

        Key insight: the water sitting on top of bar i is bounded by the
        shorter of (tallest bar to its left) and (tallest bar to its right).
        So  water[i] = min(maxLeft[i], maxRight[i]) - height[i].

        We precompute those two "tallest so far" arrays in one pass each
        (prefix max from the left, suffix max from the right), then sum the
        trapped water at every index.

        Time:  O(n)  — three linear passes
        Space: O(n)  — two auxiliary arrays
        """
        n = len(height)
        max_left = [0] * n      # max_left[i]  = tallest bar in height[0..i]
        max_right = [0] * n     # max_right[i] = tallest bar in height[i..n-1]

        # Pass 1: prefix maxima (tallest wall at or to the left of i)
        max_height = 0
        for i in range(n):
            max_height = max(max_height, height[i])
            max_left[i] = max_height

        # Pass 2: suffix maxima (tallest wall at or to the right of i)
        max_height = 0
        for i in range(n - 1, -1, -1):
            max_height = max(max_height, height[i])
            max_right[i] = max_height

        # Pass 3: water above each bar is capped by the shorter surrounding wall
        area = 0
        for i in range(n):
            area += min(max_left[i], max_right[i]) - height[i]

        return area