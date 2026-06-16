
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        LC 238 — Product of Array Except Self

        Return an array where res[i] = product of all elements except nums[i],
        without using division and in O(n) time.

        Key idea: the product of everything except index i is
            (product of all elements to its LEFT) * (product of all elements to its RIGHT).
        We compute these two running products in two passes and combine them
        directly in the result array — no extra arrays needed.

        Time:  O(n)  — two linear passes
        Space: O(1)  — output array excluded, only two scalar accumulators used
        """
        res = [1] * len(nums)

        # ---- Pass 1: left-to-right ----
        # `prefix` holds the product of all elements strictly BEFORE i.
        # We write it into res[i] before folding nums[i] in, so index i
        # never includes itself.
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix          # res[i] = product of everything to the left of i
            prefix *= nums[i]        # extend the running left-product to include i

        # ---- Pass 2: right-to-left ----
        # `postfix` holds the product of all elements strictly AFTER i.
        # Multiply it into res[i], which already contains the left product,
        # giving left * right = product of everything except nums[i].
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix        # combine: (left product) * (right product)
            postfix *= nums[i]       # extend the running right-product to include i

        return res