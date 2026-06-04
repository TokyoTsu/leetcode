# 0049. Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# Difficulty: Medium
# Topic: Arrays, Hash Map, Sorting
#
# Problem:
# Given an array of strings, group the anagrams together.
# Return the groups in any order.
#
# Approach:
# Sort each string to produce a canonical key — all anagrams
# share the same sorted form. Use a defaultdict to accumulate
# strings under their key, then return the grouped values.
#
# Time:  O(n * k log k)  where n = number of strings, k = max string length
# Space: O(n * k)

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)

        return list(groups.values())
