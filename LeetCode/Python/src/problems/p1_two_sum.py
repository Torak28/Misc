"""
__author__ = "Torak28"
__version__ = "0.1"
__status__ = "PoC"

Link: https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.
"""
from typing import List


class Solution:
    """
    store Solutions
    """

    def two_sum_1(self, nums: List[int], target: int) -> List[int]:
        """
        BruteForce solutions, goes through all possibilities and tries to find a solution
        """
        for i_idx, i in enumerate(nums):
            for j_idx, j in enumerate(nums):
                if i_idx == j_idx:
                    continue
                if i + j == target:
                    return [i_idx, j_idx]
        return []

    def two_sum_2(self, nums: List[int], target: int) -> List[int]:
        """
        A bit clever - subtract `elem` from `target` and searched for it in `nums` list.
        Return `sorted()` list in case of two the same numbers.
        """
        idx_elem = 0
        for idx_elem, elem in enumerate(nums):
            tmp = target - elem
            if tmp in nums:
                idx_tmp = nums.index(tmp)
                if idx_elem == idx_tmp:
                    continue
                break
        return sorted([idx_elem, idx_tmp])
