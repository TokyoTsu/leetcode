# 0045. Jump Game II
# https://leetcode.com/problems/jump-game-ii/
# Difficulty: Medium
# Topic: Arrays, Greedy
#
# Problem:
# Given an array of integers nums where nums[i] is the max jump length
# from index i, return the minimum number of jumps to reach the last index.
#
# Approach:
# Sliding window greedy. Maintain a window [l, r] representing the indices
# reachable in the current number of jumps. For each window, find the
# farthest index reachable from any position within it. Advance the window
# and increment jump count. Stop when r reaches or passes the last index.
#
# Time:  O(n)
# Space: O(1)

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1

        return res
