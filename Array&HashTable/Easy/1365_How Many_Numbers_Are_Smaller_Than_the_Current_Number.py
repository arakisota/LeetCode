"""
時間計算量 : O(nlogn), 80.3%
空間計算量 : O(n), 68.46%
"""

from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        mapping = {}
        result = []
        for i in range(len(temp)):
            if temp[i] not in mapping:
                mapping[temp[i]] = i
        for i in range(len(nums)):
            result.append(mapping[nums[i]])

        return result