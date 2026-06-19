from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        LC 128 — Longest Consecutive Sequence

        Return the length of the longest run of consecutive integers in nums.
        Required to run in O(n) time, so sorting (O(n log n)) is off the table.

        Key insight: every consecutive sequence has exactly ONE natural starting
        point — the number whose predecessor (n-1) is absent from the set. By
        only expanding a sequence from its start, each number is visited at most
        twice total (once in the loop, once during a walk), keeping it O(n).

        Time:  O(n)  — the inner while loop runs only from sequence starts, so
                       across the whole run each element is counted once
        Space: O(n)  — the set of all numbers
        """
        numsSet = set(nums)      # O(1) membership tests; dedups automatically
        longest = 0

        for n in numsSet:
            # Only begin counting if n is the START of a sequence, i.e. n-1
            # is not present. This is what prevents re-counting the same
            # sequence from its middle and is the crux of the O(n) bound.
            if (n - 1) not in numsSet:
                length = 1                     # current run length, counting n itself

                # Walk forward as long as the next consecutive number exists.
                while (n + length) in numsSet:
                    length += 1

                longest = max(length, longest)

        return longest