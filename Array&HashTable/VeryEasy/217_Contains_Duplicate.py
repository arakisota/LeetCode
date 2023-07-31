"""
時間計算量 : O(1), 99.49%
空間計算量 : O(1), 78.61%
→等号で条件分岐させた方が空間計算量が少ないぽい
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True