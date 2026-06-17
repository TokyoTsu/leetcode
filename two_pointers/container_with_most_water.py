

"""
LC 11 — Container With Most Water

Given vertical lines at each index, find two lines that together with
the x-axis form a container holding the most water.

Area between lines i and j = min(height[i], height[j]) * (j - i)
i.e. (height of the SHORTER line) * (horizontal distance between them).

Approach: two pointers from both ends, moving inward.
Start at maximum width, then greedily shrink toward taller lines.

Time:  O(n)  — each pointer moves inward at most n times total
Space: O(1)  — only scalar variables
"""

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1      # widest possible container: both ends
        maxArea = 0

        while l < r:
            # Water is capped by the SHORTER of the two walls; width is r - l.
            currentArea = min(height[l], height[r]) * (r - l)
            maxArea = max(maxArea, currentArea)

            # Move the pointer at the SHORTER line inward.
            # Why: the shorter line is the limiting factor. Moving the taller one
            # can only keep or lower the height while losing width — never better.
            # Moving the shorter one is the only move that could find a taller wall.
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return maxArea