from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        LC 15 — 3Sum

        Find all unique triplets (a, b, c) in nums such that a + b + c = 0.

        Strategy: sort, then for each element fix it as the smallest of the
        triplet and reduce the rest to a Two-Sum-on-a-sorted-array problem
        solved with two pointers converging from both ends.

        Sorting is what makes everything work: it lets the two pointers know
        which way to move (sum too big -> shrink from the right; too small ->
        grow from the left) and lets us skip duplicates by comparing neighbors.

        Time:  O(n^2)  — outer loop O(n), inner two-pointer scan O(n)
        Space: O(1)    — excluding the output (sort is in-place)
        """
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            # Once the fixed element is positive, the two larger numbers after
            # it are positive too, so no triplet can sum to 0. Safe to stop.
            if n > 0:
                break

            # Skip duplicate values for the fixed element to avoid duplicate
            # triplets (e.g. two identical -1's would produce the same results).
            if i > 0 and n == nums[i - 1]:
                continue

            # Two pointers over the remaining (sorted) subarray to the right.
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = n + nums[l] + nums[r]   # the actual quantity we care about

                if s > 0:
                    r -= 1                  # too big -> need a smaller value
                elif s < 0:
                    l += 1                  # too small -> need a bigger value
                else:
                    # Exact match: record it, then move BOTH pointers inward
                    # to look for further pairs with the same fixed element.
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicate left values so we don't repeat triplets.
                    # Bounds check (l < r) comes FIRST so we never index
                    # nums[l] out of range.
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res